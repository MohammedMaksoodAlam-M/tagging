# Question Tagging System

AI-powered classification system for Indian competitive exam questions (TNPSC, Banking, SSC-Railways). Tags each question with a 3-level taxonomy: **Subject > Topic > Subtopic** from a fixed set of 1,606 valid triplets.

## Architecture

- **Single-stage classification**: One AI call per question directly selects the best Subject-Topic-Subtopic triplet
- **Dual provider**: Ollama (primary, local) with OpenAI GPT-4o-mini as fallback
- **Strict validation**: Only exact matches from the exam-specific taxonomy are accepted
- **Rule-based pre-filter**: Pattern-matching classifier bypasses AI for known question formats
- **Retry logic**: Up to 3 attempts per question with enhanced prompts on retry

## Key Files

### Core Pipeline
- `batch_question_extractor.py` - Extracts question batches from main CSV (1.8M questions) into Excel format
- `separate_by_exam.py` - Separates input questions into 3 exam tabs based on OptionE column
- `process_separated_excel.py` - Main entry point: orchestrates exam-specific classification
- `exam_specific_classifier.py` - Single-stage AI classifier using exam-specific taxonomies
- `verify_classifications.py` - Post-classification AI verification; highlights mismatches yellow

### Support Modules
- `config.py` - All configuration: providers, models, paths, prompts, validation rules
- `taxonomy_constants.py` - Generated file containing all exam-specific triplets (do not edit manually)
- `generate_taxonomy_constants_by_exam.py` - Generates taxonomy_constants.py from Tags_New.xlsx
- `multi_tab_excel_processor.py` - Reads/writes multi-tab Excel files (TNPSC, Banking, SSC-Railways)
- `ollama_client.py` - Ollama API wrapper with circuit breaker and fallback model support
- `openai_client.py` - OpenAI API wrapper with rate limiting and cost tracking
- `cost_tracker.py` - Tracks API usage costs in USD/INR with budget enforcement
- `rule_based_classifier.py` - Pattern-based classifier for known question formats
- `file_name_utils.py` - Utilities for parsing/generating filenames with question ranges

## Folder Structure

```
tagging/
├── input/     → InputExcel.xlsx (raw questions)
├── output/    → SeparatedQuestions.xlsx (after exam separation)
├── result/    → ClassifiedQuestions.xlsx (final tagged output)
├── tags/      → Tags_New.xlsx (exam-specific taxonomy source, 3 tabs)
├── temp/      → Progress snapshots and backups during processing
└── logs/      → processing_errors.log, api_costs.json
```

## Workflow

```
1. batch_question_extractor.py  →  input/InputExcel.xlsx
2. separate_by_exam.py          →  output/SeparatedQuestions.xlsx (3 tabs)
3. process_separated_excel.py   →  result/ClassifiedQuestions.xlsx (3 tabs, tagged)
4. verify_classifications.py    →  Highlights mismatches yellow in result Excel
```

## Exam Separation Logic (OptionE Column)

| OptionE value                | Exam type    |
|------------------------------|-------------|
| Exactly "Answer not known"   | TNPSC       |
| Has content, not above       | Banking     |
| Blank / empty / whitespace   | SSC-Railways|

## Taxonomy Structure

Source: `tags/Tags_New.xlsx` (3 tabs: TNPSC, Banking, SSCRailways)
Generated into: `taxonomy_constants.py` via `generate_taxonomy_constants_by_exam.py`

Format: `Subject > Topic > Subtopic` (e.g., "Indian Polity (UNIT 4) > Fundamental Rights > Right to equality")

| Exam         | Subjects | Triplets |
|--------------|----------|----------|
| TNPSC        | 9        | 693      |
| Banking      | 3        | 227      |
| SSC-Railways | 6        | 686      |
| **Total**    | -        | **1,606**|

## Output Format

`result/ClassifiedQuestions.xlsx` has 3 tabs (TNPSC, Banking, SSC-Railways). Each row:

| Column   | Description                         |
|----------|-------------------------------------|
| Row No   | Renumbered per tab starting from 1  |
| Subject  | Mapped from taxonomy Subject        |
| Topic    | From taxonomy                       |
| Subtopic | From taxonomy                       |
| Questions| Original question text              |
| OptionA-E| Answer options                      |
| Answer   | Correct answer                      |
| Explanation | Answer explanation               |

## Configuration Reference (config.py)

- **Primary provider**: `PROVIDER_CONFIG["primary_provider"]` - `"ollama"` or `"openai"`
- **Ollama model**: `OLLAMA_CONFIG["model"]` - currently `"qwen2.5:14b"`
- **Ollama timeout**: `OLLAMA_CONFIG["timeout"]` - 120s for 14B model
- **Temperature**: `0.02` (ultra-low for consistency)
- **Batch size**: 1 (single question per API call)
- **Save interval**: Every 10 questions
- **Backup interval**: Every 25 questions
- **Validation**: Strict exact-match only, no partial matches

## Local Model Setup (Ollama)

```bash
# Install Ollama (if not installed)
curl -fsSL https://ollama.com/install.sh | sh

# Pull the recommended model
ollama pull qwen2.5:14b

# Verify it's running
curl http://localhost:11434/api/tags
```

### Model Recommendations (RTX 5070 12GB / i7-14700 / 64GB RAM)

| Model          | VRAM   | Speed          | Accuracy | Use case            |
|----------------|--------|----------------|----------|---------------------|
| qwen2.5:14b    | ~9-10GB| ~5-15s/question| High     | Primary (recommended)|
| qwen2.5:32b    | 12GB+RAM| ~30-60s/question| Highest | Max accuracy fallback|
| phi4:14b        | ~9-10GB| ~5-15s/question| Good     | Alternative          |
| gemma2:9b       | ~6GB   | ~3-8s/question | Low      | Not recommended      |

Why Qwen2.5: 128K context window handles all 693 TNPSC triplets, superior instruction following for exact text copying, excellent structured JSON output, strong multilingual support for Tamil/Hindi content.

## Coding Conventions

- Python 3.12, scripts use `#!/usr/bin/env python3` shebang
- Module docstrings at top of every file describing purpose
- `logging` module for all output (not print, except in `__main__` blocks)
- Config values in `config.py`, not hardcoded in modules
- Type hints used throughout (`typing` module)
- Classes use descriptive names: `ExamSpecificClassifier`, `MultiTabExcelProcessor`
- Try/except imports for optional dependencies (`OLLAMA_AVAILABLE`, `OPENAI_AVAILABLE` flags)
- `dataclass` for structured data (rules, usage records)
- All paths defined in `config.py` PATHS dict
- Excel I/O via `pandas` and `openpyxl`
