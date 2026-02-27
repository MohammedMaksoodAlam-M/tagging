#!/usr/bin/env python3
"""
Exam-Specific Question Classifier - Two-stage AI-powered classification

Classifies questions using exam-specific taxonomies in a two-stage approach:
- Stage 1: Identify the subject area (small set of options, high accuracy)
- Stage 2: Select the exact triplet within that subject (filtered options)
- Maps "Subject" from taxonomy to "Chapter" in output
- Supports dual providers: OpenAI (primary) and Ollama (fallback)
"""

import json
import logging
import time
import os
from typing import Dict, Optional, List
from datetime import datetime

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from taxonomy_constants import get_taxonomy_for_exam

# Import rule-based classifier
try:
    from rule_based_classifier import RuleBasedClassifier, create_default_rules, get_classification_dict
    RULE_BASED_AVAILABLE = True
except ImportError:
    RULE_BASED_AVAILABLE = False
    RuleBasedClassifier = None

# Import AI clients
try:
    from openai_client import OpenAIClient, create_openai_client
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    OpenAIClient = None


# ── Disambiguation hints injected into prompts ──────────────────────────────
# Stage 1: Helps the model pick the correct SUBJECT for each exam.
# Key failure mode: Banking coding/direction questions classified as English.
STAGE1_EXAM_HINTS: Dict[str, str] = {
    "Banking": """
DISAMBIGUATION (Banking exam subjects):
- Arrangement (Linear/Circular/Square/Tabular), Puzzles, Coding-Decoding, Blood Relations, Direction, Inequality, Syllogism, Series/Sequence, Alpha-Numeric → Reasoning
- Grammar, Vocabulary, Fill in Blanks, Error Spotting, Sentence Rearrangement, Reading Comprehension, Match Columns, Cloze Test → English
- Arithmetic, Percentage, Profit/Loss, Speed/Time/Distance, Data Interpretation, Quantitative problems → Aptitude""",
    "TNPSC": "",    # Stage 1 subject detection works well for TNPSC
    "SSC-Railways": "",
}

# Stage 2: Helps the model pick the correct TRIPLET within a subject.
# Key failure mode: TNPSC LCM vs HCF application confusion; Banking Puzzle vs Inequality.
STAGE2_SUBJECT_HINTS: Dict[tuple, str] = {
    ("TNPSC", "Aptitude (Part B Unit 1)"): """
LCM vs HCF KEY DISTINCTIONS:
- "Distribute equally", "fill containers", "tile a floor", "arrange in rows/columns", "largest number that divides exactly", "greatest number that divides" → HCF: Application Sums - HCF-based
- "Bells/alarms ring together", "traffic lights change together", "periodic events happen simultaneously", "after how long will they meet again" → LCM: Application Sums - LCM-based
- Questions involving fractions where you find the LCM of numerator/denominator values → LCM: LCM of Fractions
- "When divided by X leaves remainder Y" type problems → HCF: Problems on Remainders""",
    ("Banking", "Reasoning"): """
TOPIC DISTINCTIONS (Banking Reasoning):
- Questions with symbols like "A > B means A is greater than B", "A @ B means A ≥ B" → Inequality
- "In a certain code APPLE is written as...", letters/numbers are substituted → Coding decoding
- "A walks North, turns East, walks X km..." → Direction
- People sitting in a row, circle, square, hexagon → Linear/Circular/Square/etc. Arrangement
- Multiple attributes assigned to people (floor/colour/profession) in tabular format → Tabular Puzzle""",
}
# ─────────────────────────────────────────────────────────────────────────────


class ExamSpecificClassifier:
    """
    Two-stage question classifier using exam-specific taxonomies

    For each exam type (TNPSC, Banking, SSC-Railways):
    - Stage 1: Identifies the subject from a small list (3-9 options)
    - Stage 2: Selects the exact triplet from that subject's options (avg ~77 options)
    """

    def __init__(self, exam_type: str, config: Dict, ollama_client=None):
        """
        Initialize exam-specific classifier

        Args:
            exam_type: Exam type ("TNPSC", "Banking", or "SSC-Railways")
            config: Configuration dictionary with provider settings
            ollama_client: Optional OllamaClient instance for fallback
        """
        self.exam_type = exam_type
        self.config = config
        self.provider_config = config.get("provider", {})
        self.ollama_client = ollama_client
        self.openai_client = None

        # Setup logging
        self.logger = logging.getLogger(__name__)

        # Load exam-specific taxonomy
        taxonomy = get_taxonomy_for_exam(exam_type)
        if not taxonomy:
            raise ValueError(f"Invalid exam type: {exam_type}")

        self.subjects = taxonomy['subjects']
        self.triplets = taxonomy['triplets']
        self.triplet_dict = taxonomy['triplet_dict']

        # Build subject-to-triplets index for Stage 2
        self.subject_triplets = {}
        for triplet in self.triplets:
            subject = triplet.split(" > ")[0]
            if subject not in self.subject_triplets:
                self.subject_triplets[subject] = []
            self.subject_triplets[subject].append(triplet)

        # Determine primary and fallback providers
        self.primary_provider = self.provider_config.get("primary_provider", "openai")
        self.fallback_provider = self.provider_config.get("fallback_provider", "ollama")
        self.auto_fallback = self.provider_config.get("auto_fallback", True)

        # Initialize providers
        self.initialize_providers()

        # Initialize rule-based classifier
        self.rule_based_config = config.get("rule_based", {})
        self.rule_classifier = None
        if RULE_BASED_AVAILABLE and self.rule_based_config.get("enabled", True):
            try:
                rules = create_default_rules()
                self.rule_classifier = RuleBasedClassifier(rules)
                self.logger.info(f"Rule-based classifier initialized with {len(rules)} rules")
            except Exception as e:
                self.logger.warning(f"Failed to initialize rule-based classifier: {e}")
                self.rule_classifier = None

        # Statistics
        self.stats = {
            'total_classifications': 0,
            'successful_classifications': 0,
            'failed_classifications': 0,
            'validation_failures': 0,
            'rule_based_matches': 0,
            'openai_requests': 0,
            'ollama_requests': 0,
            'provider_fallbacks': 0,
            'total_cost_usd': 0.0,
            'cost_savings_usd': 0.0,
            'average_response_time': 0,
            'low_confidence_count': 0,
            'subject_detection_failures': 0,
            'start_time': datetime.now()
        }

        self.logger.info(f"Exam-specific classifier initialized for {exam_type}")
        self.logger.info(f"  {len(self.subjects)} subjects, {len(self.triplets)} triplets")
        self.logger.info(f"  Subject triplet counts: {', '.join(f'{s}: {len(ts)}' for s, ts in self.subject_triplets.items())}")
        self.logger.info(f"  Primary: {self.primary_provider}, Fallback: {self.fallback_provider}")

    def initialize_providers(self):
        """Initialize AI providers based on configuration"""
        # Initialize OpenAI if available and configured
        if OPENAI_AVAILABLE and (self.primary_provider == "openai" or self.fallback_provider == "openai"):
            openai_config = self.config.get("openai", {})
            api_key = openai_config.get("api_key") or os.getenv("OPENAI_API_KEY")

            if api_key:
                try:
                    self.openai_client = create_openai_client(self.config)
                    self.logger.info("OpenAI client initialized")
                except Exception as e:
                    self.logger.warning(f"Failed to initialize OpenAI client: {e}")
                    self.openai_client = None
            else:
                self.logger.warning("OpenAI API key not found")
                self.openai_client = None

        # Ollama client is passed in constructor
        if self.ollama_client:
            self.logger.info("Ollama client available")

    def _build_combined_context(self, question: str, explanation: str = "") -> str:
        """Build combined question + explanation text"""
        combined = question
        if explanation and explanation.strip() and explanation.lower() != 'nan':
            combined += f"\n\nExplanation: {explanation}"
        return combined

    def create_subject_detection_prompt(self, question: str, explanation: str = "") -> str:
        """
        Stage 1: Create prompt to identify the subject area

        Only sends subject names (3-9 options), not the full triplet list.
        """
        combined_context = self._build_combined_context(question, explanation)

        subjects_formatted = "\n".join([f"{i+1}. {s}" for i, s in enumerate(self.subjects)])

        # Inject exam-level disambiguation hint if available
        exam_hint = STAGE1_EXAM_HINTS.get(self.exam_type, "")
        hint_section = f"\n{exam_hint}" if exam_hint.strip() else ""

        prompt = f"""You are classifying a question for the {self.exam_type} exam.

QUESTION:
{combined_context}

AVAILABLE SUBJECTS (choose exactly one):
{subjects_formatted}{hint_section}

INSTRUCTIONS:
1. Read the question and explanation carefully
2. Identify the PRIMARY knowledge domain being tested
3. Select EXACTLY ONE subject from the list above
4. Use the EXACT subject name as shown - do not modify it

REQUIRED OUTPUT FORMAT (JSON only, no other text):
{{
    "subject": "EXACT_SUBJECT_NAME_FROM_LIST",
    "confidence": 0.85,
    "reasoning": "Brief explanation of why this subject"
}}

RULES:
- Pick EXACTLY ONE subject from the numbered list
- Copy the subject name EXACTLY as shown
- Return ONLY the JSON, no extra text
- Base decision on question content, not answer options"""

        return prompt

    def create_triplet_selection_prompt(self, question: str, explanation: str, subject: str, is_retry: bool = False) -> str:
        """
        Stage 2: Create prompt to select exact triplet within the identified subject

        Only sends triplets for the matched subject (avg ~77 options instead of all 693).
        """
        combined_context = self._build_combined_context(question, explanation)

        # Get triplets for this subject only
        subject_triplets = self.subject_triplets.get(subject, [])
        if not subject_triplets:
            self.logger.error(f"No triplets found for subject: {subject}")
            return ""

        triplets_formatted = "\n".join([f"{i+1}. {t}" for i, t in enumerate(subject_triplets)])

        retry_note = ""
        if is_retry:
            retry_note = """
NOTE: Your previous attempt was rejected because the triplet was not copied exactly.
Copy the COMPLETE triplet character-by-character from the list. Do not modify any part."""

        # Inject subject-level disambiguation hint if available
        subject_hint = STAGE2_SUBJECT_HINTS.get((self.exam_type, subject), "")
        hint_section = f"\n{subject_hint}" if subject_hint.strip() else ""

        prompt = f"""You are classifying a question for the {self.exam_type} exam.
The subject has been identified as: {subject}

QUESTION:
{combined_context}

AVAILABLE TRIPLETS for "{subject}" (choose exactly one):
{triplets_formatted}
{retry_note}{hint_section}
INSTRUCTIONS:
1. Read the question and explanation carefully
2. Find the triplet that best matches the question content
3. Copy the ENTIRE triplet EXACTLY as shown in the list
4. Extract the three parts: Subject > Topic > Subtopic

REQUIRED OUTPUT FORMAT (JSON only, no other text):
{{
    "subject": "{subject}",
    "topic": "EXACT_TOPIC_FROM_TRIPLET",
    "subtopic": "EXACT_SUBTOPIC_FROM_TRIPLET",
    "full_triplet": "EXACT_COMPLETE_TRIPLET_FROM_LIST",
    "confidence": 0.85,
    "reasoning": "Brief explanation of selection"
}}

RULES:
- Select EXACTLY ONE triplet from the numbered list above
- Copy EVERY character exactly including spaces and punctuation
- The subject field MUST be: "{subject}"
- Return ONLY the JSON, no extra text"""

        return prompt

    def parse_subject_response(self, response_text: str) -> Optional[str]:
        """
        Parse Stage 1 response to extract subject

        Returns:
            Subject name string or None if parsing fails
        """
        try:
            if not response_text or not isinstance(response_text, str):
                self.logger.error("Invalid response for subject detection")
                return None

            response_text = response_text.strip()

            # Remove markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            response_text = response_text.strip()

            data = json.loads(response_text)
            subject = (data.get('subject') or '').strip()

            if not subject:
                self.logger.error("Empty subject in response")
                return None

            # Validate subject exists in our list
            if subject in self.subjects:
                return subject

            # Try case-insensitive match
            for valid_subject in self.subjects:
                if subject.lower() == valid_subject.lower():
                    self.logger.info(f"Subject case-corrected: '{subject}' -> '{valid_subject}'")
                    return valid_subject

            # Try partial match as last resort
            for valid_subject in self.subjects:
                if subject.lower() in valid_subject.lower() or valid_subject.lower() in subject.lower():
                    self.logger.warning(f"Subject fuzzy-matched: '{subject}' -> '{valid_subject}'")
                    return valid_subject

            self.logger.warning(f"Subject not found in taxonomy: '{subject}'. Valid subjects: {self.subjects}")
            return None

        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse subject JSON: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Error parsing subject response: {e}")
            return None

    def parse_triplet_response(self, response_text: str) -> Optional[Dict]:
        """
        Parse Stage 2 response to extract triplet classification

        Returns:
            Dictionary with subject, topic, subtopic or None if parsing fails
        """
        try:
            if not response_text or not isinstance(response_text, str):
                self.logger.error("Invalid response for triplet selection")
                return None

            response_text = response_text.strip()

            # Remove markdown code blocks if present
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.startswith("```"):
                response_text = response_text[3:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]
            response_text = response_text.strip()

            data = json.loads(response_text)

            subject = (data.get('subject') or data.get('chapter') or '').strip()
            topic = (data.get('topic') or '').strip()
            subtopic = (data.get('subtopic') or '').strip()
            full_triplet = (data.get('full_triplet') or data.get('triplet') or '').strip()
            confidence = data.get('confidence', 0.0)
            reasoning = data.get('reasoning', '')

            if not (subject and topic and subtopic):
                self.logger.error(f"Missing fields: subject='{subject}', topic='{topic}', subtopic='{subtopic}'")
                return None

            return {
                'subject': subject,
                'topic': topic,
                'subtopic': subtopic,
                'triplet': full_triplet,
                'confidence': confidence,
                'reasoning': reasoning
            }

        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse triplet JSON: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Error parsing triplet response: {e}")
            return None

    def validate_classification(self, result: Dict) -> bool:
        """
        Validate that classification exists in exam-specific taxonomy

        No auto-correction by line number - only accepts exact matches.

        Args:
            result: Classification result dictionary

        Returns:
            True if valid, False otherwise
        """
        subject = result.get('subject', '')
        topic = result.get('topic', '')
        subtopic = result.get('subtopic', '')

        # Construct the triplet for validation
        constructed_triplet = f"{subject} > {topic} > {subtopic}"

        # Check if constructed triplet exists in taxonomy
        if constructed_triplet in self.triplet_dict:
            result['triplet'] = constructed_triplet
            return True

        # If full_triplet was provided, also check it
        full_triplet = result.get('triplet', '')
        if full_triplet and full_triplet in self.triplet_dict:
            # Use the validated full_triplet to correct the individual parts
            parts = full_triplet.split(" > ")
            if len(parts) == 3:
                result['subject'] = parts[0]
                result['topic'] = parts[1]
                result['subtopic'] = parts[2]
                return True

        # Validation failed - log details for debugging
        self.logger.warning(f"Validation failed for {self.exam_type}: {constructed_triplet}")

        # Check if subject exists
        subject_triplets = self.subject_triplets.get(subject, [])
        if subject_triplets:
            self.logger.info(f"Subject '{subject}' has {len(subject_triplets)} valid triplets")
            # Show first few for debugging
            for t in subject_triplets[:3]:
                self.logger.debug(f"  Valid: {t}")
        else:
            similar = [s for s in self.subjects if subject.lower() in s.lower() or s.lower() in subject.lower()]
            if similar:
                self.logger.warning(f"Subject '{subject}' not found. Similar: {similar}")
            else:
                self.logger.warning(f"Subject '{subject}' not found in any form. Valid: {self.subjects}")

        return False

    def classify_with_provider(self, prompt: str, provider: str) -> Optional[str]:
        """
        Get classification from specified provider

        Args:
            prompt: Classification prompt
            provider: "openai" or "ollama"

        Returns:
            Raw response text or None if failed
        """
        try:
            if provider == "openai" and self.openai_client:
                self.stats['openai_requests'] += 1
                response = self.openai_client.make_request(
                    prompt=prompt,
                    question="",
                    operation="classification"
                )
                return response

            elif provider == "ollama" and self.ollama_client:
                self.stats['ollama_requests'] += 1
                response = self.ollama_client.make_request(prompt)
                return response

            else:
                self.logger.error(f"Provider '{provider}' not available")
                return None

        except Exception as e:
            self.logger.error(f"Error calling {provider}: {e}")
            return None

    def _call_provider_with_fallback(self, prompt: str) -> Optional[str]:
        """Call primary provider, fall back to secondary if needed"""
        response = self.classify_with_provider(prompt, self.primary_provider)

        if not response and self.auto_fallback:
            self.logger.info(f"Primary provider failed, falling back to {self.fallback_provider}")
            self.stats['provider_fallbacks'] += 1
            response = self.classify_with_provider(prompt, self.fallback_provider)

        return response

    def _detect_subject(self, question: str, explanation: str) -> Optional[str]:
        """
        Stage 1: Detect the subject area

        Tries up to 2 attempts to get a valid subject.
        """
        for attempt in range(2):
            prompt = self.create_subject_detection_prompt(question, explanation)

            if attempt > 0:
                prompt += "\n\nNOTE: Previous attempt returned an invalid subject. Please select EXACTLY from the numbered list."

            response = self._call_provider_with_fallback(prompt)
            if not response:
                continue

            subject = self.parse_subject_response(response)
            if subject:
                self.logger.info(f"Stage 1 - Subject detected: {subject} (attempt {attempt + 1})")
                return subject

            self.logger.warning(f"Stage 1 - Invalid subject on attempt {attempt + 1}")

        self.stats['subject_detection_failures'] += 1
        return None

    def _select_triplet(self, question: str, explanation: str, subject: str) -> Optional[Dict]:
        """
        Stage 2: Select exact triplet within the detected subject

        Tries up to 3 attempts with enhanced prompts on retry.
        """
        validation_config = self.config.get("validation", {})
        max_retries = validation_config.get("max_validation_retries", 3)

        for attempt in range(max_retries):
            is_retry = attempt > 0
            prompt = self.create_triplet_selection_prompt(question, explanation, subject, is_retry)

            if not prompt:
                return None

            if attempt > 0:
                self.logger.info(f"Stage 2 - Retry {attempt + 1}/{max_retries}")

            response = self._call_provider_with_fallback(prompt)
            if not response:
                continue

            result = self.parse_triplet_response(response)
            if not result:
                self.logger.warning(f"Stage 2 - Failed to parse response on attempt {attempt + 1}")
                continue

            # Validate against taxonomy
            if self.validate_classification(result):
                self.logger.info(f"Stage 2 - Validated on attempt {attempt + 1}: {result['triplet']}")
                return result
            else:
                self.stats['validation_failures'] += 1
                self.logger.warning(f"Stage 2 - Validation failed on attempt {attempt + 1}")

        return None

    def classify_question(self, question: str, explanation: str = "") -> Optional[Dict]:
        """
        Classify a question using two-stage approach

        Stage 1: Identify subject (3-9 options)
        Stage 2: Select exact triplet within that subject (avg ~77 options)

        Args:
            question: Question text
            explanation: Optional explanation text

        Returns:
            Dictionary with subject, topic, subtopic or None if failed
        """
        start_time = time.time()
        self.stats['total_classifications'] += 1

        try:
            # Validate question length
            min_length = self.config.get("validation", {}).get("min_question_length", 10)
            max_length = self.config.get("validation", {}).get("max_question_length", 2000)

            question_stripped = question.strip() if question else ""
            if len(question_stripped) < min_length:
                self.logger.warning(f"Question too short ({len(question_stripped)} chars < {min_length}), skipping")
                self.stats['failed_classifications'] += 1
                return None

            if len(question_stripped) > max_length:
                self.logger.info(f"Question truncated from {len(question_stripped)} to {max_length} chars")
                question_stripped = question_stripped[:max_length]

            # Try rule-based classification first
            if (self.rule_classifier and
                self.rule_based_config.get("enabled", True) and
                self.rule_based_config.get("priority") == "before_ai"):

                rule_result = self.rule_classifier.classify_question(question_stripped, self.exam_type)

                if rule_result.matched:
                    # Validate rule-based result against taxonomy
                    rule_classification = {
                        'subject': rule_result.rule.chapter,
                        'topic': rule_result.rule.topic,
                        'subtopic': rule_result.rule.subtopic,
                        'confidence': rule_result.confidence
                    }

                    constructed = f"{rule_classification['subject']} > {rule_classification['topic']} > {rule_classification['subtopic']}"
                    if constructed in self.triplet_dict:
                        self.stats['rule_based_matches'] += 1
                        self.stats['cost_savings_usd'] += 0.000054
                        self.stats['successful_classifications'] += 1

                        elapsed = time.time() - start_time
                        total = self.stats['total_classifications']
                        current_avg = self.stats['average_response_time']
                        self.stats['average_response_time'] = ((current_avg * (total - 1)) + elapsed) / total

                        if self.rule_based_config.get("log_matches", True):
                            self.logger.info(f"Rule-based: {constructed} (rule: {rule_result.rule.description})")

                        return rule_classification
                    else:
                        self.logger.warning(f"Rule-based triplet not in taxonomy: {constructed}. Falling through to AI.")

            # Stage 1: Detect subject
            subject = self._detect_subject(question_stripped, explanation)
            if not subject:
                self.logger.error("Stage 1 failed: Could not detect subject")
                self.stats['failed_classifications'] += 1
                return None

            # Stage 2: Select exact triplet within subject
            result = self._select_triplet(question_stripped, explanation, subject)
            if not result:
                self.logger.error(f"Stage 2 failed for subject '{subject}'")
                self.stats['failed_classifications'] += 1
                return None

            # Build classification output
            classification = {
                'subject': result['subject'],
                'topic': result['topic'],
                'subtopic': result['subtopic'],
                'confidence': result.get('confidence', 0.0)
            }

            # Check confidence threshold
            confidence_threshold = self.config.get("prompt", {}).get("confidence_threshold", 0.7)
            if classification['confidence'] < confidence_threshold:
                self.stats['low_confidence_count'] += 1
                self.logger.warning(
                    f"Low confidence ({classification['confidence']:.2f} < {confidence_threshold}): "
                    f"{classification['subject']} > {classification['topic']} > {classification['subtopic']}"
                )

            # Update statistics
            self.stats['successful_classifications'] += 1
            elapsed = time.time() - start_time
            total = self.stats['total_classifications']
            current_avg = self.stats['average_response_time']
            self.stats['average_response_time'] = ((current_avg * (total - 1)) + elapsed) / total

            self.logger.info(f"Classified: {classification['subject']} > {classification['topic']} > "
                           f"{classification['subtopic']} (confidence: {classification['confidence']:.2f})")

            return classification

        except Exception as e:
            self.logger.error(f"Classification error: {e}")
            self.stats['failed_classifications'] += 1
            return None

    def get_statistics(self) -> Dict:
        """Get classification statistics"""
        success_rate = 0
        if self.stats['total_classifications'] > 0:
            success_rate = (self.stats['successful_classifications'] /
                          self.stats['total_classifications']) * 100

        return {
            **self.stats,
            'success_rate': round(success_rate, 2),
            'exam_type': self.exam_type,
            'taxonomy_size': len(self.triplets)
        }


def create_exam_classifier(exam_type: str, config: Dict, ollama_client=None) -> ExamSpecificClassifier:
    """
    Create an exam-specific classifier

    Args:
        exam_type: Exam type ("TNPSC", "Banking", or "SSC-Railways")
        config: Configuration dictionary
        ollama_client: Optional Ollama client

    Returns:
        ExamSpecificClassifier instance
    """
    return ExamSpecificClassifier(exam_type, config, ollama_client)


# Module testing
if __name__ == "__main__":
    from config import get_config

    print("EXAM-SPECIFIC CLASSIFIER TESTING")
    print("=" * 50)

    config = get_config()

    # Test classifier for each exam
    for exam_type in ["TNPSC", "Banking", "SSC-Railways"]:
        print(f"\nTesting {exam_type} classifier...")
        try:
            classifier = create_exam_classifier(exam_type, config)
            stats = classifier.get_statistics()
            print(f"  Initialized successfully")
            print(f"  Subjects: {len(classifier.subjects)}")
            print(f"  Triplets: {stats['taxonomy_size']}")
            print(f"  Subject breakdown:")
            for subject, triplets in classifier.subject_triplets.items():
                print(f"    {subject}: {len(triplets)} triplets")
        except Exception as e:
            print(f"  Error: {e}")

    print("\nExam-specific classifier testing completed!")
