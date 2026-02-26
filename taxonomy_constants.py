#!/usr/bin/env python3
"""
Taxonomy Constants - Exam-Specific Taxonomies

Generated on: 2026-02-26 07:27:33
Source: tags/Tags_New.xlsx

Contains exam-specific Subject-Topic-Subtopic taxonomies:
  - TNPSC: 693 unique triplets
  - BANKING: 227 unique triplets
  - SSC_RAILWAYS: 686 unique triplets
"""

from typing import Dict, List


# ===== TNPSC TAXONOMY =====

TNPSC_SUBJECTS: List[str] = [
    "Aptitude (Part B Unit 1)",
    "General Science (Unit 1)",
    "Geography of India (Unit 2)",
    "History, Culture of India, and Indian National Movement (UNIT 3)",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
    "Indian Polity (UNIT 4)",
    "Reasoning (Part B Unit 2)",
    "TAMIL LANGUAGE",
]

TNPSC_TRIPLETS: List[str] = [
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Regulating act of 1773",
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Charter Act of 1833",
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Charter Act of 1853",
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Government of India Act of 1858",
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Indian Councils Act of 1909",
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Government of India Act 1919",
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Government of India Act 1935",
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > India Independence Act 1947",
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Background-Constituent Assembly",
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Constituent Assembly",
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Committees (Major & Minor)",
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Sources of the constitution",
    "Indian Polity (UNIT 4) > Making of Indian Constitution > salient features in Indian Constitution",
    "Indian Polity (UNIT 4) > Preamble > Nature of Indian State",
    "Indian Polity (UNIT 4) > Preamble > Objectives of the constitution",
    "Indian Polity (UNIT 4) > Preamble > Significance of the Preamble",
    "Indian Polity (UNIT 4) > Preamble > Amenability of the Preamble (cases)",
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Evolution of states and Union territories",
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 1",
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 2",
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 3",
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 4",
    "Indian Polity (UNIT 4) > Union, State and Union Territory > State reorganization commissions",
    "Indian Polity (UNIT 4) > Citizenship > Article 5 - 11",
    "Indian Polity (UNIT 4) > Citizenship > Acquisition of Citizenship",
    "Indian Polity (UNIT 4) > Citizenship > Loss of Citizenship",
    "Indian Polity (UNIT 4) > Citizenship > Citizenship Act 1955 and amendments",
    "Indian Polity (UNIT 4) > Fundamental Rights > Right to equality",
    "Indian Polity (UNIT 4) > Fundamental Rights > Right to freedom",
    "Indian Polity (UNIT 4) > Fundamental Rights > Right against exploitation",
    "Indian Polity (UNIT 4) > Fundamental Rights > Right to freedom of Religion",
    "Indian Polity (UNIT 4) > Fundamental Rights > Cultural and educational rights",
    "Indian Polity (UNIT 4) > Fundamental Rights > Rights to constitutional remedies",
    "Indian Polity (UNIT 4) > Fundamental Rights > Impact on fundamental rights",
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Socialistic principles",
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Gandhian principles",
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Liberal - intellectual principles",
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Comparison between DPSP and FRs",
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Important Cases related to FR and DPSP",
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Important amendments",
    "Indian Polity (UNIT 4) > Fundamental Duties > Committees",
    "Indian Polity (UNIT 4) > Fundamental Duties > Article 51A (List of FDs)",
    "Indian Polity (UNIT 4) > Amendments > Types of amendments",
    "Indian Polity (UNIT 4) > Amendments > Emergence of the concept of basic structure",
    "Indian Polity (UNIT 4) > Amendments > Role of judiciary",
    "Indian Polity (UNIT 4) > Union Executive > President",
    "Indian Polity (UNIT 4) > Union Executive > Vice President",
    "Indian Polity (UNIT 4) > Union Executive > Prime Minister",
    "Indian Polity (UNIT 4) > Union Executive > Central Council of Ministers",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Rajya Sabha",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Lok Sabha",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Members of Parliament",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Speaker of the Lok Sabha",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Chairman of Rajya Sabha",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliament - Functioning",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Bills- enactment/procedure, stages in passing bills etc",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Budget",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Powers and functions of parliament Legislative",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Position of Rajya Sabha",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Cabinet committees",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliamentary committees",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliamentary forums",
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliament privileges",
    "Indian Polity (UNIT 4) > State Executive > Governor",
    "Indian Polity (UNIT 4) > State Executive > Comparison between Governor and President",
    "Indian Polity (UNIT 4) > State Executive > Chief Minister",
    "Indian Polity (UNIT 4) > State Executive > State council of ministers",
    "Indian Polity (UNIT 4) > State Legislature > Composition of Two Houses",
    "Indian Polity (UNIT 4) > State Legislature > Duration of Two Houses",
    "Indian Polity (UNIT 4) > State Legislature > Powers and functions",
    "Indian Polity (UNIT 4) > State Legislature > Membership of State Legislature",
    "Indian Polity (UNIT 4) > State Legislature > Presiding Officers of State Legislature",
    "Indian Polity (UNIT 4) > State Legislature > Governor assent to bill",
    "Indian Polity (UNIT 4) > State Legislature > Legislative Procedure in State Legislature",
    "Indian Polity (UNIT 4) > State Legislature > Position of Legislative Counci",
    "Indian Polity (UNIT 4) > State Legislature > State legislature comparison with parliament",
    "Indian Polity (UNIT 4) > State Legislature > Position of state legislative council w.r.t legislative assembly and Rajya Sabha",
    "Indian Polity (UNIT 4) > State Legislature > Sessions of State Legislature",
    "Indian Polity (UNIT 4) > JUDICIARY > Supreme Court",
    "Indian Polity (UNIT 4) > JUDICIARY > High court",
    "Indian Polity (UNIT 4) > JUDICIARY > Jurisdiction and Power",
    "Indian Polity (UNIT 4) > JUDICIARY > Judicial review & judicial activism",
    "Indian Polity (UNIT 4) > JUDICIARY > Subordinate courts",
    "Indian Polity (UNIT 4) > LOCAL SELF GOVERNMENT > Panchayati Raj",
    "Indian Polity (UNIT 4) > LOCAL SELF GOVERNMENT > Municipalities",
    "Indian Polity (UNIT 4) > LOCAL SELF GOVERNMENT > committees",
    "Indian Polity (UNIT 4) > Centre - State Relationships > Inter-state relation",
    "Indian Polity (UNIT 4) > Centre - State Relationships > Legislative relations",
    "Indian Polity (UNIT 4) > Centre - State Relationships > Administrative relations",
    "Indian Polity (UNIT 4) > Centre - State Relationships > Financial relation",
    "Indian Polity (UNIT 4) > Centre - State Relationships > Effects of emergencies",
    "Indian Polity (UNIT 4) > Centre - State Relationships > Committees/Commission related to Centre state relations",
    "Indian Polity (UNIT 4) > Emergency Provisions > National Emergency",
    "Indian Polity (UNIT 4) > Emergency Provisions > President’s Rule",
    "Indian Polity (UNIT 4) > Emergency Provisions > Financial Emergency",
    "Indian Polity (UNIT 4) > Emergency Provisions > Impact of emergency",
    "Indian Polity (UNIT 4) > Constitutional Bodies > Election Commission",
    "Indian Polity (UNIT 4) > Constitutional Bodies > UPSC, SPSC and JPSC",
    "Indian Polity (UNIT 4) > Constitutional Bodies > National Commissions SC/ ST/ Backward classes",
    "Indian Polity (UNIT 4) > Constitutional Bodies > Comptroller and Auditor General of India",
    "Indian Polity (UNIT 4) > Constitutional Bodies > Attorney General",
    "Indian Polity (UNIT 4) > Constitutional Bodies > Advocate general",
    "Indian Polity (UNIT 4) > Constitutional Bodies > Solicitor general",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > National human rights commission & State human rights commission",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Central information commission & State information commission",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Central vigilance commission",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Lokpal and Lokayukta",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > National law commission",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > National green tribunal",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Food safety and standard authority of India",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Bureau of Indian standards",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Competition commission of India",
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Non - Statutory Bodies",
    "Indian Polity (UNIT 4) > Empowerment of Women > Women Empowerment Schemes in India",
    "Indian Polity (UNIT 4) > Empowerment of Women > Constitutional Provisions",
    "Indian Polity (UNIT 4) > Empowerment of Women > Important Acts",
    "Indian Polity (UNIT 4) > Consumer Protection Forums > Consumer Protection Act 2019",
    "Indian Polity (UNIT 4) > Political parties and political system in India > Recognised parties",
    "Indian Polity (UNIT 4) > Political parties and political system in India > non - recognised parties",
    "Indian Polity (UNIT 4) > Election > Representation of people act 1950 & 1951",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Microeconomics vs Macroeconomics",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Sectors of Economy-Primary, Secondary and Tertiary Sector",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Factors of Production",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Type of Economic System",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Growth and Development",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Nature of Indian Economy > Strengths of Indian Economy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Nature of Indian Economy > Weakness of Indian Economy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Nature of Indian Economy > Natural Resources",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Economic Planning in India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Planning Commission of India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > National Development Council (NDC)s",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Five Year Plan",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Niti Aayog",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > National Income > Basic concepts of national income",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > National Income > Money",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > National Income > Money, Demand and Supply",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Expansionary Vs. Contractionary",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Objectives of Monetary Policy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Composition of the MPC",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Methods of Credit Control",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Inflation",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Meaning of Deflation, Disinflation and Stagflation",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Measurement of Inflation",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Reserve Bank of India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Scheduled and Non Scheduled Banks",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Non-Banking Financial Companies(NBFC)",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > All India Financial Institutions (AIFI)- Non Banks",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Issue of Banking Sector",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Meaning of Public Finance",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Budgetary Deficits",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Bodies related to Budgeting",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Basics of Budget",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Components of Budget",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Types of Budget",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > Direct Taxes",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > Indirect Taxes",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > GST",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > Miscellaneous",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > The sources of income as prescribed by the Constitution of India for the Central Government",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > Earnings of state government",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > TAXES LEVIED AND COLLECTED BY THE UNION BUT ASSIGNED TO THE STATES",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > DUTIES LEVIED BY THE UNION BUT COLLECTED AND APPROPRIATED BY THE STATES",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > Taxes which are Levied and Collected by the Union but which may be Distributed between the Union and the States",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > Finance Commission",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Structure of Indian Economy and Employment Generation > Main Sectors in India’s Economy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Structure of Indian Economy and Employment Generation > Other Sectors in India’s Economy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Structure of Indian Economy and Employment Generation > Initiatives for Employment Generation",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Role of Agriculture in Indian Economy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Application of Science and Technology in Agriculture",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Land Reforms",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > ¨ Cropping Pattern in India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > ¨ Types of crops in India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Major Producer of the Crops in India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Cropping Seasons in India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Green Revolution",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Agriculture Related Schemes",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Irrigation",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > PDS",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Minimum support prices (MSP), Procurement prices, Issue Price, Retail prices",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Rural Welfare Oriented Programmes",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Types of Industries",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Core Industries in India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > State-wise Distribution of Industries",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Industrial Policies",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Public Sector Enterprises",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Population",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Education",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Health",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Employment",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Poverty",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > Three indicators",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > Human Development Report",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > 5 Indices of Human Development Report",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > Important Human Development Indicators of Tamil Nadu",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Reform Movements in Tamil Nadu > Social Reformers of Tamilnadu",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Political Parties",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Recognized Tamil Nadu State Parties",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Achievements of the Parties",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Social Welfare Schemes by Tamil Nadu",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Reservation Policy > Reservation Policy in Tamilnadu",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Reservation Policy > Reservation Policy in India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Social Justice Theories",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Constitutional Provisions of social Justice",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Justice Party Contribution",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Welfare and empowerment of SCs, STs, differently abled, women, transgender, aged and senior citizens, child rights",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Various Commissions",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > Highlights of Tamil Nadu Economy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > GI Tags",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > Economic Policies",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > Budget Highlights",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Tamil Nadu Educational System",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Literacy in Tamil Nadu",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Education & Health Related Constitutional Provisions, Acts, Government Schemes",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Education Policy - Tamil Nadu and India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Policy - Tamil Nadu and India",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Systems in Tamil Nadu",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Indicators",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Care Institutions in TN - Primary, Secondary and Tertiary",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Physiographic Divisions",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Land Area Extent",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Climate",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Soils",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Natural Vegetation",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Agriculture",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Livestock",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > water sources",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Mineral resources",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Industries",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Transport and communication",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Demography",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > Institutional frameworks for e-governance",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > Core Infrastructure of Information Technology",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > e-Governance programs",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > e-governance policy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > Achievements and Awards",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > E-Governance Initiatives in Tamilnadu",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > Performance of Tamil Nadu Economy",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > Tamil Nadu related recent Survey, data, Indices, Ranking, Reports, etc",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Public awareness and General administration > Public awareness and General administration",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Current socio-economic issues > Current socio-economic issues",
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Welfare oriented Government schemes and their utility > Welfare oriented Government schemes and their utility",
    "History, Culture of India, and Indian National Movement (UNIT 3) > IVC > Phases of IVC",
    "History, Culture of India, and Indian National Movement (UNIT 3) > IVC > Lifestyle of people during IVC",
    "History, Culture of India, and Indian National Movement (UNIT 3) > IVC > Findings, sites , economic activities",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > ¨ Sources of Gupta Rule",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Important rulers and titles adopted by Gupta kings",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Foreign Travellers Visit - Fahien’s Visit",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Life under Gupta’s",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Post Guptas",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Delhi Sultanate > EARLY MUSLIM INVASIONS",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Delhi Sultanate > Major Dynasties and their rulers",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Delhi Sultanate > Life under Delhi Sultanate",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Establishment of Mughal Empire",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Akbar",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Jahangir and Shah Jahan",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Aurangzeb",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Life under Mughals",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Mughals Contribution",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Rise of Marathas under Shivaji",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Treaty of Purander",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Sambhaji",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Rajaram",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Shahu",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Peshwas under Maratha empire",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Mughals and Marathas conflicts",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > ANGLO-MARATHA WARS",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Decline of Marathas",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Dynasties",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Administration",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Army and military organisation",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Social and economic life",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Social life",
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Rulers of the Bahmani Kingdom",
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > The Five Kingdoms",
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Administration",
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Contribution to Education",
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Art and Architecture",
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Decline of Bahmani Kingdom",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Sangam Age",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Life under Sangam Age",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Kalabras",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Pallavas dynasty",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Chalukya dynasty",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Rashtrakutas dynasty",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Later Pandyas",
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Later Cholas",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Religious development in Medieval India > Sufism",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Religious development in Medieval India > Bhaktism",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Religious development in Medieval India > Sikhism",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > Art and Culture",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > Characteristics of Indian Culture",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > India as a Secular State",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > Social Harmony",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Vedic Age",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Pre Mauryan Age",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Mauryan Age",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Post Mauryan Age",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Foreign successors of Mauryas",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The Portuguese in India",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The Dutch in India",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The Danes in India",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The English",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The French",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > Carnatic Wars",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > BRITISH EXPANSION IN INDIA",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > ECONOMIC POLICIES OF BRITISH",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > IMPACT OF BRITISH ADMINISTRATION",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Early uprising against British rule > Tribal Movements",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Early uprising against British rule > Peasant Movements",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Early uprising against British rule > Politico- religious movements",
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Causes of the Revolt",
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Centres and Spread of the Revolt",
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Leaders of the Revolt",
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Causes of Failure of the Revolt",
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Nature and Impact of the Revolt",
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > SOCIO-RELIGIOUS REFORMS",
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > Muslim reform movements",
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > Miscellaneous movements",
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > PERSONALITIES",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Early Phase Indian National Congress",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > The Moderate Congress (1885-1905)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Political associations in Bengal, Bombay and Madras GoI Act 1861 and 1892",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > The Extremist (1905-1920)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Differences between the Moderates and the Extremists",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Pre congress campaign",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Partition of Bengal (1905)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Swadeshi Movement",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Muslim League, 1906",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Surat Session of INC, 1907",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Indian Council Act (Morley-Minto Act) 1909",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Ghadar Party, 1913",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Komagata Maru Incident 1914",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > First world war and its impact",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > The Lucknow Pact (1916)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Emergence of Gandhi",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > The Government of India Act, 1919",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Rowlatt Act and Jallianwala Bagh Massacre (1919)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Khilafat Movement",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > The Non-Cooperation Movement (1920-22)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Swarajists and no changers",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Nagpur Session of Congress",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Swaraj Party and its Evaluation",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Muddiman Committee (1924)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Simon Commission (1927)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Bardoli Satyagraha (1928)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Nehru Report (1928)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Jinnah’s Fourteen Points",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Calcutta session of INC 1928",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Delhi Manifesto",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Lahore Session, 1929",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Allahabad Address (1930)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Emergence of New Forces during 1920s",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Civil Disobedience Movement (1930-1931)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Round Table ConferencE",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Gandhi-Irwin Pact, 1931",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Karachi session of 1931",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Communal Award",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Poona Pact, 1932",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Government of India Act, 1935",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > World War II and Indian Nationalism",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Resignation of Congress Ministers (1939)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Poona Resolution and Conditional Support to Britain (1941)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > August Offer of 1940",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > The Individual Civil Disobedience",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Two-Nation Theory",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Demand for Pakistan (1942)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Cripps Mission (1942)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Quit India Movement",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Azad Hind Fauj",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Indian National Army",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > N.A. Trials",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > I.N. Rebellion",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Rajagopalachari Formula, 1945",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Desai - Liaqat Pact",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Cabinet Mission (1946)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Wavell Plan",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Jinnah’s Direct Action Resolution",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Mountbatten Plan of June 1947",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Indian Independence Act 1947",
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Communalism and Partition",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > B.R. Ambedkar",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Bhagat Singh",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Bharathiar",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > V.O. Chidambaranar",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Jawaharlal Nehru",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Kamarajar",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Mahatma Gandhi",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Maulana Abul Kalam Azad",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Thanthai Periyar",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Rajaji",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Subash Chandra Bose",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Rabindranath Tagore",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Others",
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Governor of Bengal (Before 1773)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Governor Generals of Bengal (1773-1833)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Governor Generals of India (1832-1858)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Viceroy of India (1858-1947)",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Constitutional Development in India",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Development of Civil Services",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Development of Education",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Development of Press",
    "History, Culture of India, and Indian National Movement (UNIT 3) > Prominent personalities in various spheres > - Arts, Science, Literature and Philosophy",
    "General Science (Unit 1) > Physics > Nature of Universe",
    "General Science (Unit 1) > Physics > General Scientific laws",
    "General Science (Unit 1) > Physics > Force, Motion and Energy",
    "General Science (Unit 1) > Physics > Light",
    "General Science (Unit 1) > Physics > Sound",
    "General Science (Unit 1) > Physics > Heat",
    "General Science (Unit 1) > Physics > Electricity and Magnetism",
    "General Science (Unit 1) > Physics > Nuclear Physics",
    "General Science (Unit 1) > Physics > Laser, Electronics and Communications",
    "General Science (Unit 1) > Physics > Properties of matter",
    "General Science (Unit 1) > Physics > Everyday application of the basic principles of mechanics",
    "General Science (Unit 1) > Scientific knowledge and scientific temper > Scientific knowledge and scientific temper",
    "General Science (Unit 1) > Power of reasoning > Power of reasoning",
    "General Science (Unit 1) > Rote learning vs conceptual learning > Rote learning vs conceptual learning",
    "General Science (Unit 1) > Science as a tool to understand the past, present, and future > Science as a tool to understand the past, present, and future",
    "General Science (Unit 1) > Chemistry > Elements and Compounds",
    "General Science (Unit 1) > Chemistry > Acids, Bases, Salts",
    "General Science (Unit 1) > Chemistry > Petroleum Products",
    "General Science (Unit 1) > Chemistry > fertilizers, pesticides",
    "General Science (Unit 1) > Chemistry > Main concepts of Life Science",
    "General Science (Unit 1) > Chemistry > Classification of Living Organisms",
    "General Science (Unit 1) > Chemistry > Evolution, Genetics",
    "General Science (Unit 1) > Chemistry > Physiology",
    "General Science (Unit 1) > Chemistry > Nutrition",
    "General Science (Unit 1) > Chemistry > Health and Hygiene",
    "General Science (Unit 1) > Chemistry > Human Diseases",
    "General Science (Unit 1) > Chemistry > Environment and ecology",
    "General Science (Unit 1) > Latest inventions in science and technology > Latest inventions in science and technology",
    "Geography of India (Unit 2) > Location and physiography of India > India: An Introduction",
    "Geography of India (Unit 2) > Location and physiography of India > The Himalayas",
    "Geography of India (Unit 2) > Location and physiography of India > Indo Gangetic plain",
    "Geography of India (Unit 2) > Location and physiography of India > Peninsular plateau",
    "Geography of India (Unit 2) > Location and physiography of India > Thar desert",
    "Geography of India (Unit 2) > Location and physiography of India > Coastal plains",
    "Geography of India (Unit 2) > Location and physiography of India > The islands",
    "Geography of India (Unit 2) > Drainage system > Himalayan Rivers",
    "Geography of India (Unit 2) > Drainage system > Peninsular Rivers",
    "Geography of India (Unit 2) > Drainage system > Lakes- types and lakes in India",
    "Geography of India (Unit 2) > Drainage system > Dams and waterfals",
    "Geography of India (Unit 2) > Climate of India > Composition of the Atmosphere",
    "Geography of India (Unit 2) > Climate of India > Layers of the Atmosphere",
    "Geography of India (Unit 2) > Climate of India > Heat Zones of the World",
    "Geography of India (Unit 2) > Climate of India > The factors affecting the climate",
    "Geography of India (Unit 2) > Climate of India > Indian Monsoon",
    "Geography of India (Unit 2) > Natural Vegetation > Classification of forest",
    "Geography of India (Unit 2) > Natural Vegetation > Indian State of Forest Report",
    "Geography of India (Unit 2) > Natural Vegetation > Biodiversity hotspots in India",
    "Geography of India (Unit 2) > Natural Vegetation > Major Threats to Biodiversity",
    "Geography of India (Unit 2) > Natural Vegetation > The Protected Areas of India",
    "Geography of India (Unit 2) > Natural Vegetation > Specialised projects in India",
    "Geography of India (Unit 2) > Agricultural and Soils > Soils of India",
    "Geography of India (Unit 2) > Agricultural and Soils > Irrigation",
    "Geography of India (Unit 2) > Agricultural and Soils > Agriculture IN INDIA",
    "Geography of India (Unit 2) > Agricultural and Soils > Livestock & Fisheries",
    "Geography of India (Unit 2) > Minerals and Natural Resources > Classification of Resources",
    "Geography of India (Unit 2) > Minerals and Natural Resources > Types of minerals",
    "Geography of India (Unit 2) > Minerals and Natural Resources > Industries",
    "Geography of India (Unit 2) > Transport - Communication > Road transport",
    "Geography of India (Unit 2) > Transport - Communication > Railways",
    "Geography of India (Unit 2) > Transport - Communication > Water transport, ports",
    "Geography of India (Unit 2) > Transport - Communication > Air transport",
    "Geography of India (Unit 2) > Transport - Communication > International trade routes",
    "Geography of India (Unit 2) > Transport - Communication > Communication",
    "Geography of India (Unit 2) > Social Geography > Population density and distribution",
    "Geography of India (Unit 2) > Social Geography > Urbanization",
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Racial Groups",
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Religion",
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Tribal Distribution in world",
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Tribal in India",
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Tribals in Tamilnadu",
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Language",
    "Geography of India (Unit 2) > Natural calamity - Disaster Management > Natural disasters",
    "Geography of India (Unit 2) > Natural calamity - Disaster Management > Man-made disasters",
    "Geography of India (Unit 2) > Natural calamity - Disaster Management > National Disaster Management Authority",
    "Geography of India (Unit 2) > Environmental pollution > Pollution",
    "Geography of India (Unit 2) > Environmental pollution > Pollutants",
    "Geography of India (Unit 2) > Environmental pollution > Classification of Pollutants",
    "Geography of India (Unit 2) > Environmental pollution > Types of Pollution",
    "Geography of India (Unit 2) > Environmental pollution > Government Initiatives to Combat Pollution",
    "Geography of India (Unit 2) > Climate Change > Factors Affecting Climate Change",
    "Geography of India (Unit 2) > Climate Change > Evidence for Rapid Climate Change in India",
    "Geography of India (Unit 2) > Climate Change > Effects of climate change in India",
    "Geography of India (Unit 2) > Climate Change > India’s response to Climate Change",
    "Geography of India (Unit 2) > Green energy > Solar Power, Wind Power, Hydropower, Geothermal Energy, Biomass, Biofuels",
    "Geography of India (Unit 2) > Green energy > Renewable Energy Potential States in India",
    "Geography of India (Unit 2) > Green energy > Achievements of India in the Renewable energy sector",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > History of Tamil Society > தமிழர் தோற்றம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > History of Tamil Society > சங்க கால மூவேந்தர்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > History of Tamil Society > சங்க கால தமிழ் நகரங்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > archaeological discoveries > தமிழ்நாடு தொல்லியல் துறையால் அகழாய்வு செய்யப்பட்ட இடங்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > archaeological discoveries > தமிழ் அல்லாத பிற மொழிச் சான்றுகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > archaeological discoveries > வெளிநாட்டினரின் குறிப்புகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > எட்டுத்தொகை",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > பத்துப்பாட்டு",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > பதிணென் கீழ்கணக்கு நூல்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > ஐம்பெரும்காப்பியங்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > ஐஞ்சிறு காப்பியங்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > தொடர்நிலைச்செய்யுள்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > பக்தி இலக்கியம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > மதச்சார்பற்ற தனித்தன்மையுள்ள இலக்கியம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > மானுடத்தின் மீதான திருக்குறளின் தாக்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > அன்றாட வாழ்வியலோடு தொடர்புத் தன்மை",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > திருக்குறளும் மாறாத விழுமியங்களும் - மனிதநேயம், சமத்துவம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > திருக்குறளில் தத்துவக் கோட்பாடுகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > சமூக அரசியல் பொருளாதார நிகழ்வுகளில் திருக்குறளின்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > தமிழ்நாட்டில் நாயக்கர் ஆட்சி",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > புலித்தேவன்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > வீரபாண்டிய கட்டபொம்மன்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > மருது சகோதரர்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > தென்னிந்திய விடுதலைக்கூட்டமைப்பு",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > வேலூர் கிளர்ச்சி",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சென்னை வாசிகள் சங்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சென்னை மகாஜன சங்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சுதேசி நீராவி கப்பல் நிறுவனம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சென்னை ஜனசங்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > தன்னாட்சி இயக்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > ரௌலட் அறப்போராட்டம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > கிலாபத் இயக்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > ஒத்துழையாமை இயக்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > நீல் சிலை அறப்போராட்டம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சைமன் குழு புறக்கணிப்பு",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சட்ட மறுப்பு இயக்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > தனிநபர் சத்தியாக்கிரகம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > வெள்ளையனே வெளியேறு இயக்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > தில்லையாடி வள்ளியம்மை",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > அஞ்சலை அம்மாள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > அம்புஜத்தம்மாள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > முத்துலட்சுமி ரெட்டி",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > எஸ். தர்மாம்பாள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > மூவலூர் இராமாமிர்தம் அம்மையார்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > ருக்மணி லட்சுமிபதி",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > எஸ்.ஆர்.கண்ணம்மா",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > நாகம்மையார்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > துர்க்காபாய் தேஷ்முக்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > இராமலிங்க அடிகளார்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > நாராயணகுரு",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > அய்யன்காளி",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > வைகுண்ட சாமிகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > திராவிடர் மகா ஜனசபை",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > தென்னிந்திய நல உரிமை சங்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > பிராமணரல்லாதார் மாநாடு",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > நீதிக்கட்சியின் கொள்கைகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > சென்னை மாகாண சங்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > நீதிக்கட்சியும் தன்னாட்சி இயக்கமும்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > Justice Party",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > சாதனையாளர்கள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Self Respect Movement > 15 அம்சக் கொள்கை",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Self Respect Movement > சுயமரியாதை இயக்கத்தின் மாநாடு",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Self Respect Movement > சுயமரியாதை இயக்கத்தின் சாதனைகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > பகுத்தறிவு - விளக்கம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > பெண் விடுதலை",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > சமூக சீர்திருத்தம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > வைக்கம் போராட்டம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > அண்ணாவின் பொன்மொழிகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > திராவிடர் கழகம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > தி.மு.க தோற்றம்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > தமிழக முதல்வராக அண்ணாவின் சாதனைகள்",
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > அண்ணாவின் இலக்கிய படைப்புகள்",
    "Aptitude (Part B Unit 1) > Simplification > BODMAS",
    "Aptitude (Part B Unit 1) > Simplification > Powers",
    "Aptitude (Part B Unit 1) > Simplification > Surds & Indices",
    "Aptitude (Part B Unit 1) > Simplification > AP & GP",
    "Aptitude (Part B Unit 1) > Simplification > Special Series",
    "Aptitude (Part B Unit 1) > Percentage > Percentage Increase and Decrease",
    "Aptitude (Part B Unit 1) > Percentage > Exam and Marks Related Problems",
    "Aptitude (Part B Unit 1) > Percentage > Population and Growth Problems",
    "Aptitude (Part B Unit 1) > Percentage > Profit and Loss",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > Problems on Remainders",
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > problems on Multiples and Factors",
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > Prime Factorization and Division Method Usage",
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Mixture and Alligation",
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Problems on Ages",
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Number System",
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Average",
    "Aptitude (Part B Unit 1) > Simple interest > Finding Total Amount, Principal, Interest, Time",
    "Aptitude (Part B Unit 1) > Simple interest > Borrowing and Lending Problem",
    "Aptitude (Part B Unit 1) > Compound interest > Finding Total Amount, Principal, Interest, Time",
    "Aptitude (Part B Unit 1) > Compound interest > Compound Interest When Interest is Compounded Half-Yearly or Quarterly",
    "Aptitude (Part B Unit 1) > Compound interest > Difference Between Simple Interest and Compound Interest",
    "Aptitude (Part B Unit 1) > Area > Square",
    "Aptitude (Part B Unit 1) > Area > Rectangle",
    "Aptitude (Part B Unit 1) > Area > Triangle",
    "Aptitude (Part B Unit 1) > Area > Circle",
    "Aptitude (Part B Unit 1) > Area > Parallelogram",
    "Aptitude (Part B Unit 1) > Area > Trapezoid",
    "Aptitude (Part B Unit 1) > Volume > Cube",
    "Aptitude (Part B Unit 1) > Volume > Cuboid",
    "Aptitude (Part B Unit 1) > Volume > Cone",
    "Aptitude (Part B Unit 1) > Volume > Cylinder",
    "Aptitude (Part B Unit 1) > Volume > Sphere",
    "Aptitude (Part B Unit 1) > Volume > Hemi Sphere",
    "Aptitude (Part B Unit 1) > Time and Work > Work Done by Multiple People Together",
    "Aptitude (Part B Unit 1) > Time and Work > Work and Efficiency Relationship",
    "Aptitude (Part B Unit 1) > Time and Work > Work Done by Alternating Workers",
    "Reasoning (Part B Unit 2) > Logical reasoning > seating arrangment",
    "Reasoning (Part B Unit 2) > Logical reasoning > Chronological order",
    "Reasoning (Part B Unit 2) > Logical reasoning > syllogism",
    "Reasoning (Part B Unit 2) > Logical reasoning > Venn diagram",
    "Reasoning (Part B Unit 2) > Logical reasoning > Calander",
    "Reasoning (Part B Unit 2) > Logical reasoning > Statement and Conclusions",
    "Reasoning (Part B Unit 2) > Puzzles > Box Type Missing numbers",
    "Reasoning (Part B Unit 2) > Puzzles > Number of Triangle Etc",
    "Reasoning (Part B Unit 2) > Puzzles > Blood Relations",
    "Reasoning (Part B Unit 2) > Puzzles > Classification & Odd one out",
    "Reasoning (Part B Unit 2) > Dice > Normal Dice",
    "Reasoning (Part B Unit 2) > Dice > Standard Dice",
    "Reasoning (Part B Unit 2) > Visual reasoning > Clock",
    "Reasoning (Part B Unit 2) > Visual reasoning > Directions",
    "Reasoning (Part B Unit 2) > Visual reasoning > Embeded figures",
    "Reasoning (Part B Unit 2) > Visual reasoning > Figural Classifications",
    "Reasoning (Part B Unit 2) > Visual reasoning > Paper Cutting and Folding",
    "Reasoning (Part B Unit 2) > Visual reasoning > Mirror iamge",
    "Reasoning (Part B Unit 2) > Alpha numeric reasoning > Analogy",
    "Reasoning (Part B Unit 2) > Alpha numeric reasoning > Coding and decoding",
    "Reasoning (Part B Unit 2) > Alpha numeric reasoning > Missing Letters",
    "Reasoning (Part B Unit 2) > Number series > Mathematical Operations",
    "Reasoning (Part B Unit 2) > Number series > Missing numbers",
    "Reasoning (Part B Unit 2) > Number series > Series complete",
    "TAMIL LANGUAGE > எழுத்து > பிரித்து எழுதுதல்‌",
    "TAMIL LANGUAGE > எழுத்து > சேர்த்து எழுதுதல்‌",
    "TAMIL LANGUAGE > எழுத்து > சந்திப்பிழை",
    "TAMIL LANGUAGE > எழுத்து > குறில்‌, நெடில்‌ வேறுபாடு",
    "TAMIL LANGUAGE > எழுத்து > லகர,ளகர, ழகர வேறுபாடு",
    "TAMIL LANGUAGE > எழுத்து > னகர, ணகர வேறுபாடு",
    "TAMIL LANGUAGE > எழுத்து > ரகர, றகர வேறுபாடு",
    "TAMIL LANGUAGE > எழுத்து > இனவெழுத்துகள்‌ அறிதல்‌",
    "TAMIL LANGUAGE > எழுத்து > சுட்டு எழுத்துகள்‌",
    "TAMIL LANGUAGE > எழுத்து > வினா எழுத்துகள்‌",
    "TAMIL LANGUAGE > எழுத்து > ஒருமைப்‌ பன்மை அறிதல்‌",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வேர்ச்சொல்‌ அறிதல்‌",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வேர்ச்சொல்லில்‌ இருந்து வினைமுற்று, வினையெச்சம்‌, வினையாலணையும்‌ பெயர்‌,பெயரெச்சம்‌ வகை அறிதல்‌",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > அயற்சொல்‌ - தமிழ்ச்சொல்‌",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > எதிர்ச்சொல்‌.",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வினைச்சொல்‌",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வினையெச்சம் பெயரெச்சம்",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > எழுத்துப்‌ பிழை, ஒற்றுப்பிழை அறிதல்‌",
    "TAMIL LANGUAGE > சொல் இலக்கணம் > இரண்டு வினைச்‌ சொற்களின்‌ வேறுபாடு அறிதல்‌தொடர் வகைகள்",
    "TAMIL LANGUAGE > சொல்லகராதி > எதிர்ச்சொல்லை எடுத்தெழுதுதல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > ஓரெழுத்து ஒரு மொழிக்கு உரிய பொருளைக்‌ கண்டறிதல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > ஒரு பொருள்‌ தரும்‌ பல சொற்கள்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > பொருந்தா சொல்லைக்‌ கண்டறிதல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > அகர வரிசைப்படி சொற்களைச்‌ சீர்செய்தல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > ஒருபொருள்‌ பன்மொழி",
    "TAMIL LANGUAGE > சொல்லகராதி > இருபொருள்‌ குறிக்கும்‌ சொற்கள்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > பேச்சு வழக்கு, எழுத்து வழக்கு",
    "TAMIL LANGUAGE > சொல்லகராதி > சொல்லும்‌ பொருளும்‌ அறிதல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > ஒரு சொல்லிற்கு இணையான வேறு சொல் அறிதல்‌.",
    "TAMIL LANGUAGE > சொல்லகராதி > கோடிட்ட இடத்தில்‌ சரியான சொல்லைத்‌ தேர்ந்தெடுத்து எழுதுதல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > பொருத்தமான பொருளைத்‌ தெரிவு செய்தல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > ஊர்ப்‌ பெயர்களின்‌ மரூஉவை எழுதுக",
    "TAMIL LANGUAGE > சொல்லகராதி > பிழை திருத்துக. (எ.கா) ஒரு - ஓர்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > பேச்சுவழக்குச்‌ சொற்களுக்கு இணையான தூய தமிழ்ச்‌ சொற்களை இணைத்தல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > பேச்சு வழக்குத்‌ தொடர்களிலுள்ள பிழை திருத்தம்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > சொற்களை இணைத்துப்‌ புதிய சொல்‌ உருவாக்குதல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > அடைப்புக்குள்‌ உள்ள சொல்லைத்‌ தகுந்த இடத்தில்‌ சேர்த்தல்‌",
    "TAMIL LANGUAGE > சொல்லகராதி > பல பொருள்‌ தரும்‌ ஓர்‌ எழுத்து",
    "TAMIL LANGUAGE > சொல்லகராதி > பல பொருள்‌ தரும்‌ ஒரு சொல்லைக்‌ கூறுக",
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > சொற்களை ஒழுங்குபடுத்திச்‌ சொற்றொடர்‌ அமைத்தல்‌",
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > தொடர்‌ வகைகள்‌",
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > செய்வினை, செயப்பாட்டு வினை",
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > தன்வினை, பிறவினை",
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > ஒருமைப்‌ பன்மை பிழையறிந்து சரியான தொடரறிதல்‌",
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > மரபுத்‌ தமிழ்‌: திணை மரபு,பால்‌ மரபு, காலம்‌, இளமைப்‌ பெயர்,வினைமரபு,தொகை மரபு",
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > நிறுத்தல்‌ குறியீடுகள்.",
    "TAMIL LANGUAGE > கலைச்‌ சொற்கள்‌ > பலதுறை சார்ந்த கலைச்‌ சொற்களை அதாவது அறிவியல்‌, கல்வி, மருத்துவம்‌, மேலாண்மை, சட்டம்‌, புவியியல்‌, தொழில்நுட்பம்‌, ஊடகம்‌, தகவல்‌ தொழில்நுட்பம்‌ உள்ளிட்ட பல்துறை சார்ந்த கலைச்‌ சொல்லுக்கு நேரான தமிழ்ச்‌ சொற்களை அறிந்திருக்க வேண்டும்‌.",
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > கொடுக்கப்பட்ட பத்தியிலிருந்து கேட்கப்பட்ட வினாக்களுக்கு சரியான விடையைத்‌ தேர்ந்தெடுத்தல்‌-செய்தித்தாள்‌ - தலையங்கம்‌ - முகப்புச்‌ செய்திகள்‌ - அரசு சார்ந்த செய்திகள்‌ - கட்டுரைகள்‌ - இவற்றை வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ .",
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > உவமைத்‌ தொடரின்‌ பொருளறிதல்‌",
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > மரபுத்‌ தொடரின்‌ பொருளறிதல்‌",
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > பழமொழிகள்‌ பொருளறிதல்‌",
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > ஆவண உள்ளடக்கங்களைப்‌ புரிந்து கொள்ளும்‌ திறன்‌.",
    "TAMIL LANGUAGE > எளிய மொழி பெயர்ப்பு > ஆங்கிலம்‌ மற்றும்‌ பிறமொழிச்‌ சொற்களுக்கு இணையான தமிழ்ச்‌ சொற்கள்‌ அறிதல்‌ வேண்டும்‌",
    "TAMIL LANGUAGE > எளிய மொழி பெயர்ப்பு > பயன்பாட்டில்‌ உள்ள ஆங்கிலச்‌ சொற்களை மொழிபெயர்த்தல்‌ வேண்டும்‌",
    "TAMIL LANGUAGE > எளிய மொழி பெயர்ப்பு > ஆவணங்களின்‌ தலைப்பு - கோப்புகள்‌ - கடிதங்கள்‌ - மனுக்கள்‌ - மொழிபெயர்ப்பு புரிந்து கொள்ளுதல்‌",
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > திருக்குறள்‌ தொடர்பான செய்திகள்‌ (இருபது அதிகாரங்கள்‌ மட்டும்‌) ஒழுக்கமுடைமை, பொறையுடைமை, ஊக்கமுடைமை, விருந்தோம்பல்‌, அறன்‌ வலியுறுத்தல்‌,ஈகை, பெரியாரைத்‌ துணைக்கோடல்‌, வினை செயல்வகை, அவையஞ்சாமை, கண்ணோட்டம்‌, அன்புடைமை, கல்வி,நடுநிலைமை, கூடா ஒழுக்கம்‌, கல்லாமை, செங்கோன்மை, பண்புடைமை, நட்பாராய்தல்‌, புறங்கூறாமை, அருளுடைமை - மேற்கோள்கள்‌.",
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > அறநூல்‌ தொடர்பான செய்திகள்‌ நாலடியார்‌, நான்மணிக்கடிகை, பழமொழி நானூறு, முதுமொழிக்காஞ்சி, திரிகடுகம்‌, இன்னாநாற்பது, சிறுபஞ்சமூலம்‌, ஏலாதி, அவ்வையார்‌ பாடல்கள்‌)",
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > தமிழின்‌ தொன்மை, சிறப்பு, திராவிட மொழிகள்‌ தொடர்பான செய்திகள்‌",
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > உ.வே.சாமிநாத ஐயர்‌, தெ.பொ.மீனாட்சி சுந்தரம்‌, சி.இலக்குவனார்‌ தமிழ்ப்பணி தொடர்பான செய்திகள்‌",
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > தேவநேய பாவாணர்‌, அகரமுதலி, பாவலரேறு பெருஞ்சித்திரனார்‌, ஜி.யு.போப்‌, வீரமாமுனிவர்‌ தமிழ்த்‌ தொண்டு தொடர்பான செய்திகள்‌",
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > தமிழ்ச்‌ சான்றோர்‌ பற்றிய செய்திகள்‌: பாவேந்தர்‌, டி.கே.சிதம்பரனாதர்‌, தவத்திரு குன்றக்குடி அடிகளார்‌, கண்ணதாசன்‌, காயிதே மில்லத்‌, தாரா பாரதி, வேலுநாச்சியார்‌, பட்டுக்கோட்டைக்‌ கல்யாணசுந்தரம்‌, முடியரசன்‌, தமிழ்‌ ஒளி, உருத்திரங்கண்ணனார்‌, கி.வா.ஜகந்நாதர்‌, நாமக்கல்‌ கவிஞர்‌.",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF Basics",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF using Long Division Method",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF of Powers",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF of Decimals",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF of Fractions",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > Relation between HCF & LCM",
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > Application Sums - HCF-based (e.g., dividing items, grouping problems)",
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM Basics",
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM of Powers",
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM of Decimals",
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM of Fractions",
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > Application Sums - LCM-based (alarms, traffic lights, periodic events)",
]

TNPSC_TRIPLET_DICT: Dict[str, Dict[str, str]] = {
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Regulating act of 1773": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Regulating act of 1773"
    },
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Charter Act of 1833": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Charter Act of 1833"
    },
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Charter Act of 1853": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Charter Act of 1853"
    },
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Government of India Act of 1858": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Government of India Act of 1858"
    },
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Indian Councils Act of 1909": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Indian Councils Act of 1909"
    },
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Government of India Act 1919": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Government of India Act 1919"
    },
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > Government of India Act 1935": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "Government of India Act 1935"
    },
    "Indian Polity (UNIT 4) > Evolution of Indian Constitution > India Independence Act 1947": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Evolution of Indian Constitution",
        "subtopic": "India Independence Act 1947"
    },
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Background-Constituent Assembly": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Making of Indian Constitution",
        "subtopic": "Background-Constituent Assembly"
    },
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Constituent Assembly": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Making of Indian Constitution",
        "subtopic": "Constituent Assembly"
    },
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Committees (Major & Minor)": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Making of Indian Constitution",
        "subtopic": "Committees (Major & Minor)"
    },
    "Indian Polity (UNIT 4) > Making of Indian Constitution > Sources of the constitution": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Making of Indian Constitution",
        "subtopic": "Sources of the constitution"
    },
    "Indian Polity (UNIT 4) > Making of Indian Constitution > salient features in Indian Constitution": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Making of Indian Constitution",
        "subtopic": "salient features in Indian Constitution"
    },
    "Indian Polity (UNIT 4) > Preamble > Nature of Indian State": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Preamble",
        "subtopic": "Nature of Indian State"
    },
    "Indian Polity (UNIT 4) > Preamble > Objectives of the constitution": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Preamble",
        "subtopic": "Objectives of the constitution"
    },
    "Indian Polity (UNIT 4) > Preamble > Significance of the Preamble": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Preamble",
        "subtopic": "Significance of the Preamble"
    },
    "Indian Polity (UNIT 4) > Preamble > Amenability of the Preamble (cases)": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Preamble",
        "subtopic": "Amenability of the Preamble (cases)"
    },
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Evolution of states and Union territories": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union, State and Union Territory",
        "subtopic": "Evolution of states and Union territories"
    },
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 1": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 1"
    },
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 2": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 2"
    },
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 3": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 3"
    },
    "Indian Polity (UNIT 4) > Union, State and Union Territory > Article 4": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union, State and Union Territory",
        "subtopic": "Article 4"
    },
    "Indian Polity (UNIT 4) > Union, State and Union Territory > State reorganization commissions": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union, State and Union Territory",
        "subtopic": "State reorganization commissions"
    },
    "Indian Polity (UNIT 4) > Citizenship > Article 5 - 11": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Citizenship",
        "subtopic": "Article 5 - 11"
    },
    "Indian Polity (UNIT 4) > Citizenship > Acquisition of Citizenship": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Citizenship",
        "subtopic": "Acquisition of Citizenship"
    },
    "Indian Polity (UNIT 4) > Citizenship > Loss of Citizenship": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Citizenship",
        "subtopic": "Loss of Citizenship"
    },
    "Indian Polity (UNIT 4) > Citizenship > Citizenship Act 1955 and amendments": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Citizenship",
        "subtopic": "Citizenship Act 1955 and amendments"
    },
    "Indian Polity (UNIT 4) > Fundamental Rights > Right to equality": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Rights",
        "subtopic": "Right to equality"
    },
    "Indian Polity (UNIT 4) > Fundamental Rights > Right to freedom": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Rights",
        "subtopic": "Right to freedom"
    },
    "Indian Polity (UNIT 4) > Fundamental Rights > Right against exploitation": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Rights",
        "subtopic": "Right against exploitation"
    },
    "Indian Polity (UNIT 4) > Fundamental Rights > Right to freedom of Religion": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Rights",
        "subtopic": "Right to freedom of Religion"
    },
    "Indian Polity (UNIT 4) > Fundamental Rights > Cultural and educational rights": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Rights",
        "subtopic": "Cultural and educational rights"
    },
    "Indian Polity (UNIT 4) > Fundamental Rights > Rights to constitutional remedies": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Rights",
        "subtopic": "Rights to constitutional remedies"
    },
    "Indian Polity (UNIT 4) > Fundamental Rights > Impact on fundamental rights": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Rights",
        "subtopic": "Impact on fundamental rights"
    },
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Socialistic principles": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Socialistic principles"
    },
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Gandhian principles": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Gandhian principles"
    },
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Liberal - intellectual principles": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Liberal - intellectual principles"
    },
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Comparison between DPSP and FRs": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Comparison between DPSP and FRs"
    },
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Important Cases related to FR and DPSP": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Important Cases related to FR and DPSP"
    },
    "Indian Polity (UNIT 4) > Directive Principles of State Policy > Important amendments": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Directive Principles of State Policy",
        "subtopic": "Important amendments"
    },
    "Indian Polity (UNIT 4) > Fundamental Duties > Committees": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Duties",
        "subtopic": "Committees"
    },
    "Indian Polity (UNIT 4) > Fundamental Duties > Article 51A (List of FDs)": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Fundamental Duties",
        "subtopic": "Article 51A (List of FDs)"
    },
    "Indian Polity (UNIT 4) > Amendments > Types of amendments": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Amendments",
        "subtopic": "Types of amendments"
    },
    "Indian Polity (UNIT 4) > Amendments > Emergence of the concept of basic structure": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Amendments",
        "subtopic": "Emergence of the concept of basic structure"
    },
    "Indian Polity (UNIT 4) > Amendments > Role of judiciary": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Amendments",
        "subtopic": "Role of judiciary"
    },
    "Indian Polity (UNIT 4) > Union Executive > President": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union Executive",
        "subtopic": "President"
    },
    "Indian Polity (UNIT 4) > Union Executive > Vice President": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union Executive",
        "subtopic": "Vice President"
    },
    "Indian Polity (UNIT 4) > Union Executive > Prime Minister": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union Executive",
        "subtopic": "Prime Minister"
    },
    "Indian Polity (UNIT 4) > Union Executive > Central Council of Ministers": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Union Executive",
        "subtopic": "Central Council of Ministers"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Rajya Sabha": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Rajya Sabha"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Lok Sabha": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Lok Sabha"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Members of Parliament": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Members of Parliament"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Speaker of the Lok Sabha": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Speaker of the Lok Sabha"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Chairman of Rajya Sabha": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Chairman of Rajya Sabha"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliament - Functioning": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Parliament - Functioning"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Bills- enactment/procedure, stages in passing bills etc": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Bills- enactment/procedure, stages in passing bills etc"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Budget": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Budget"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Powers and functions of parliament Legislative": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Powers and functions of parliament Legislative"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Position of Rajya Sabha": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Position of Rajya Sabha"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Cabinet committees": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Cabinet committees"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliamentary committees": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Parliamentary committees"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliamentary forums": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Parliamentary forums"
    },
    "Indian Polity (UNIT 4) > UNION LEGISLATURE > Parliament privileges": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "UNION LEGISLATURE",
        "subtopic": "Parliament privileges"
    },
    "Indian Polity (UNIT 4) > State Executive > Governor": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Executive",
        "subtopic": "Governor"
    },
    "Indian Polity (UNIT 4) > State Executive > Comparison between Governor and President": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Executive",
        "subtopic": "Comparison between Governor and President"
    },
    "Indian Polity (UNIT 4) > State Executive > Chief Minister": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Executive",
        "subtopic": "Chief Minister"
    },
    "Indian Polity (UNIT 4) > State Executive > State council of ministers": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Executive",
        "subtopic": "State council of ministers"
    },
    "Indian Polity (UNIT 4) > State Legislature > Composition of Two Houses": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Composition of Two Houses"
    },
    "Indian Polity (UNIT 4) > State Legislature > Duration of Two Houses": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Duration of Two Houses"
    },
    "Indian Polity (UNIT 4) > State Legislature > Powers and functions": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Powers and functions"
    },
    "Indian Polity (UNIT 4) > State Legislature > Membership of State Legislature": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Membership of State Legislature"
    },
    "Indian Polity (UNIT 4) > State Legislature > Presiding Officers of State Legislature": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Presiding Officers of State Legislature"
    },
    "Indian Polity (UNIT 4) > State Legislature > Governor assent to bill": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Governor assent to bill"
    },
    "Indian Polity (UNIT 4) > State Legislature > Legislative Procedure in State Legislature": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Legislative Procedure in State Legislature"
    },
    "Indian Polity (UNIT 4) > State Legislature > Position of Legislative Counci": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Position of Legislative Counci"
    },
    "Indian Polity (UNIT 4) > State Legislature > State legislature comparison with parliament": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "State legislature comparison with parliament"
    },
    "Indian Polity (UNIT 4) > State Legislature > Position of state legislative council w.r.t legislative assembly and Rajya Sabha": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Position of state legislative council w.r.t legislative assembly and Rajya Sabha"
    },
    "Indian Polity (UNIT 4) > State Legislature > Sessions of State Legislature": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "State Legislature",
        "subtopic": "Sessions of State Legislature"
    },
    "Indian Polity (UNIT 4) > JUDICIARY > Supreme Court": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "JUDICIARY",
        "subtopic": "Supreme Court"
    },
    "Indian Polity (UNIT 4) > JUDICIARY > High court": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "JUDICIARY",
        "subtopic": "High court"
    },
    "Indian Polity (UNIT 4) > JUDICIARY > Jurisdiction and Power": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "JUDICIARY",
        "subtopic": "Jurisdiction and Power"
    },
    "Indian Polity (UNIT 4) > JUDICIARY > Judicial review & judicial activism": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "JUDICIARY",
        "subtopic": "Judicial review & judicial activism"
    },
    "Indian Polity (UNIT 4) > JUDICIARY > Subordinate courts": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "JUDICIARY",
        "subtopic": "Subordinate courts"
    },
    "Indian Polity (UNIT 4) > LOCAL SELF GOVERNMENT > Panchayati Raj": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "LOCAL SELF GOVERNMENT",
        "subtopic": "Panchayati Raj"
    },
    "Indian Polity (UNIT 4) > LOCAL SELF GOVERNMENT > Municipalities": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "LOCAL SELF GOVERNMENT",
        "subtopic": "Municipalities"
    },
    "Indian Polity (UNIT 4) > LOCAL SELF GOVERNMENT > committees": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "LOCAL SELF GOVERNMENT",
        "subtopic": "committees"
    },
    "Indian Polity (UNIT 4) > Centre - State Relationships > Inter-state relation": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Centre - State Relationships",
        "subtopic": "Inter-state relation"
    },
    "Indian Polity (UNIT 4) > Centre - State Relationships > Legislative relations": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Centre - State Relationships",
        "subtopic": "Legislative relations"
    },
    "Indian Polity (UNIT 4) > Centre - State Relationships > Administrative relations": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Centre - State Relationships",
        "subtopic": "Administrative relations"
    },
    "Indian Polity (UNIT 4) > Centre - State Relationships > Financial relation": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Centre - State Relationships",
        "subtopic": "Financial relation"
    },
    "Indian Polity (UNIT 4) > Centre - State Relationships > Effects of emergencies": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Centre - State Relationships",
        "subtopic": "Effects of emergencies"
    },
    "Indian Polity (UNIT 4) > Centre - State Relationships > Committees/Commission related to Centre state relations": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Centre - State Relationships",
        "subtopic": "Committees/Commission related to Centre state relations"
    },
    "Indian Polity (UNIT 4) > Emergency Provisions > National Emergency": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Emergency Provisions",
        "subtopic": "National Emergency"
    },
    "Indian Polity (UNIT 4) > Emergency Provisions > President’s Rule": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Emergency Provisions",
        "subtopic": "President’s Rule"
    },
    "Indian Polity (UNIT 4) > Emergency Provisions > Financial Emergency": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Emergency Provisions",
        "subtopic": "Financial Emergency"
    },
    "Indian Polity (UNIT 4) > Emergency Provisions > Impact of emergency": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Emergency Provisions",
        "subtopic": "Impact of emergency"
    },
    "Indian Polity (UNIT 4) > Constitutional Bodies > Election Commission": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Constitutional Bodies",
        "subtopic": "Election Commission"
    },
    "Indian Polity (UNIT 4) > Constitutional Bodies > UPSC, SPSC and JPSC": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Constitutional Bodies",
        "subtopic": "UPSC, SPSC and JPSC"
    },
    "Indian Polity (UNIT 4) > Constitutional Bodies > National Commissions SC/ ST/ Backward classes": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Constitutional Bodies",
        "subtopic": "National Commissions SC/ ST/ Backward classes"
    },
    "Indian Polity (UNIT 4) > Constitutional Bodies > Comptroller and Auditor General of India": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Constitutional Bodies",
        "subtopic": "Comptroller and Auditor General of India"
    },
    "Indian Polity (UNIT 4) > Constitutional Bodies > Attorney General": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Constitutional Bodies",
        "subtopic": "Attorney General"
    },
    "Indian Polity (UNIT 4) > Constitutional Bodies > Advocate general": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Constitutional Bodies",
        "subtopic": "Advocate general"
    },
    "Indian Polity (UNIT 4) > Constitutional Bodies > Solicitor general": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Constitutional Bodies",
        "subtopic": "Solicitor general"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > National human rights commission & State human rights commission": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "National human rights commission & State human rights commission"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Central information commission & State information commission": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Central information commission & State information commission"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Central vigilance commission": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Central vigilance commission"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Lokpal and Lokayukta": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Lokpal and Lokayukta"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > National law commission": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "National law commission"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > National green tribunal": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "National green tribunal"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Food safety and standard authority of India": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Food safety and standard authority of India"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Bureau of Indian standards": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Bureau of Indian standards"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Competition commission of India": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Competition commission of India"
    },
    "Indian Polity (UNIT 4) > Non-Constitutional Bodies > Non - Statutory Bodies": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Non-Constitutional Bodies",
        "subtopic": "Non - Statutory Bodies"
    },
    "Indian Polity (UNIT 4) > Empowerment of Women > Women Empowerment Schemes in India": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Empowerment of Women",
        "subtopic": "Women Empowerment Schemes in India"
    },
    "Indian Polity (UNIT 4) > Empowerment of Women > Constitutional Provisions": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Empowerment of Women",
        "subtopic": "Constitutional Provisions"
    },
    "Indian Polity (UNIT 4) > Empowerment of Women > Important Acts": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Empowerment of Women",
        "subtopic": "Important Acts"
    },
    "Indian Polity (UNIT 4) > Consumer Protection Forums > Consumer Protection Act 2019": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Consumer Protection Forums",
        "subtopic": "Consumer Protection Act 2019"
    },
    "Indian Polity (UNIT 4) > Political parties and political system in India > Recognised parties": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Political parties and political system in India",
        "subtopic": "Recognised parties"
    },
    "Indian Polity (UNIT 4) > Political parties and political system in India > non - recognised parties": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Political parties and political system in India",
        "subtopic": "non - recognised parties"
    },
    "Indian Polity (UNIT 4) > Election > Representation of people act 1950 & 1951": {
        "subject": "Indian Polity (UNIT 4)",
        "topic": "Election",
        "subtopic": "Representation of people act 1950 & 1951"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Microeconomics vs Macroeconomics": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Basics of Economy",
        "subtopic": "Microeconomics vs Macroeconomics"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Sectors of Economy-Primary, Secondary and Tertiary Sector": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Basics of Economy",
        "subtopic": "Sectors of Economy-Primary, Secondary and Tertiary Sector"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Factors of Production": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Basics of Economy",
        "subtopic": "Factors of Production"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Type of Economic System": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Basics of Economy",
        "subtopic": "Type of Economic System"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Basics of Economy > Growth and Development": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Basics of Economy",
        "subtopic": "Growth and Development"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Nature of Indian Economy > Strengths of Indian Economy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Nature of Indian Economy",
        "subtopic": "Strengths of Indian Economy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Nature of Indian Economy > Weakness of Indian Economy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Nature of Indian Economy",
        "subtopic": "Weakness of Indian Economy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Nature of Indian Economy > Natural Resources": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Nature of Indian Economy",
        "subtopic": "Natural Resources"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Economic Planning in India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Five-year plan",
        "subtopic": "Economic Planning in India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Planning Commission of India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Five-year plan",
        "subtopic": "Planning Commission of India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > National Development Council (NDC)s": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Five-year plan",
        "subtopic": "National Development Council (NDC)s"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Five Year Plan": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Five-year plan",
        "subtopic": "Five Year Plan"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Five-year plan > Niti Aayog": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Five-year plan",
        "subtopic": "Niti Aayog"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > National Income > Basic concepts of national income": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "National Income",
        "subtopic": "Basic concepts of national income"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > National Income > Money": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "National Income",
        "subtopic": "Money"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > National Income > Money, Demand and Supply": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "National Income",
        "subtopic": "Money, Demand and Supply"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Expansionary Vs. Contractionary": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Monetary Policy",
        "subtopic": "Expansionary Vs. Contractionary"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Objectives of Monetary Policy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Monetary Policy",
        "subtopic": "Objectives of Monetary Policy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Composition of the MPC": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Monetary Policy",
        "subtopic": "Composition of the MPC"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Methods of Credit Control": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Monetary Policy",
        "subtopic": "Methods of Credit Control"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Inflation": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Monetary Policy",
        "subtopic": "Inflation"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Meaning of Deflation, Disinflation and Stagflation": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Monetary Policy",
        "subtopic": "Meaning of Deflation, Disinflation and Stagflation"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Monetary Policy > Measurement of Inflation": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Monetary Policy",
        "subtopic": "Measurement of Inflation"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Reserve Bank of India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Banking",
        "subtopic": "Reserve Bank of India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Scheduled and Non Scheduled Banks": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Banking",
        "subtopic": "Scheduled and Non Scheduled Banks"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Non-Banking Financial Companies(NBFC)": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Banking",
        "subtopic": "Non-Banking Financial Companies(NBFC)"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > All India Financial Institutions (AIFI)- Non Banks": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Banking",
        "subtopic": "All India Financial Institutions (AIFI)- Non Banks"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Banking > Issue of Banking Sector": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Banking",
        "subtopic": "Issue of Banking Sector"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Meaning of Public Finance": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Fiscal Policy",
        "subtopic": "Meaning of Public Finance"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Budgetary Deficits": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Fiscal Policy",
        "subtopic": "Budgetary Deficits"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Bodies related to Budgeting": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Fiscal Policy",
        "subtopic": "Bodies related to Budgeting"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Basics of Budget": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Fiscal Policy",
        "subtopic": "Basics of Budget"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Components of Budget": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Fiscal Policy",
        "subtopic": "Components of Budget"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Fiscal Policy > Types of Budget": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Fiscal Policy",
        "subtopic": "Types of Budget"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > Direct Taxes": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Taxation",
        "subtopic": "Direct Taxes"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > Indirect Taxes": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Taxation",
        "subtopic": "Indirect Taxes"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > GST": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Taxation",
        "subtopic": "GST"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Taxation > Miscellaneous": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Taxation",
        "subtopic": "Miscellaneous"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > The sources of income as prescribed by the Constitution of India for the Central Government": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Resource sharing between Union and State Governments",
        "subtopic": "The sources of income as prescribed by the Constitution of India for the Central Government"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > Earnings of state government": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Resource sharing between Union and State Governments",
        "subtopic": "Earnings of state government"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > TAXES LEVIED AND COLLECTED BY THE UNION BUT ASSIGNED TO THE STATES": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Resource sharing between Union and State Governments",
        "subtopic": "TAXES LEVIED AND COLLECTED BY THE UNION BUT ASSIGNED TO THE STATES"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > DUTIES LEVIED BY THE UNION BUT COLLECTED AND APPROPRIATED BY THE STATES": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Resource sharing between Union and State Governments",
        "subtopic": "DUTIES LEVIED BY THE UNION BUT COLLECTED AND APPROPRIATED BY THE STATES"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > Taxes which are Levied and Collected by the Union but which may be Distributed between the Union and the States": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Resource sharing between Union and State Governments",
        "subtopic": "Taxes which are Levied and Collected by the Union but which may be Distributed between the Union and the States"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Resource sharing between Union and State Governments > Finance Commission": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Resource sharing between Union and State Governments",
        "subtopic": "Finance Commission"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Structure of Indian Economy and Employment Generation > Main Sectors in India’s Economy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Structure of Indian Economy and Employment Generation",
        "subtopic": "Main Sectors in India’s Economy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Structure of Indian Economy and Employment Generation > Other Sectors in India’s Economy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Structure of Indian Economy and Employment Generation",
        "subtopic": "Other Sectors in India’s Economy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Structure of Indian Economy and Employment Generation > Initiatives for Employment Generation": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Structure of Indian Economy and Employment Generation",
        "subtopic": "Initiatives for Employment Generation"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Role of Agriculture in Indian Economy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Role of Agriculture in Indian Economy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Application of Science and Technology in Agriculture": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Application of Science and Technology in Agriculture"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Land Reforms": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Land Reforms"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > ¨ Cropping Pattern in India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "¨ Cropping Pattern in India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > ¨ Types of crops in India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "¨ Types of crops in India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Major Producer of the Crops in India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Major Producer of the Crops in India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Cropping Seasons in India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Cropping Seasons in India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Green Revolution": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Green Revolution"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Agriculture Related Schemes": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Agriculture Related Schemes"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Irrigation": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Irrigation"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > PDS": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "PDS"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Minimum support prices (MSP), Procurement prices, Issue Price, Retail prices": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Minimum support prices (MSP), Procurement prices, Issue Price, Retail prices"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Land Reforms and Agriculture > Rural Welfare Oriented Programmes": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Land Reforms and Agriculture",
        "subtopic": "Rural Welfare Oriented Programmes"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Types of Industries": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Industrial growth",
        "subtopic": "Types of Industries"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Core Industries in India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Industrial growth",
        "subtopic": "Core Industries in India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > State-wise Distribution of Industries": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Industrial growth",
        "subtopic": "State-wise Distribution of Industries"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Industrial Policies": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Industrial growth",
        "subtopic": "Industrial Policies"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Industrial growth > Public Sector Enterprises": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Industrial growth",
        "subtopic": "Public Sector Enterprises"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Population": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Problems",
        "subtopic": "Population"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Education": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Problems",
        "subtopic": "Education"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Health": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Problems",
        "subtopic": "Health"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Employment": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Problems",
        "subtopic": "Employment"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Problems > Poverty": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Problems",
        "subtopic": "Poverty"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > Three indicators": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Human Development Index",
        "subtopic": "Three indicators"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > Human Development Report": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Human Development Index",
        "subtopic": "Human Development Report"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > 5 Indices of Human Development Report": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Human Development Index",
        "subtopic": "5 Indices of Human Development Report"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Human Development Index > Important Human Development Indicators of Tamil Nadu": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Human Development Index",
        "subtopic": "Important Human Development Indicators of Tamil Nadu"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Reform Movements in Tamil Nadu > Social Reformers of Tamilnadu": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Reform Movements in Tamil Nadu",
        "subtopic": "Social Reformers of Tamilnadu"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Political Parties": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Political parties and Welfare schemes",
        "subtopic": "Political Parties"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Recognized Tamil Nadu State Parties": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Political parties and Welfare schemes",
        "subtopic": "Recognized Tamil Nadu State Parties"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Achievements of the Parties": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Political parties and Welfare schemes",
        "subtopic": "Achievements of the Parties"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Political parties and Welfare schemes > Social Welfare Schemes by Tamil Nadu": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Political parties and Welfare schemes",
        "subtopic": "Social Welfare Schemes by Tamil Nadu"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Reservation Policy > Reservation Policy in Tamilnadu": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Reservation Policy",
        "subtopic": "Reservation Policy in Tamilnadu"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Reservation Policy > Reservation Policy in India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Reservation Policy",
        "subtopic": "Reservation Policy in India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Social Justice Theories": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Justice and Social Harmony",
        "subtopic": "Social Justice Theories"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Constitutional Provisions of social Justice": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Justice and Social Harmony",
        "subtopic": "Constitutional Provisions of social Justice"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Justice Party Contribution": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Justice and Social Harmony",
        "subtopic": "Justice Party Contribution"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Welfare and empowerment of SCs, STs, differently abled, women, transgender, aged and senior citizens, child rights": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Justice and Social Harmony",
        "subtopic": "Welfare and empowerment of SCs, STs, differently abled, women, transgender, aged and senior citizens, child rights"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Social Justice and Social Harmony > Various Commissions": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Social Justice and Social Harmony",
        "subtopic": "Various Commissions"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > Highlights of Tamil Nadu Economy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "Highlights of Tamil Nadu Economy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > GI Tags": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "GI Tags"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > Economic Policies": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "Economic Policies"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Economic Trends in Tamil Nadu > Budget Highlights": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Economic Trends in Tamil Nadu",
        "subtopic": "Budget Highlights"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Tamil Nadu Educational System": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Tamil Nadu Educational System"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Literacy in Tamil Nadu": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Literacy in Tamil Nadu"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Education & Health Related Constitutional Provisions, Acts, Government Schemes": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Education & Health Related Constitutional Provisions, Acts, Government Schemes"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Education Policy - Tamil Nadu and India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Education Policy - Tamil Nadu and India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Policy - Tamil Nadu and India": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Policy - Tamil Nadu and India"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Systems in Tamil Nadu": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Systems in Tamil Nadu"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Indicators": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Indicators"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Education and Health Systems in Tamil Nadu > Health Care Institutions in TN - Primary, Secondary and Tertiary": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Education and Health Systems in Tamil Nadu",
        "subtopic": "Health Care Institutions in TN - Primary, Secondary and Tertiary"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Physiographic Divisions": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Physiographic Divisions"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Land Area Extent": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Land Area Extent"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Climate": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Climate"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Soils": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Soils"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Natural Vegetation": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Natural Vegetation"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Agriculture": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Agriculture"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Livestock": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Livestock"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > water sources": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "water sources"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Mineral resources": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Mineral resources"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Industries": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Industries"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Transport and communication": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Transport and communication"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Geography of Tamil Nadu > Demography": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Geography of Tamil Nadu",
        "subtopic": "Demography"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > Institutional frameworks for e-governance": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "Institutional frameworks for e-governance"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > Core Infrastructure of Information Technology": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "Core Infrastructure of Information Technology"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > e-Governance programs": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "e-Governance programs"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Tamil Nadu e-Governance > e-governance policy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Tamil Nadu e-Governance",
        "subtopic": "e-governance policy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > Achievements and Awards": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "Achievements and Awards"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > E-Governance Initiatives in Tamilnadu": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "E-Governance Initiatives in Tamilnadu"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > Performance of Tamil Nadu Economy": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "Performance of Tamil Nadu Economy"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Achievements of Tamil Nadu in Various Fields > Tamil Nadu related recent Survey, data, Indices, Ranking, Reports, etc": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Achievements of Tamil Nadu in Various Fields",
        "subtopic": "Tamil Nadu related recent Survey, data, Indices, Ranking, Reports, etc"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Public awareness and General administration > Public awareness and General administration": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Public awareness and General administration",
        "subtopic": "Public awareness and General administration"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Current socio-economic issues > Current socio-economic issues": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Current socio-economic issues",
        "subtopic": "Current socio-economic issues"
    },
    "Indian Economy and Development Administration in Tamil Nadu (UNIT 5) > Welfare oriented Government schemes and their utility > Welfare oriented Government schemes and their utility": {
        "subject": "Indian Economy and Development Administration in Tamil Nadu (UNIT 5)",
        "topic": "Welfare oriented Government schemes and their utility",
        "subtopic": "Welfare oriented Government schemes and their utility"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > IVC > Phases of IVC": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "IVC",
        "subtopic": "Phases of IVC"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > IVC > Lifestyle of people during IVC": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "IVC",
        "subtopic": "Lifestyle of people during IVC"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > IVC > Findings, sites , economic activities": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "IVC",
        "subtopic": "Findings, sites , economic activities"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > ¨ Sources of Gupta Rule": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Gupta Period",
        "subtopic": "¨ Sources of Gupta Rule"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Important rulers and titles adopted by Gupta kings": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Gupta Period",
        "subtopic": "Important rulers and titles adopted by Gupta kings"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Foreign Travellers Visit - Fahien’s Visit": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Gupta Period",
        "subtopic": "Foreign Travellers Visit - Fahien’s Visit"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Life under Gupta’s": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Gupta Period",
        "subtopic": "Life under Gupta’s"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Gupta Period > Post Guptas": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Gupta Period",
        "subtopic": "Post Guptas"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Delhi Sultanate > EARLY MUSLIM INVASIONS": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Delhi Sultanate",
        "subtopic": "EARLY MUSLIM INVASIONS"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Delhi Sultanate > Major Dynasties and their rulers": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Delhi Sultanate",
        "subtopic": "Major Dynasties and their rulers"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Delhi Sultanate > Life under Delhi Sultanate": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Delhi Sultanate",
        "subtopic": "Life under Delhi Sultanate"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Establishment of Mughal Empire": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Mughals",
        "subtopic": "Establishment of Mughal Empire"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Akbar": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Mughals",
        "subtopic": "Akbar"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Jahangir and Shah Jahan": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Mughals",
        "subtopic": "Jahangir and Shah Jahan"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Aurangzeb": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Mughals",
        "subtopic": "Aurangzeb"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Life under Mughals": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Mughals",
        "subtopic": "Life under Mughals"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Mughals > Mughals Contribution": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Mughals",
        "subtopic": "Mughals Contribution"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Rise of Marathas under Shivaji": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Rise of Marathas under Shivaji"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Treaty of Purander": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Treaty of Purander"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Sambhaji": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Sambhaji"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Rajaram": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Rajaram"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Shahu": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Shahu"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Peshwas under Maratha empire": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Peshwas under Maratha empire"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Mughals and Marathas conflicts": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Mughals and Marathas conflicts"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > ANGLO-MARATHA WARS": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "ANGLO-MARATHA WARS"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Marathas > Decline of Marathas": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Marathas",
        "subtopic": "Decline of Marathas"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Dynasties": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Vijaynagar empire",
        "subtopic": "Dynasties"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Administration": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Vijaynagar empire",
        "subtopic": "Administration"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Army and military organisation": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Vijaynagar empire",
        "subtopic": "Army and military organisation"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Social and economic life": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Vijaynagar empire",
        "subtopic": "Social and economic life"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Vijaynagar empire > Social life": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Vijaynagar empire",
        "subtopic": "Social life"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Rulers of the Bahmani Kingdom": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Rulers of the Bahmani Kingdom"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > The Five Kingdoms": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "The Bahmani Kingdom",
        "subtopic": "The Five Kingdoms"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Administration": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Administration"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Contribution to Education": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Contribution to Education"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Art and Architecture": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Art and Architecture"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > The Bahmani Kingdom > Decline of Bahmani Kingdom": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "The Bahmani Kingdom",
        "subtopic": "Decline of Bahmani Kingdom"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Sangam Age": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Sangam Age"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Life under Sangam Age": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Life under Sangam Age"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Kalabras": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Kalabras"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Pallavas dynasty": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Pallavas dynasty"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Chalukya dynasty": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Chalukya dynasty"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Rashtrakutas dynasty": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Rashtrakutas dynasty"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Later Pandyas": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Later Pandyas"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > South Indian History > Later Cholas": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "South Indian History",
        "subtopic": "Later Cholas"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Religious development in Medieval India > Sufism": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Religious development in Medieval India",
        "subtopic": "Sufism"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Religious development in Medieval India > Bhaktism": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Religious development in Medieval India",
        "subtopic": "Bhaktism"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Religious development in Medieval India > Sikhism": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Religious development in Medieval India",
        "subtopic": "Sikhism"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > Art and Culture": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Cultural History of India",
        "subtopic": "Art and Culture"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > Characteristics of Indian Culture": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Cultural History of India",
        "subtopic": "Characteristics of Indian Culture"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > India as a Secular State": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Cultural History of India",
        "subtopic": "India as a Secular State"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Cultural History of India > Social Harmony": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Cultural History of India",
        "subtopic": "Social Harmony"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Vedic Age": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Additional Topics",
        "subtopic": "Vedic Age"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Pre Mauryan Age": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Additional Topics",
        "subtopic": "Pre Mauryan Age"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Mauryan Age": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Additional Topics",
        "subtopic": "Mauryan Age"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Post Mauryan Age": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Additional Topics",
        "subtopic": "Post Mauryan Age"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Additional Topics > Foreign successors of Mauryas": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Additional Topics",
        "subtopic": "Foreign successors of Mauryas"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The Portuguese in India": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "The Portuguese in India"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The Dutch in India": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "The Dutch in India"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The Danes in India": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "The Danes in India"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The English": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "The English"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > The French": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "The French"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > Carnatic Wars": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "Carnatic Wars"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > BRITISH EXPANSION IN INDIA": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "BRITISH EXPANSION IN INDIA"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > ECONOMIC POLICIES OF BRITISH": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "ECONOMIC POLICIES OF BRITISH"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Advent of Europeans in India > IMPACT OF BRITISH ADMINISTRATION": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Advent of Europeans in India",
        "subtopic": "IMPACT OF BRITISH ADMINISTRATION"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Early uprising against British rule > Tribal Movements": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Early uprising against British rule",
        "subtopic": "Tribal Movements"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Early uprising against British rule > Peasant Movements": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Early uprising against British rule",
        "subtopic": "Peasant Movements"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Early uprising against British rule > Politico- religious movements": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Early uprising against British rule",
        "subtopic": "Politico- religious movements"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Causes of the Revolt": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "THE REVOLT OF 1857",
        "subtopic": "Causes of the Revolt"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Centres and Spread of the Revolt": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "THE REVOLT OF 1857",
        "subtopic": "Centres and Spread of the Revolt"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Leaders of the Revolt": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "THE REVOLT OF 1857",
        "subtopic": "Leaders of the Revolt"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Causes of Failure of the Revolt": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "THE REVOLT OF 1857",
        "subtopic": "Causes of Failure of the Revolt"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > THE REVOLT OF 1857 > Nature and Impact of the Revolt": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "THE REVOLT OF 1857",
        "subtopic": "Nature and Impact of the Revolt"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > SOCIO-RELIGIOUS REFORMS": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "SOCIO-RELIGIOUS REFORMS"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > Muslim reform movements": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "Muslim reform movements"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > Miscellaneous movements": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "Miscellaneous movements"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > National Renaissance Social and religious reform movements > PERSONALITIES": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "National Renaissance Social and religious reform movements",
        "subtopic": "PERSONALITIES"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Early Phase Indian National Congress": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Early Phase Indian National Congress"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > The Moderate Congress (1885-1905)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "The Moderate Congress (1885-1905)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Political associations in Bengal, Bombay and Madras GoI Act 1861 and 1892": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Political associations in Bengal, Bombay and Madras GoI Act 1861 and 1892"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > The Extremist (1905-1920)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "The Extremist (1905-1920)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Differences between the Moderates and the Extremists": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Differences between the Moderates and the Extremists"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Indian National Congress (1885 - 1920) > Pre congress campaign": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Indian National Congress (1885 - 1920)",
        "subtopic": "Pre congress campaign"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Partition of Bengal (1905)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "Partition of Bengal (1905)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Swadeshi Movement": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "Swadeshi Movement"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Muslim League, 1906": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "Muslim League, 1906"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Surat Session of INC, 1907": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "Surat Session of INC, 1907"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Indian Council Act (Morley-Minto Act) 1909": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "Indian Council Act (Morley-Minto Act) 1909"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Ghadar Party, 1913": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "Ghadar Party, 1913"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > Komagata Maru Incident 1914": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "Komagata Maru Incident 1914"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > First world war and its impact": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "First world war and its impact"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - I (1905-1918) > The Lucknow Pact (1916)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - I (1905-1918)",
        "subtopic": "The Lucknow Pact (1916)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Emergence of Gandhi": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Emergence of Gandhi"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > The Government of India Act, 1919": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "The Government of India Act, 1919"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Rowlatt Act and Jallianwala Bagh Massacre (1919)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Rowlatt Act and Jallianwala Bagh Massacre (1919)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Khilafat Movement": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Khilafat Movement"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > The Non-Cooperation Movement (1920-22)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "The Non-Cooperation Movement (1920-22)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Swarajists and no changers": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Swarajists and no changers"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Nagpur Session of Congress": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Nagpur Session of Congress"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Swaraj Party and its Evaluation": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Swaraj Party and its Evaluation"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Muddiman Committee (1924)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Muddiman Committee (1924)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Simon Commission (1927)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Simon Commission (1927)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Bardoli Satyagraha (1928)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Bardoli Satyagraha (1928)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Nehru Report (1928)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Nehru Report (1928)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Jinnah’s Fourteen Points": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Jinnah’s Fourteen Points"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Calcutta session of INC 1928": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Calcutta session of INC 1928"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Delhi Manifesto": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Delhi Manifesto"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Lahore Session, 1929": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Lahore Session, 1929"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Allahabad Address (1930)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Allahabad Address (1930)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT -II (1918-1929) > Emergence of New Forces during 1920s": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT -II (1918-1929)",
        "subtopic": "Emergence of New Forces during 1920s"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Civil Disobedience Movement (1930-1931)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Civil Disobedience Movement (1930-1931)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Round Table ConferencE": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Round Table ConferencE"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Gandhi-Irwin Pact, 1931": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Gandhi-Irwin Pact, 1931"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Karachi session of 1931": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Karachi session of 1931"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Communal Award": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Communal Award"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Poona Pact, 1932": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Poona Pact, 1932"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Government of India Act, 1935": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Government of India Act, 1935"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > World War II and Indian Nationalism": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "World War II and Indian Nationalism"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Resignation of Congress Ministers (1939)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Resignation of Congress Ministers (1939)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Poona Resolution and Conditional Support to Britain (1941)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Poona Resolution and Conditional Support to Britain (1941)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > August Offer of 1940": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "August Offer of 1940"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > The Individual Civil Disobedience": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "The Individual Civil Disobedience"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Two-Nation Theory": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Two-Nation Theory"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Demand for Pakistan (1942)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Demand for Pakistan (1942)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Cripps Mission (1942)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Cripps Mission (1942)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Quit India Movement": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Quit India Movement"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Azad Hind Fauj": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Azad Hind Fauj"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Indian National Army": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Indian National Army"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > N.A. Trials": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "N.A. Trials"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > I.N. Rebellion": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "I.N. Rebellion"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Rajagopalachari Formula, 1945": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Rajagopalachari Formula, 1945"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Desai - Liaqat Pact": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Desai - Liaqat Pact"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Cabinet Mission (1946)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Cabinet Mission (1946)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Wavell Plan": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Wavell Plan"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Jinnah’s Direct Action Resolution": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Jinnah’s Direct Action Resolution"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Mountbatten Plan of June 1947": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Mountbatten Plan of June 1947"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Indian Independence Act 1947": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Indian Independence Act 1947"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > INDIAN NATIONAL MOVEMENT - III (1930-1947) > Communalism and Partition": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "INDIAN NATIONAL MOVEMENT - III (1930-1947)",
        "subtopic": "Communalism and Partition"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > B.R. Ambedkar": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "B.R. Ambedkar"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Bhagat Singh": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Bhagat Singh"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Bharathiar": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Bharathiar"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > V.O. Chidambaranar": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "V.O. Chidambaranar"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Jawaharlal Nehru": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Jawaharlal Nehru"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Kamarajar": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Kamarajar"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Mahatma Gandhi": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Mahatma Gandhi"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Maulana Abul Kalam Azad": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Maulana Abul Kalam Azad"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Thanthai Periyar": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Thanthai Periyar"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Rajaji": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Rajaji"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Subash Chandra Bose": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Subash Chandra Bose"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Rabindranath Tagore": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Rabindranath Tagore"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Emergence of leaders > Others": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Emergence of leaders",
        "subtopic": "Others"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Governor of Bengal (Before 1773)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "GOVERNOR GENERALS DURING BRITISH INDIA",
        "subtopic": "Governor of Bengal (Before 1773)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Governor Generals of Bengal (1773-1833)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "GOVERNOR GENERALS DURING BRITISH INDIA",
        "subtopic": "Governor Generals of Bengal (1773-1833)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Governor Generals of India (1832-1858)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "GOVERNOR GENERALS DURING BRITISH INDIA",
        "subtopic": "Governor Generals of India (1832-1858)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > GOVERNOR GENERALS DURING BRITISH INDIA > Viceroy of India (1858-1947)": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "GOVERNOR GENERALS DURING BRITISH INDIA",
        "subtopic": "Viceroy of India (1858-1947)"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Constitutional Development in India": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Miscellaneous",
        "subtopic": "Constitutional Development in India"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Development of Civil Services": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Miscellaneous",
        "subtopic": "Development of Civil Services"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Development of Education": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Miscellaneous",
        "subtopic": "Development of Education"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Miscellaneous > Development of Press": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Miscellaneous",
        "subtopic": "Development of Press"
    },
    "History, Culture of India, and Indian National Movement (UNIT 3) > Prominent personalities in various spheres > - Arts, Science, Literature and Philosophy": {
        "subject": "History, Culture of India, and Indian National Movement (UNIT 3)",
        "topic": "Prominent personalities in various spheres",
        "subtopic": "- Arts, Science, Literature and Philosophy"
    },
    "General Science (Unit 1) > Physics > Nature of Universe": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Nature of Universe"
    },
    "General Science (Unit 1) > Physics > General Scientific laws": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "General Scientific laws"
    },
    "General Science (Unit 1) > Physics > Force, Motion and Energy": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Force, Motion and Energy"
    },
    "General Science (Unit 1) > Physics > Light": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Light"
    },
    "General Science (Unit 1) > Physics > Sound": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Sound"
    },
    "General Science (Unit 1) > Physics > Heat": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Heat"
    },
    "General Science (Unit 1) > Physics > Electricity and Magnetism": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Electricity and Magnetism"
    },
    "General Science (Unit 1) > Physics > Nuclear Physics": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Nuclear Physics"
    },
    "General Science (Unit 1) > Physics > Laser, Electronics and Communications": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Laser, Electronics and Communications"
    },
    "General Science (Unit 1) > Physics > Properties of matter": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Properties of matter"
    },
    "General Science (Unit 1) > Physics > Everyday application of the basic principles of mechanics": {
        "subject": "General Science (Unit 1)",
        "topic": "Physics",
        "subtopic": "Everyday application of the basic principles of mechanics"
    },
    "General Science (Unit 1) > Scientific knowledge and scientific temper > Scientific knowledge and scientific temper": {
        "subject": "General Science (Unit 1)",
        "topic": "Scientific knowledge and scientific temper",
        "subtopic": "Scientific knowledge and scientific temper"
    },
    "General Science (Unit 1) > Power of reasoning > Power of reasoning": {
        "subject": "General Science (Unit 1)",
        "topic": "Power of reasoning",
        "subtopic": "Power of reasoning"
    },
    "General Science (Unit 1) > Rote learning vs conceptual learning > Rote learning vs conceptual learning": {
        "subject": "General Science (Unit 1)",
        "topic": "Rote learning vs conceptual learning",
        "subtopic": "Rote learning vs conceptual learning"
    },
    "General Science (Unit 1) > Science as a tool to understand the past, present, and future > Science as a tool to understand the past, present, and future": {
        "subject": "General Science (Unit 1)",
        "topic": "Science as a tool to understand the past, present, and future",
        "subtopic": "Science as a tool to understand the past, present, and future"
    },
    "General Science (Unit 1) > Chemistry > Elements and Compounds": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Elements and Compounds"
    },
    "General Science (Unit 1) > Chemistry > Acids, Bases, Salts": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Acids, Bases, Salts"
    },
    "General Science (Unit 1) > Chemistry > Petroleum Products": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Petroleum Products"
    },
    "General Science (Unit 1) > Chemistry > fertilizers, pesticides": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "fertilizers, pesticides"
    },
    "General Science (Unit 1) > Chemistry > Main concepts of Life Science": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Main concepts of Life Science"
    },
    "General Science (Unit 1) > Chemistry > Classification of Living Organisms": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Classification of Living Organisms"
    },
    "General Science (Unit 1) > Chemistry > Evolution, Genetics": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Evolution, Genetics"
    },
    "General Science (Unit 1) > Chemistry > Physiology": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Physiology"
    },
    "General Science (Unit 1) > Chemistry > Nutrition": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Nutrition"
    },
    "General Science (Unit 1) > Chemistry > Health and Hygiene": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Health and Hygiene"
    },
    "General Science (Unit 1) > Chemistry > Human Diseases": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Human Diseases"
    },
    "General Science (Unit 1) > Chemistry > Environment and ecology": {
        "subject": "General Science (Unit 1)",
        "topic": "Chemistry",
        "subtopic": "Environment and ecology"
    },
    "General Science (Unit 1) > Latest inventions in science and technology > Latest inventions in science and technology": {
        "subject": "General Science (Unit 1)",
        "topic": "Latest inventions in science and technology",
        "subtopic": "Latest inventions in science and technology"
    },
    "Geography of India (Unit 2) > Location and physiography of India > India: An Introduction": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Location and physiography of India",
        "subtopic": "India: An Introduction"
    },
    "Geography of India (Unit 2) > Location and physiography of India > The Himalayas": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Location and physiography of India",
        "subtopic": "The Himalayas"
    },
    "Geography of India (Unit 2) > Location and physiography of India > Indo Gangetic plain": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Location and physiography of India",
        "subtopic": "Indo Gangetic plain"
    },
    "Geography of India (Unit 2) > Location and physiography of India > Peninsular plateau": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Location and physiography of India",
        "subtopic": "Peninsular plateau"
    },
    "Geography of India (Unit 2) > Location and physiography of India > Thar desert": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Location and physiography of India",
        "subtopic": "Thar desert"
    },
    "Geography of India (Unit 2) > Location and physiography of India > Coastal plains": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Location and physiography of India",
        "subtopic": "Coastal plains"
    },
    "Geography of India (Unit 2) > Location and physiography of India > The islands": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Location and physiography of India",
        "subtopic": "The islands"
    },
    "Geography of India (Unit 2) > Drainage system > Himalayan Rivers": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Drainage system",
        "subtopic": "Himalayan Rivers"
    },
    "Geography of India (Unit 2) > Drainage system > Peninsular Rivers": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Drainage system",
        "subtopic": "Peninsular Rivers"
    },
    "Geography of India (Unit 2) > Drainage system > Lakes- types and lakes in India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Drainage system",
        "subtopic": "Lakes- types and lakes in India"
    },
    "Geography of India (Unit 2) > Drainage system > Dams and waterfals": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Drainage system",
        "subtopic": "Dams and waterfals"
    },
    "Geography of India (Unit 2) > Climate of India > Composition of the Atmosphere": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate of India",
        "subtopic": "Composition of the Atmosphere"
    },
    "Geography of India (Unit 2) > Climate of India > Layers of the Atmosphere": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate of India",
        "subtopic": "Layers of the Atmosphere"
    },
    "Geography of India (Unit 2) > Climate of India > Heat Zones of the World": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate of India",
        "subtopic": "Heat Zones of the World"
    },
    "Geography of India (Unit 2) > Climate of India > The factors affecting the climate": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate of India",
        "subtopic": "The factors affecting the climate"
    },
    "Geography of India (Unit 2) > Climate of India > Indian Monsoon": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate of India",
        "subtopic": "Indian Monsoon"
    },
    "Geography of India (Unit 2) > Natural Vegetation > Classification of forest": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural Vegetation",
        "subtopic": "Classification of forest"
    },
    "Geography of India (Unit 2) > Natural Vegetation > Indian State of Forest Report": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural Vegetation",
        "subtopic": "Indian State of Forest Report"
    },
    "Geography of India (Unit 2) > Natural Vegetation > Biodiversity hotspots in India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural Vegetation",
        "subtopic": "Biodiversity hotspots in India"
    },
    "Geography of India (Unit 2) > Natural Vegetation > Major Threats to Biodiversity": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural Vegetation",
        "subtopic": "Major Threats to Biodiversity"
    },
    "Geography of India (Unit 2) > Natural Vegetation > The Protected Areas of India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural Vegetation",
        "subtopic": "The Protected Areas of India"
    },
    "Geography of India (Unit 2) > Natural Vegetation > Specialised projects in India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural Vegetation",
        "subtopic": "Specialised projects in India"
    },
    "Geography of India (Unit 2) > Agricultural and Soils > Soils of India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Agricultural and Soils",
        "subtopic": "Soils of India"
    },
    "Geography of India (Unit 2) > Agricultural and Soils > Irrigation": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Agricultural and Soils",
        "subtopic": "Irrigation"
    },
    "Geography of India (Unit 2) > Agricultural and Soils > Agriculture IN INDIA": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Agricultural and Soils",
        "subtopic": "Agriculture IN INDIA"
    },
    "Geography of India (Unit 2) > Agricultural and Soils > Livestock & Fisheries": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Agricultural and Soils",
        "subtopic": "Livestock & Fisheries"
    },
    "Geography of India (Unit 2) > Minerals and Natural Resources > Classification of Resources": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Minerals and Natural Resources",
        "subtopic": "Classification of Resources"
    },
    "Geography of India (Unit 2) > Minerals and Natural Resources > Types of minerals": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Minerals and Natural Resources",
        "subtopic": "Types of minerals"
    },
    "Geography of India (Unit 2) > Minerals and Natural Resources > Industries": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Minerals and Natural Resources",
        "subtopic": "Industries"
    },
    "Geography of India (Unit 2) > Transport - Communication > Road transport": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Transport - Communication",
        "subtopic": "Road transport"
    },
    "Geography of India (Unit 2) > Transport - Communication > Railways": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Transport - Communication",
        "subtopic": "Railways"
    },
    "Geography of India (Unit 2) > Transport - Communication > Water transport, ports": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Transport - Communication",
        "subtopic": "Water transport, ports"
    },
    "Geography of India (Unit 2) > Transport - Communication > Air transport": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Transport - Communication",
        "subtopic": "Air transport"
    },
    "Geography of India (Unit 2) > Transport - Communication > International trade routes": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Transport - Communication",
        "subtopic": "International trade routes"
    },
    "Geography of India (Unit 2) > Transport - Communication > Communication": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Transport - Communication",
        "subtopic": "Communication"
    },
    "Geography of India (Unit 2) > Social Geography > Population density and distribution": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Social Geography",
        "subtopic": "Population density and distribution"
    },
    "Geography of India (Unit 2) > Social Geography > Urbanization": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Social Geography",
        "subtopic": "Urbanization"
    },
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Racial Groups": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Racial Groups"
    },
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Religion": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Religion"
    },
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Tribal Distribution in world": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Tribal Distribution in world"
    },
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Tribal in India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Tribal in India"
    },
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Tribals in Tamilnadu": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Tribals in Tamilnadu"
    },
    "Geography of India (Unit 2) > Racial, Linguistic Groups and Major Tribes > Language": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Racial, Linguistic Groups and Major Tribes",
        "subtopic": "Language"
    },
    "Geography of India (Unit 2) > Natural calamity - Disaster Management > Natural disasters": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural calamity - Disaster Management",
        "subtopic": "Natural disasters"
    },
    "Geography of India (Unit 2) > Natural calamity - Disaster Management > Man-made disasters": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural calamity - Disaster Management",
        "subtopic": "Man-made disasters"
    },
    "Geography of India (Unit 2) > Natural calamity - Disaster Management > National Disaster Management Authority": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Natural calamity - Disaster Management",
        "subtopic": "National Disaster Management Authority"
    },
    "Geography of India (Unit 2) > Environmental pollution > Pollution": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Environmental pollution",
        "subtopic": "Pollution"
    },
    "Geography of India (Unit 2) > Environmental pollution > Pollutants": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Environmental pollution",
        "subtopic": "Pollutants"
    },
    "Geography of India (Unit 2) > Environmental pollution > Classification of Pollutants": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Environmental pollution",
        "subtopic": "Classification of Pollutants"
    },
    "Geography of India (Unit 2) > Environmental pollution > Types of Pollution": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Environmental pollution",
        "subtopic": "Types of Pollution"
    },
    "Geography of India (Unit 2) > Environmental pollution > Government Initiatives to Combat Pollution": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Environmental pollution",
        "subtopic": "Government Initiatives to Combat Pollution"
    },
    "Geography of India (Unit 2) > Climate Change > Factors Affecting Climate Change": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate Change",
        "subtopic": "Factors Affecting Climate Change"
    },
    "Geography of India (Unit 2) > Climate Change > Evidence for Rapid Climate Change in India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate Change",
        "subtopic": "Evidence for Rapid Climate Change in India"
    },
    "Geography of India (Unit 2) > Climate Change > Effects of climate change in India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate Change",
        "subtopic": "Effects of climate change in India"
    },
    "Geography of India (Unit 2) > Climate Change > India’s response to Climate Change": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Climate Change",
        "subtopic": "India’s response to Climate Change"
    },
    "Geography of India (Unit 2) > Green energy > Solar Power, Wind Power, Hydropower, Geothermal Energy, Biomass, Biofuels": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Green energy",
        "subtopic": "Solar Power, Wind Power, Hydropower, Geothermal Energy, Biomass, Biofuels"
    },
    "Geography of India (Unit 2) > Green energy > Renewable Energy Potential States in India": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Green energy",
        "subtopic": "Renewable Energy Potential States in India"
    },
    "Geography of India (Unit 2) > Green energy > Achievements of India in the Renewable energy sector": {
        "subject": "Geography of India (Unit 2)",
        "topic": "Green energy",
        "subtopic": "Achievements of India in the Renewable energy sector"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > History of Tamil Society > தமிழர் தோற்றம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "History of Tamil Society",
        "subtopic": "தமிழர் தோற்றம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > History of Tamil Society > சங்க கால மூவேந்தர்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "History of Tamil Society",
        "subtopic": "சங்க கால மூவேந்தர்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > History of Tamil Society > சங்க கால தமிழ் நகரங்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "History of Tamil Society",
        "subtopic": "சங்க கால தமிழ் நகரங்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > archaeological discoveries > தமிழ்நாடு தொல்லியல் துறையால் அகழாய்வு செய்யப்பட்ட இடங்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "archaeological discoveries",
        "subtopic": "தமிழ்நாடு தொல்லியல் துறையால் அகழாய்வு செய்யப்பட்ட இடங்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > archaeological discoveries > தமிழ் அல்லாத பிற மொழிச் சான்றுகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "archaeological discoveries",
        "subtopic": "தமிழ் அல்லாத பிற மொழிச் சான்றுகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > archaeological discoveries > வெளிநாட்டினரின் குறிப்புகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "archaeological discoveries",
        "subtopic": "வெளிநாட்டினரின் குறிப்புகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > எட்டுத்தொகை": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Tamil literature",
        "subtopic": "எட்டுத்தொகை"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > பத்துப்பாட்டு": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Tamil literature",
        "subtopic": "பத்துப்பாட்டு"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > பதிணென் கீழ்கணக்கு நூல்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Tamil literature",
        "subtopic": "பதிணென் கீழ்கணக்கு நூல்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > ஐம்பெரும்காப்பியங்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Tamil literature",
        "subtopic": "ஐம்பெரும்காப்பியங்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > ஐஞ்சிறு காப்பியங்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Tamil literature",
        "subtopic": "ஐஞ்சிறு காப்பியங்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > தொடர்நிலைச்செய்யுள்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Tamil literature",
        "subtopic": "தொடர்நிலைச்செய்யுள்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Tamil literature > பக்தி இலக்கியம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Tamil literature",
        "subtopic": "பக்தி இலக்கியம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > மதச்சார்பற்ற தனித்தன்மையுள்ள இலக்கியம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Thirukkural",
        "subtopic": "மதச்சார்பற்ற தனித்தன்மையுள்ள இலக்கியம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > மானுடத்தின் மீதான திருக்குறளின் தாக்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Thirukkural",
        "subtopic": "மானுடத்தின் மீதான திருக்குறளின் தாக்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > அன்றாட வாழ்வியலோடு தொடர்புத் தன்மை": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Thirukkural",
        "subtopic": "அன்றாட வாழ்வியலோடு தொடர்புத் தன்மை"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > திருக்குறளும் மாறாத விழுமியங்களும் - மனிதநேயம், சமத்துவம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Thirukkural",
        "subtopic": "திருக்குறளும் மாறாத விழுமியங்களும் - மனிதநேயம், சமத்துவம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > திருக்குறளில் தத்துவக் கோட்பாடுகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Thirukkural",
        "subtopic": "திருக்குறளில் தத்துவக் கோட்பாடுகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Thirukkural > சமூக அரசியல் பொருளாதார நிகழ்வுகளில் திருக்குறளின்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Thirukkural",
        "subtopic": "சமூக அரசியல் பொருளாதார நிகழ்வுகளில் திருக்குறளின்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > தமிழ்நாட்டில் நாயக்கர் ஆட்சி": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "தமிழ்நாட்டில் நாயக்கர் ஆட்சி"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > புலித்தேவன்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "புலித்தேவன்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > வீரபாண்டிய கட்டபொம்மன்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "வீரபாண்டிய கட்டபொம்மன்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > மருது சகோதரர்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "மருது சகோதரர்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > தென்னிந்திய விடுதலைக்கூட்டமைப்பு": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "தென்னிந்திய விடுதலைக்கூட்டமைப்பு"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Early agitations aginst British Rule > வேலூர் கிளர்ச்சி": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Early agitations aginst British Rule",
        "subtopic": "வேலூர் கிளர்ச்சி"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சென்னை வாசிகள் சங்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "சென்னை வாசிகள் சங்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சென்னை மகாஜன சங்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "சென்னை மகாஜன சங்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சுதேசி நீராவி கப்பல் நிறுவனம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "சுதேசி நீராவி கப்பல் நிறுவனம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சென்னை ஜனசங்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "சென்னை ஜனசங்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > தன்னாட்சி இயக்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "தன்னாட்சி இயக்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > ரௌலட் அறப்போராட்டம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "ரௌலட் அறப்போராட்டம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > கிலாபத் இயக்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "கிலாபத் இயக்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > ஒத்துழையாமை இயக்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "ஒத்துழையாமை இயக்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > நீல் சிலை அறப்போராட்டம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "நீல் சிலை அறப்போராட்டம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சைமன் குழு புறக்கணிப்பு": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "சைமன் குழு புறக்கணிப்பு"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > சட்ட மறுப்பு இயக்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "சட்ட மறுப்பு இயக்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > தனிநபர் சத்தியாக்கிரகம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "தனிநபர் சத்தியாக்கிரகம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of Tamil Nadu in freedom struggle > வெள்ளையனே வெளியேறு இயக்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of Tamil Nadu in freedom struggle",
        "subtopic": "வெள்ளையனே வெளியேறு இயக்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > தில்லையாடி வள்ளியம்மை": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "தில்லையாடி வள்ளியம்மை"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > அஞ்சலை அம்மாள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "அஞ்சலை அம்மாள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > அம்புஜத்தம்மாள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "அம்புஜத்தம்மாள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > முத்துலட்சுமி ரெட்டி": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "முத்துலட்சுமி ரெட்டி"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > எஸ். தர்மாம்பாள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "எஸ். தர்மாம்பாள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > மூவலூர் இராமாமிர்தம் அம்மையார்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "மூவலூர் இராமாமிர்தம் அம்மையார்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > ருக்மணி லட்சுமிபதி": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "ருக்மணி லட்சுமிபதி"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > எஸ்.ஆர்.கண்ணம்மா": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "எஸ்.ஆர்.கண்ணம்மா"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > நாகம்மையார்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "நாகம்மையார்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Role of women in freedom struggle > துர்க்காபாய் தேஷ்முக்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Role of women in freedom struggle",
        "subtopic": "துர்க்காபாய் தேஷ்முக்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > இராமலிங்க அடிகளார்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "இராமலிங்க அடிகளார்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > நாராயணகுரு": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "நாராயணகுரு"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > அய்யன்காளி": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "அய்யன்காளி"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Evolution of 19th and 20th century socio-political movements in Tamil Nadu > வைகுண்ட சாமிகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Evolution of 19th and 20th century socio-political movements in Tamil Nadu",
        "subtopic": "வைகுண்ட சாமிகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > திராவிடர் மகா ஜனசபை": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "திராவிடர் மகா ஜனசபை"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > தென்னிந்திய நல உரிமை சங்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "தென்னிந்திய நல உரிமை சங்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > பிராமணரல்லாதார் மாநாடு": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "பிராமணரல்லாதார் மாநாடு"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > நீதிக்கட்சியின் கொள்கைகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "நீதிக்கட்சியின் கொள்கைகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > சென்னை மாகாண சங்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "சென்னை மாகாண சங்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > நீதிக்கட்சியும் தன்னாட்சி இயக்கமும்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "நீதிக்கட்சியும் தன்னாட்சி இயக்கமும்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > Justice Party": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "Justice Party"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Justice Party > சாதனையாளர்கள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Justice Party",
        "subtopic": "சாதனையாளர்கள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Self Respect Movement > 15 அம்சக் கொள்கை": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Self Respect Movement",
        "subtopic": "15 அம்சக் கொள்கை"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Self Respect Movement > சுயமரியாதை இயக்கத்தின் மாநாடு": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Self Respect Movement",
        "subtopic": "சுயமரியாதை இயக்கத்தின் மாநாடு"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Self Respect Movement > சுயமரியாதை இயக்கத்தின் சாதனைகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Self Respect Movement",
        "subtopic": "சுயமரியாதை இயக்கத்தின் சாதனைகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > பகுத்தறிவு - விளக்கம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "பகுத்தறிவு - விளக்கம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > பெண் விடுதலை": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "பெண் விடுதலை"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > சமூக சீர்திருத்தம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "சமூக சீர்திருத்தம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Thanthai Periyar > வைக்கம் போராட்டம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Thanthai Periyar",
        "subtopic": "வைக்கம் போராட்டம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > அண்ணாவின் பொன்மொழிகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "அண்ணாவின் பொன்மொழிகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > திராவிடர் கழகம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "திராவிடர் கழகம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > தி.மு.க தோற்றம்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "தி.மு.க தோற்றம்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > தமிழக முதல்வராக அண்ணாவின் சாதனைகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "தமிழக முதல்வராக அண்ணாவின் சாதனைகள்"
    },
    "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6) > Contributions of Perarignar Anna > அண்ணாவின் இலக்கிய படைப்புகள்": {
        "subject": "History, Culture, Heritage, and Socio-Political Movements in Tamil Nadu (Unit 6)",
        "topic": "Contributions of Perarignar Anna",
        "subtopic": "அண்ணாவின் இலக்கிய படைப்புகள்"
    },
    "Aptitude (Part B Unit 1) > Simplification > BODMAS": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Simplification",
        "subtopic": "BODMAS"
    },
    "Aptitude (Part B Unit 1) > Simplification > Powers": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Simplification",
        "subtopic": "Powers"
    },
    "Aptitude (Part B Unit 1) > Simplification > Surds & Indices": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Simplification",
        "subtopic": "Surds & Indices"
    },
    "Aptitude (Part B Unit 1) > Simplification > AP & GP": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Simplification",
        "subtopic": "AP & GP"
    },
    "Aptitude (Part B Unit 1) > Simplification > Special Series": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Simplification",
        "subtopic": "Special Series"
    },
    "Aptitude (Part B Unit 1) > Percentage > Percentage Increase and Decrease": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Percentage",
        "subtopic": "Percentage Increase and Decrease"
    },
    "Aptitude (Part B Unit 1) > Percentage > Exam and Marks Related Problems": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Percentage",
        "subtopic": "Exam and Marks Related Problems"
    },
    "Aptitude (Part B Unit 1) > Percentage > Population and Growth Problems": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Percentage",
        "subtopic": "Population and Growth Problems"
    },
    "Aptitude (Part B Unit 1) > Percentage > Profit and Loss": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Percentage",
        "subtopic": "Profit and Loss"
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > Problems on Remainders": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "Problems on Remainders"
    },
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > problems on Multiples and Factors": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "problems on Multiples and Factors"
    },
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > Prime Factorization and Division Method Usage": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "Prime Factorization and Division Method Usage"
    },
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Mixture and Alligation": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Ratio and Proportion",
        "subtopic": "Mixture and Alligation"
    },
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Problems on Ages": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Ratio and Proportion",
        "subtopic": "Problems on Ages"
    },
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Number System": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Ratio and Proportion",
        "subtopic": "Number System"
    },
    "Aptitude (Part B Unit 1) > Ratio and Proportion > Average": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Ratio and Proportion",
        "subtopic": "Average"
    },
    "Aptitude (Part B Unit 1) > Simple interest > Finding Total Amount, Principal, Interest, Time": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Simple interest",
        "subtopic": "Finding Total Amount, Principal, Interest, Time"
    },
    "Aptitude (Part B Unit 1) > Simple interest > Borrowing and Lending Problem": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Simple interest",
        "subtopic": "Borrowing and Lending Problem"
    },
    "Aptitude (Part B Unit 1) > Compound interest > Finding Total Amount, Principal, Interest, Time": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Compound interest",
        "subtopic": "Finding Total Amount, Principal, Interest, Time"
    },
    "Aptitude (Part B Unit 1) > Compound interest > Compound Interest When Interest is Compounded Half-Yearly or Quarterly": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Compound interest",
        "subtopic": "Compound Interest When Interest is Compounded Half-Yearly or Quarterly"
    },
    "Aptitude (Part B Unit 1) > Compound interest > Difference Between Simple Interest and Compound Interest": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Compound interest",
        "subtopic": "Difference Between Simple Interest and Compound Interest"
    },
    "Aptitude (Part B Unit 1) > Area > Square": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Area",
        "subtopic": "Square"
    },
    "Aptitude (Part B Unit 1) > Area > Rectangle": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Area",
        "subtopic": "Rectangle"
    },
    "Aptitude (Part B Unit 1) > Area > Triangle": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Area",
        "subtopic": "Triangle"
    },
    "Aptitude (Part B Unit 1) > Area > Circle": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Area",
        "subtopic": "Circle"
    },
    "Aptitude (Part B Unit 1) > Area > Parallelogram": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Area",
        "subtopic": "Parallelogram"
    },
    "Aptitude (Part B Unit 1) > Area > Trapezoid": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Area",
        "subtopic": "Trapezoid"
    },
    "Aptitude (Part B Unit 1) > Volume > Cube": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Volume",
        "subtopic": "Cube"
    },
    "Aptitude (Part B Unit 1) > Volume > Cuboid": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Volume",
        "subtopic": "Cuboid"
    },
    "Aptitude (Part B Unit 1) > Volume > Cone": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Volume",
        "subtopic": "Cone"
    },
    "Aptitude (Part B Unit 1) > Volume > Cylinder": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Volume",
        "subtopic": "Cylinder"
    },
    "Aptitude (Part B Unit 1) > Volume > Sphere": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Volume",
        "subtopic": "Sphere"
    },
    "Aptitude (Part B Unit 1) > Volume > Hemi Sphere": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Volume",
        "subtopic": "Hemi Sphere"
    },
    "Aptitude (Part B Unit 1) > Time and Work > Work Done by Multiple People Together": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Time and Work",
        "subtopic": "Work Done by Multiple People Together"
    },
    "Aptitude (Part B Unit 1) > Time and Work > Work and Efficiency Relationship": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Time and Work",
        "subtopic": "Work and Efficiency Relationship"
    },
    "Aptitude (Part B Unit 1) > Time and Work > Work Done by Alternating Workers": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Time and Work",
        "subtopic": "Work Done by Alternating Workers"
    },
    "Reasoning (Part B Unit 2) > Logical reasoning > seating arrangment": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Logical reasoning",
        "subtopic": "seating arrangment"
    },
    "Reasoning (Part B Unit 2) > Logical reasoning > Chronological order": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Logical reasoning",
        "subtopic": "Chronological order"
    },
    "Reasoning (Part B Unit 2) > Logical reasoning > syllogism": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Logical reasoning",
        "subtopic": "syllogism"
    },
    "Reasoning (Part B Unit 2) > Logical reasoning > Venn diagram": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Logical reasoning",
        "subtopic": "Venn diagram"
    },
    "Reasoning (Part B Unit 2) > Logical reasoning > Calander": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Logical reasoning",
        "subtopic": "Calander"
    },
    "Reasoning (Part B Unit 2) > Logical reasoning > Statement and Conclusions": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Logical reasoning",
        "subtopic": "Statement and Conclusions"
    },
    "Reasoning (Part B Unit 2) > Puzzles > Box Type Missing numbers": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Puzzles",
        "subtopic": "Box Type Missing numbers"
    },
    "Reasoning (Part B Unit 2) > Puzzles > Number of Triangle Etc": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Puzzles",
        "subtopic": "Number of Triangle Etc"
    },
    "Reasoning (Part B Unit 2) > Puzzles > Blood Relations": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Puzzles",
        "subtopic": "Blood Relations"
    },
    "Reasoning (Part B Unit 2) > Puzzles > Classification & Odd one out": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Puzzles",
        "subtopic": "Classification & Odd one out"
    },
    "Reasoning (Part B Unit 2) > Dice > Normal Dice": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Dice",
        "subtopic": "Normal Dice"
    },
    "Reasoning (Part B Unit 2) > Dice > Standard Dice": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Dice",
        "subtopic": "Standard Dice"
    },
    "Reasoning (Part B Unit 2) > Visual reasoning > Clock": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Visual reasoning",
        "subtopic": "Clock"
    },
    "Reasoning (Part B Unit 2) > Visual reasoning > Directions": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Visual reasoning",
        "subtopic": "Directions"
    },
    "Reasoning (Part B Unit 2) > Visual reasoning > Embeded figures": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Visual reasoning",
        "subtopic": "Embeded figures"
    },
    "Reasoning (Part B Unit 2) > Visual reasoning > Figural Classifications": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Visual reasoning",
        "subtopic": "Figural Classifications"
    },
    "Reasoning (Part B Unit 2) > Visual reasoning > Paper Cutting and Folding": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Visual reasoning",
        "subtopic": "Paper Cutting and Folding"
    },
    "Reasoning (Part B Unit 2) > Visual reasoning > Mirror iamge": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Visual reasoning",
        "subtopic": "Mirror iamge"
    },
    "Reasoning (Part B Unit 2) > Alpha numeric reasoning > Analogy": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Alpha numeric reasoning",
        "subtopic": "Analogy"
    },
    "Reasoning (Part B Unit 2) > Alpha numeric reasoning > Coding and decoding": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Alpha numeric reasoning",
        "subtopic": "Coding and decoding"
    },
    "Reasoning (Part B Unit 2) > Alpha numeric reasoning > Missing Letters": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Alpha numeric reasoning",
        "subtopic": "Missing Letters"
    },
    "Reasoning (Part B Unit 2) > Number series > Mathematical Operations": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Number series",
        "subtopic": "Mathematical Operations"
    },
    "Reasoning (Part B Unit 2) > Number series > Missing numbers": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Number series",
        "subtopic": "Missing numbers"
    },
    "Reasoning (Part B Unit 2) > Number series > Series complete": {
        "subject": "Reasoning (Part B Unit 2)",
        "topic": "Number series",
        "subtopic": "Series complete"
    },
    "TAMIL LANGUAGE > எழுத்து > பிரித்து எழுதுதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "பிரித்து எழுதுதல்‌"
    },
    "TAMIL LANGUAGE > எழுத்து > சேர்த்து எழுதுதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "சேர்த்து எழுதுதல்‌"
    },
    "TAMIL LANGUAGE > எழுத்து > சந்திப்பிழை": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "சந்திப்பிழை"
    },
    "TAMIL LANGUAGE > எழுத்து > குறில்‌, நெடில்‌ வேறுபாடு": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "குறில்‌, நெடில்‌ வேறுபாடு"
    },
    "TAMIL LANGUAGE > எழுத்து > லகர,ளகர, ழகர வேறுபாடு": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "லகர,ளகர, ழகர வேறுபாடு"
    },
    "TAMIL LANGUAGE > எழுத்து > னகர, ணகர வேறுபாடு": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "னகர, ணகர வேறுபாடு"
    },
    "TAMIL LANGUAGE > எழுத்து > ரகர, றகர வேறுபாடு": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "ரகர, றகர வேறுபாடு"
    },
    "TAMIL LANGUAGE > எழுத்து > இனவெழுத்துகள்‌ அறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "இனவெழுத்துகள்‌ அறிதல்‌"
    },
    "TAMIL LANGUAGE > எழுத்து > சுட்டு எழுத்துகள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "சுட்டு எழுத்துகள்‌"
    },
    "TAMIL LANGUAGE > எழுத்து > வினா எழுத்துகள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "வினா எழுத்துகள்‌"
    },
    "TAMIL LANGUAGE > எழுத்து > ஒருமைப்‌ பன்மை அறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுத்து",
        "subtopic": "ஒருமைப்‌ பன்மை அறிதல்‌"
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வேர்ச்சொல்‌ அறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "வேர்ச்சொல்‌ அறிதல்‌"
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வேர்ச்சொல்லில்‌ இருந்து வினைமுற்று, வினையெச்சம்‌, வினையாலணையும்‌ பெயர்‌,பெயரெச்சம்‌ வகை அறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "வேர்ச்சொல்லில்‌ இருந்து வினைமுற்று, வினையெச்சம்‌, வினையாலணையும்‌ பெயர்‌,பெயரெச்சம்‌ வகை அறிதல்‌"
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > அயற்சொல்‌ - தமிழ்ச்சொல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "அயற்சொல்‌ - தமிழ்ச்சொல்‌"
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > எதிர்ச்சொல்‌.": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "எதிர்ச்சொல்‌."
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வினைச்சொல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "வினைச்சொல்‌"
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > வினையெச்சம் பெயரெச்சம்": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "வினையெச்சம் பெயரெச்சம்"
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > எழுத்துப்‌ பிழை, ஒற்றுப்பிழை அறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "எழுத்துப்‌ பிழை, ஒற்றுப்பிழை அறிதல்‌"
    },
    "TAMIL LANGUAGE > சொல் இலக்கணம் > இரண்டு வினைச்‌ சொற்களின்‌ வேறுபாடு அறிதல்‌தொடர் வகைகள்": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல் இலக்கணம்",
        "subtopic": "இரண்டு வினைச்‌ சொற்களின்‌ வேறுபாடு அறிதல்‌தொடர் வகைகள்"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > எதிர்ச்சொல்லை எடுத்தெழுதுதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "எதிர்ச்சொல்லை எடுத்தெழுதுதல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > ஓரெழுத்து ஒரு மொழிக்கு உரிய பொருளைக்‌ கண்டறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "ஓரெழுத்து ஒரு மொழிக்கு உரிய பொருளைக்‌ கண்டறிதல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > ஒரு பொருள்‌ தரும்‌ பல சொற்கள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "ஒரு பொருள்‌ தரும்‌ பல சொற்கள்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பொருந்தா சொல்லைக்‌ கண்டறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பொருந்தா சொல்லைக்‌ கண்டறிதல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > அகர வரிசைப்படி சொற்களைச்‌ சீர்செய்தல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "அகர வரிசைப்படி சொற்களைச்‌ சீர்செய்தல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > ஒருபொருள்‌ பன்மொழி": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "ஒருபொருள்‌ பன்மொழி"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > இருபொருள்‌ குறிக்கும்‌ சொற்கள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "இருபொருள்‌ குறிக்கும்‌ சொற்கள்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பேச்சு வழக்கு, எழுத்து வழக்கு": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பேச்சு வழக்கு, எழுத்து வழக்கு"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > சொல்லும்‌ பொருளும்‌ அறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "சொல்லும்‌ பொருளும்‌ அறிதல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > ஒரு சொல்லிற்கு இணையான வேறு சொல் அறிதல்‌.": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "ஒரு சொல்லிற்கு இணையான வேறு சொல் அறிதல்‌."
    },
    "TAMIL LANGUAGE > சொல்லகராதி > கோடிட்ட இடத்தில்‌ சரியான சொல்லைத்‌ தேர்ந்தெடுத்து எழுதுதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "கோடிட்ட இடத்தில்‌ சரியான சொல்லைத்‌ தேர்ந்தெடுத்து எழுதுதல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பொருத்தமான பொருளைத்‌ தெரிவு செய்தல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பொருத்தமான பொருளைத்‌ தெரிவு செய்தல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > ஊர்ப்‌ பெயர்களின்‌ மரூஉவை எழுதுக": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "ஊர்ப்‌ பெயர்களின்‌ மரூஉவை எழுதுக"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பிழை திருத்துக. (எ.கா) ஒரு - ஓர்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பிழை திருத்துக. (எ.கா) ஒரு - ஓர்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பேச்சுவழக்குச்‌ சொற்களுக்கு இணையான தூய தமிழ்ச்‌ சொற்களை இணைத்தல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பேச்சுவழக்குச்‌ சொற்களுக்கு இணையான தூய தமிழ்ச்‌ சொற்களை இணைத்தல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பேச்சு வழக்குத்‌ தொடர்களிலுள்ள பிழை திருத்தம்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பேச்சு வழக்குத்‌ தொடர்களிலுள்ள பிழை திருத்தம்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > சொற்களை இணைத்துப்‌ புதிய சொல்‌ உருவாக்குதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "சொற்களை இணைத்துப்‌ புதிய சொல்‌ உருவாக்குதல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > அடைப்புக்குள்‌ உள்ள சொல்லைத்‌ தகுந்த இடத்தில்‌ சேர்த்தல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "அடைப்புக்குள்‌ உள்ள சொல்லைத்‌ தகுந்த இடத்தில்‌ சேர்த்தல்‌"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பல பொருள்‌ தரும்‌ ஓர்‌ எழுத்து": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பல பொருள்‌ தரும்‌ ஓர்‌ எழுத்து"
    },
    "TAMIL LANGUAGE > சொல்லகராதி > பல பொருள்‌ தரும்‌ ஒரு சொல்லைக்‌ கூறுக": {
        "subject": "TAMIL LANGUAGE",
        "topic": "சொல்லகராதி",
        "subtopic": "பல பொருள்‌ தரும்‌ ஒரு சொல்லைக்‌ கூறுக"
    },
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > சொற்களை ஒழுங்குபடுத்திச்‌ சொற்றொடர்‌ அமைத்தல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுதும்‌ திறன்‌",
        "subtopic": "சொற்களை ஒழுங்குபடுத்திச்‌ சொற்றொடர்‌ அமைத்தல்‌"
    },
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > தொடர்‌ வகைகள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுதும்‌ திறன்‌",
        "subtopic": "தொடர்‌ வகைகள்‌"
    },
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > செய்வினை, செயப்பாட்டு வினை": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுதும்‌ திறன்‌",
        "subtopic": "செய்வினை, செயப்பாட்டு வினை"
    },
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > தன்வினை, பிறவினை": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுதும்‌ திறன்‌",
        "subtopic": "தன்வினை, பிறவினை"
    },
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > ஒருமைப்‌ பன்மை பிழையறிந்து சரியான தொடரறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுதும்‌ திறன்‌",
        "subtopic": "ஒருமைப்‌ பன்மை பிழையறிந்து சரியான தொடரறிதல்‌"
    },
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > மரபுத்‌ தமிழ்‌: திணை மரபு,பால்‌ மரபு, காலம்‌, இளமைப்‌ பெயர்,வினைமரபு,தொகை மரபு": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுதும்‌ திறன்‌",
        "subtopic": "மரபுத்‌ தமிழ்‌: திணை மரபு,பால்‌ மரபு, காலம்‌, இளமைப்‌ பெயர்,வினைமரபு,தொகை மரபு"
    },
    "TAMIL LANGUAGE > எழுதும்‌ திறன்‌ > நிறுத்தல்‌ குறியீடுகள்.": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எழுதும்‌ திறன்‌",
        "subtopic": "நிறுத்தல்‌ குறியீடுகள்."
    },
    "TAMIL LANGUAGE > கலைச்‌ சொற்கள்‌ > பலதுறை சார்ந்த கலைச்‌ சொற்களை அதாவது அறிவியல்‌, கல்வி, மருத்துவம்‌, மேலாண்மை, சட்டம்‌, புவியியல்‌, தொழில்நுட்பம்‌, ஊடகம்‌, தகவல்‌ தொழில்நுட்பம்‌ உள்ளிட்ட பல்துறை சார்ந்த கலைச்‌ சொல்லுக்கு நேரான தமிழ்ச்‌ சொற்களை அறிந்திருக்க வேண்டும்‌.": {
        "subject": "TAMIL LANGUAGE",
        "topic": "கலைச்‌ சொற்கள்‌",
        "subtopic": "பலதுறை சார்ந்த கலைச்‌ சொற்களை அதாவது அறிவியல்‌, கல்வி, மருத்துவம்‌, மேலாண்மை, சட்டம்‌, புவியியல்‌, தொழில்நுட்பம்‌, ஊடகம்‌, தகவல்‌ தொழில்நுட்பம்‌ உள்ளிட்ட பல்துறை சார்ந்த கலைச்‌ சொல்லுக்கு நேரான தமிழ்ச்‌ சொற்களை அறிந்திருக்க வேண்டும்‌."
    },
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > கொடுக்கப்பட்ட பத்தியிலிருந்து கேட்கப்பட்ட வினாக்களுக்கு சரியான விடையைத்‌ தேர்ந்தெடுத்தல்‌-செய்தித்தாள்‌ - தலையங்கம்‌ - முகப்புச்‌ செய்திகள்‌ - அரசு சார்ந்த செய்திகள்‌ - கட்டுரைகள்‌ - இவற்றை வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ .": {
        "subject": "TAMIL LANGUAGE",
        "topic": "வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌",
        "subtopic": "கொடுக்கப்பட்ட பத்தியிலிருந்து கேட்கப்பட்ட வினாக்களுக்கு சரியான விடையைத்‌ தேர்ந்தெடுத்தல்‌-செய்தித்தாள்‌ - தலையங்கம்‌ - முகப்புச்‌ செய்திகள்‌ - அரசு சார்ந்த செய்திகள்‌ - கட்டுரைகள்‌ - இவற்றை வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ ."
    },
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > உவமைத்‌ தொடரின்‌ பொருளறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌",
        "subtopic": "உவமைத்‌ தொடரின்‌ பொருளறிதல்‌"
    },
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > மரபுத்‌ தொடரின்‌ பொருளறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌",
        "subtopic": "மரபுத்‌ தொடரின்‌ பொருளறிதல்‌"
    },
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > பழமொழிகள்‌ பொருளறிதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌",
        "subtopic": "பழமொழிகள்‌ பொருளறிதல்‌"
    },
    "TAMIL LANGUAGE > வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌ > ஆவண உள்ளடக்கங்களைப்‌ புரிந்து கொள்ளும்‌ திறன்‌.": {
        "subject": "TAMIL LANGUAGE",
        "topic": "வாசித்தல்‌ - புரிந்து கொள்ளும்‌ திறன்‌",
        "subtopic": "ஆவண உள்ளடக்கங்களைப்‌ புரிந்து கொள்ளும்‌ திறன்‌."
    },
    "TAMIL LANGUAGE > எளிய மொழி பெயர்ப்பு > ஆங்கிலம்‌ மற்றும்‌ பிறமொழிச்‌ சொற்களுக்கு இணையான தமிழ்ச்‌ சொற்கள்‌ அறிதல்‌ வேண்டும்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எளிய மொழி பெயர்ப்பு",
        "subtopic": "ஆங்கிலம்‌ மற்றும்‌ பிறமொழிச்‌ சொற்களுக்கு இணையான தமிழ்ச்‌ சொற்கள்‌ அறிதல்‌ வேண்டும்‌"
    },
    "TAMIL LANGUAGE > எளிய மொழி பெயர்ப்பு > பயன்பாட்டில்‌ உள்ள ஆங்கிலச்‌ சொற்களை மொழிபெயர்த்தல்‌ வேண்டும்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எளிய மொழி பெயர்ப்பு",
        "subtopic": "பயன்பாட்டில்‌ உள்ள ஆங்கிலச்‌ சொற்களை மொழிபெயர்த்தல்‌ வேண்டும்‌"
    },
    "TAMIL LANGUAGE > எளிய மொழி பெயர்ப்பு > ஆவணங்களின்‌ தலைப்பு - கோப்புகள்‌ - கடிதங்கள்‌ - மனுக்கள்‌ - மொழிபெயர்ப்பு புரிந்து கொள்ளுதல்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "எளிய மொழி பெயர்ப்பு",
        "subtopic": "ஆவணங்களின்‌ தலைப்பு - கோப்புகள்‌ - கடிதங்கள்‌ - மனுக்கள்‌ - மொழிபெயர்ப்பு புரிந்து கொள்ளுதல்‌"
    },
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > திருக்குறள்‌ தொடர்பான செய்திகள்‌ (இருபது அதிகாரங்கள்‌ மட்டும்‌) ஒழுக்கமுடைமை, பொறையுடைமை, ஊக்கமுடைமை, விருந்தோம்பல்‌, அறன்‌ வலியுறுத்தல்‌,ஈகை, பெரியாரைத்‌ துணைக்கோடல்‌, வினை செயல்வகை, அவையஞ்சாமை, கண்ணோட்டம்‌, அன்புடைமை, கல்வி,நடுநிலைமை, கூடா ஒழுக்கம்‌, கல்லாமை, செங்கோன்மை, பண்புடைமை, நட்பாராய்தல்‌, புறங்கூறாமை, அருளுடைமை - மேற்கோள்கள்‌.": {
        "subject": "TAMIL LANGUAGE",
        "topic": "இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌",
        "subtopic": "திருக்குறள்‌ தொடர்பான செய்திகள்‌ (இருபது அதிகாரங்கள்‌ மட்டும்‌) ஒழுக்கமுடைமை, பொறையுடைமை, ஊக்கமுடைமை, விருந்தோம்பல்‌, அறன்‌ வலியுறுத்தல்‌,ஈகை, பெரியாரைத்‌ துணைக்கோடல்‌, வினை செயல்வகை, அவையஞ்சாமை, கண்ணோட்டம்‌, அன்புடைமை, கல்வி,நடுநிலைமை, கூடா ஒழுக்கம்‌, கல்லாமை, செங்கோன்மை, பண்புடைமை, நட்பாராய்தல்‌, புறங்கூறாமை, அருளுடைமை - மேற்கோள்கள்‌."
    },
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > அறநூல்‌ தொடர்பான செய்திகள்‌ நாலடியார்‌, நான்மணிக்கடிகை, பழமொழி நானூறு, முதுமொழிக்காஞ்சி, திரிகடுகம்‌, இன்னாநாற்பது, சிறுபஞ்சமூலம்‌, ஏலாதி, அவ்வையார்‌ பாடல்கள்‌)": {
        "subject": "TAMIL LANGUAGE",
        "topic": "இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌",
        "subtopic": "அறநூல்‌ தொடர்பான செய்திகள்‌ நாலடியார்‌, நான்மணிக்கடிகை, பழமொழி நானூறு, முதுமொழிக்காஞ்சி, திரிகடுகம்‌, இன்னாநாற்பது, சிறுபஞ்சமூலம்‌, ஏலாதி, அவ்வையார்‌ பாடல்கள்‌)"
    },
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > தமிழின்‌ தொன்மை, சிறப்பு, திராவிட மொழிகள்‌ தொடர்பான செய்திகள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌",
        "subtopic": "தமிழின்‌ தொன்மை, சிறப்பு, திராவிட மொழிகள்‌ தொடர்பான செய்திகள்‌"
    },
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > உ.வே.சாமிநாத ஐயர்‌, தெ.பொ.மீனாட்சி சுந்தரம்‌, சி.இலக்குவனார்‌ தமிழ்ப்பணி தொடர்பான செய்திகள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌",
        "subtopic": "உ.வே.சாமிநாத ஐயர்‌, தெ.பொ.மீனாட்சி சுந்தரம்‌, சி.இலக்குவனார்‌ தமிழ்ப்பணி தொடர்பான செய்திகள்‌"
    },
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > தேவநேய பாவாணர்‌, அகரமுதலி, பாவலரேறு பெருஞ்சித்திரனார்‌, ஜி.யு.போப்‌, வீரமாமுனிவர்‌ தமிழ்த்‌ தொண்டு தொடர்பான செய்திகள்‌": {
        "subject": "TAMIL LANGUAGE",
        "topic": "இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌",
        "subtopic": "தேவநேய பாவாணர்‌, அகரமுதலி, பாவலரேறு பெருஞ்சித்திரனார்‌, ஜி.யு.போப்‌, வீரமாமுனிவர்‌ தமிழ்த்‌ தொண்டு தொடர்பான செய்திகள்‌"
    },
    "TAMIL LANGUAGE > இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌ > தமிழ்ச்‌ சான்றோர்‌ பற்றிய செய்திகள்‌: பாவேந்தர்‌, டி.கே.சிதம்பரனாதர்‌, தவத்திரு குன்றக்குடி அடிகளார்‌, கண்ணதாசன்‌, காயிதே மில்லத்‌, தாரா பாரதி, வேலுநாச்சியார்‌, பட்டுக்கோட்டைக்‌ கல்யாணசுந்தரம்‌, முடியரசன்‌, தமிழ்‌ ஒளி, உருத்திரங்கண்ணனார்‌, கி.வா.ஜகந்நாதர்‌, நாமக்கல்‌ கவிஞர்‌.": {
        "subject": "TAMIL LANGUAGE",
        "topic": "இலக்கியம்‌, தமிழ்‌ அறிஞர்களும்‌, தமிழ்த்தொண்டும்‌",
        "subtopic": "தமிழ்ச்‌ சான்றோர்‌ பற்றிய செய்திகள்‌: பாவேந்தர்‌, டி.கே.சிதம்பரனாதர்‌, தவத்திரு குன்றக்குடி அடிகளார்‌, கண்ணதாசன்‌, காயிதே மில்லத்‌, தாரா பாரதி, வேலுநாச்சியார்‌, பட்டுக்கோட்டைக்‌ கல்யாணசுந்தரம்‌, முடியரசன்‌, தமிழ்‌ ஒளி, உருத்திரங்கண்ணனார்‌, கி.வா.ஜகந்நாதர்‌, நாமக்கல்‌ கவிஞர்‌."
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF Basics": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "HCF Basics"
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF using Long Division Method": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "HCF using Long Division Method"
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF of Powers": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "HCF of Powers"
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF of Decimals": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "HCF of Decimals"
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > HCF of Fractions": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "HCF of Fractions"
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > Relation between HCF & LCM": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "Relation between HCF & LCM"
    },
    "Aptitude (Part B Unit 1) > Highest Common Factor (HCF) > Application Sums - HCF-based (e.g., dividing items, grouping problems)": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Highest Common Factor (HCF)",
        "subtopic": "Application Sums - HCF-based (e.g., dividing items, grouping problems)"
    },
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM Basics": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "LCM Basics"
    },
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM of Powers": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "LCM of Powers"
    },
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM of Decimals": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "LCM of Decimals"
    },
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > LCM of Fractions": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "LCM of Fractions"
    },
    "Aptitude (Part B Unit 1) > Lowest Common Multiple (LCM) > Application Sums - LCM-based (alarms, traffic lights, periodic events)": {
        "subject": "Aptitude (Part B Unit 1)",
        "topic": "Lowest Common Multiple (LCM)",
        "subtopic": "Application Sums - LCM-based (alarms, traffic lights, periodic events)"
    },
}


# ===== BANKING TAXONOMY =====

BANKING_SUBJECTS: List[str] = [
    "Aptitude",
    "English",
    "Reasoning",
]

BANKING_TRIPLETS: List[str] = [
    "Reasoning > Linear Arrangement > Facing North",
    "Reasoning > Linear Arrangement > Facing South",
    "Reasoning > Linear Arrangement > Facing North & South",
    "Reasoning > Linear Arrangement > Unknown no. of persons",
    "Reasoning > Linear Arrangement > Double row",
    "Reasoning > Linear Arrangement > Triple row",
    "Reasoning > Circular Arrangement > Facing Inside",
    "Reasoning > Circular Arrangement > Facing Outside",
    "Reasoning > Circular Arrangement > Facing inside & Outside",
    "Reasoning > Circular Arrangement > Unknown no. of persons",
    "Reasoning > Circular Arrangement > Concentric Circle",
    "Reasoning > Square > Facing Inside",
    "Reasoning > Square > Facing Outside",
    "Reasoning > Square > Facing inside & Outside",
    "Reasoning > Square > Concentric Square",
    "Reasoning > Rectangle > Facing Inside",
    "Reasoning > Rectangle > Facing Outside",
    "Reasoning > Rectangle > Facing inside & Outside",
    "Reasoning > Rectangle > Concentric rectangle",
    "Reasoning > Triangular Arrangement > Facing Inside",
    "Reasoning > Triangular Arrangement > Facing Outside",
    "Reasoning > Triangular Arrangement > Facing inside & Outside",
    "Reasoning > Triangular Arrangement > Concentric Triangle",
    "Reasoning > Hexagon Arrangement > Facing Inside",
    "Reasoning > Hexagon Arrangement > Facing Outside",
    "Reasoning > Hexagon Arrangement > Facing inside & Outside",
    "Reasoning > Hexagon Arrangement > Concentric",
    "Reasoning > Tabular Puzzle > Designation",
    "Reasoning > Tabular Puzzle > Days",
    "Reasoning > Tabular Puzzle > Month",
    "Reasoning > Tabular Puzzle > Month & Date",
    "Reasoning > Tabular Puzzle > Year & age",
    "Reasoning > Tabular Puzzle > Grouping",
    "Reasoning > Floor puzzle > Single floor",
    "Reasoning > Floor puzzle > Floor & Flat",
    "Reasoning > Floor puzzle > Unknown no. of Floor",
    "Reasoning > Box puzzle > Single stack",
    "Reasoning > Box puzzle > Stack 1 & Stack 2",
    "Reasoning > Box puzzle > Unknown no. of stack",
    "Reasoning > Other puzzle > Sequence based puzzle",
    "Reasoning > Other puzzle > Quantity based puzzle",
    "Reasoning > Other puzzle > Matrix based puzzle",
    "Reasoning > Other puzzle > Order & Ranking Puzzle",
    "Reasoning > Other puzzle > Pyramid Puzzle",
    "Reasoning > Coding decoding > Letter coding",
    "Reasoning > Coding decoding > Symbol digit coding",
    "Reasoning > Coding decoding > Coding in fictitious language",
    "Reasoning > Coding decoding > Coding based on condition",
    "Reasoning > Coding decoding > Problems based on new types: Letters; symbols and numbers",
    "Reasoning > Coding decoding > Box type coding and decoding",
    "Reasoning > Direction > Normal",
    "Reasoning > Direction > Coded direction",
    "Reasoning > Blood relation > Normal",
    "Reasoning > Blood relation > Coded Blood relation",
    "Reasoning > Alphanumeric Symbol series > Number+Alphabets+Symbol series",
    "Reasoning > Alphanumeric Symbol series > Three/Four letter Word series",
    "Reasoning > Alphanumeric Symbol series > Three digit Number Series",
    "Reasoning > Alphanumeric Symbol series > Conditional ANS series",
    "Reasoning > Syllogism > Direct",
    "Reasoning > Syllogism > Coded",
    "Reasoning > Syllogism > Reverse",
    "Reasoning > Inequality > Direct",
    "Reasoning > Inequality > Coded",
    "Reasoning > Inequality > Reverse",
    "Reasoning > Inequality > Missing inequality",
    "Reasoning > Miscellaneous > Order and Ranking",
    "Reasoning > Miscellaneous > Number operation",
    "Reasoning > Miscellaneous > Alphabet operation",
    "Reasoning > Miscellaneous > Pairs of letters",
    "Reasoning > Miscellaneous > Pairs of words",
    "Reasoning > Miscellaneous > Meaningful word",
    "Reasoning > Miscellaneous > Missing series",
    "Reasoning > Miscellaneous > Odd one out",
    "Reasoning > Miscellaneous > Next series",
    "Reasoning > Critical Reasoning > Statements and Arguments",
    "Reasoning > Critical Reasoning > Cause and Effect",
    "Reasoning > Critical Reasoning > Statements and Assumption",
    "Reasoning > Critical Reasoning > Statements and Course of Action",
    "Reasoning > Critical Reasoning > Statements and Conclusion",
    "Reasoning > Critical Reasoning > Statements and inferences",
    "Reasoning > Sequential Output Tracing > Numbers",
    "Reasoning > Sequential Output Tracing > Words",
    "Reasoning > Sequential Output Tracing > Numbers and words",
    "Reasoning > Sequential Output Tracing > Box type",
    "Reasoning > Statements - Data Sufficiency > 2 statements",
    "Reasoning > Statements - Data Sufficiency > 3 Statements",
    "Aptitude > Single Graph DI > DI Line",
    "Aptitude > Single Graph DI > DI Bar",
    "Aptitude > Single Graph DI > DI Table",
    "Aptitude > Single Graph DI > DI Pie",
    "Aptitude > Single Graph DI > DI Missing",
    "Aptitude > Single Graph DI > DI Radar",
    "Aptitude > Single Graph DI > DI Funnel",
    "Aptitude > Single Graph DI > DI Candle stick",
    "Aptitude > Single Graph DI > DI Caselet",
    "Aptitude > Mixed DI > DI Table + Pie",
    "Aptitude > Mixed DI > DI Table + Bar",
    "Aptitude > Mixed DI > DI Table + Line",
    "Aptitude > Mixed DI > Double Pie DI",
    "Aptitude > Mixed DI > Double Bar DI",
    "Aptitude > Mixed DI > Double Line DI",
    "Aptitude > Mixed DI > DI Pie + Line",
    "Aptitude > Mixed DI > DI Pie + Bar",
    "Aptitude > Mixed DI > DI line + Bar",
    "Aptitude > Mixed DI > DI Graph with Note",
    "Aptitude > Application DI > Arithematic question based DI",
    "Aptitude > Missing Number > Single series",
    "Aptitude > Missing Number > Double series with statement",
    "Aptitude > Missing Number > Triple series with statement",
    "Aptitude > Missing Number > Single series with Quadratic equation",
    "Aptitude > Wrong Number > Single series",
    "Aptitude > Wrong Number > Double series with statement",
    "Aptitude > Wrong Number > Triple series with statement",
    "Aptitude > Quadratic Equation > Linear Equation",
    "Aptitude > Quadratic Equation > Quadratic Equation with Coefficient",
    "Aptitude > Quadratic Equation > Quadratic Equation with out Coefficient",
    "Aptitude > Quadratic Equation > New pattern QE",
    "Aptitude > Quadratic Equation > Simplification",
    "Aptitude > Quadratic Equation > Approximation",
    "Aptitude > Quantity Comparison > Quantity I & II (All Arithmetic topic)",
    "Aptitude > Data sufficiency > 2 statement (All Arithmetic topic)",
    "Aptitude > Data sufficiency > 3 Statement (All Arithmetic topic)",
    "Aptitude > Ratio Proportion > Statement Question",
    "Aptitude > Ratio Proportion > Passage based Question",
    "Aptitude > Ratio Proportion > Double filler question",
    "Aptitude > Average > Statement Question",
    "Aptitude > Average > Passage based Question",
    "Aptitude > Average > Double filler question",
    "Aptitude > Percentage > Statement Question",
    "Aptitude > Percentage > Passage based Question",
    "Aptitude > Percentage > Double filler question",
    "Aptitude > Ages > Statement Question",
    "Aptitude > Ages > Passage based Question",
    "Aptitude > Ages > Double filler question",
    "Aptitude > Partnership > Statement Question",
    "Aptitude > Partnership > Passage based Question",
    "Aptitude > Partnership > Double filler question",
    "Aptitude > Profit & Loss > Statement Question",
    "Aptitude > Profit & Loss > Passage based Question",
    "Aptitude > Profit & Loss > Double filler question",
    "Aptitude > Time Speed Distance > Statement Question",
    "Aptitude > Time Speed Distance > Passage based Question",
    "Aptitude > Time Speed Distance > Double filler question",
    "Aptitude > Problems on Trains > Statement Question",
    "Aptitude > Problems on Trains > Passage based Question",
    "Aptitude > Problems on Trains > Double filler question",
    "Aptitude > Boats & Stream > Statement Question",
    "Aptitude > Boats & Stream > Passage based Question",
    "Aptitude > Boats & Stream > Double filler question",
    "Aptitude > Time & Work > Statement Question",
    "Aptitude > Time & Work > Passage based Question",
    "Aptitude > Time & Work > Double filler question",
    "Aptitude > Pipes & Cistern > Statement Question",
    "Aptitude > Pipes & Cistern > Passage based Question",
    "Aptitude > Pipes & Cistern > Double filler question",
    "Aptitude > Simple Interest > Statement Question",
    "Aptitude > Simple Interest > Passage based Question",
    "Aptitude > Simple Interest > Double filler question",
    "Aptitude > Compound Interest > Statement Question",
    "Aptitude > Compound Interest > Passage based Question",
    "Aptitude > Compound Interest > Double filler question",
    "Aptitude > Mixture Allegation > Statement Question",
    "Aptitude > Mixture Allegation > Passage based Question",
    "Aptitude > Mixture Allegation > Double filler question",
    "Aptitude > Permutation & Combination > Statement Question",
    "Aptitude > Permutation & Combination > Passage based Question",
    "Aptitude > Permutation & Combination > Double filler question",
    "Aptitude > Probability > Statement Question",
    "Aptitude > Probability > Passage based Question",
    "Aptitude > Probability > Double filler question",
    "English > Reading Comprehension > Analytical passage",
    "English > Reading Comprehension > Informative passage",
    "English > Reading Comprehension > Banking and Economy",
    "English > Reading Comprehension > Story-based passage",
    "English > Reading Comprehension > Technology",
    "English > Reading Comprehension > Research-based",
    "English > Reading Comprehension > Health and Self-improvement",
    "English > Parajumble > Basic para jumble",
    "English > Parajumble > Para jumble with exclusion or inclusion",
    "English > Parajumble > Para jumble with error spotting",
    "English > Parajumble > Para jumble with rearrangement",
    "English > Parajumble > Para jumble with a blank",
    "English > Parajumble > Para jumble with match the columns",
    "English > Parajumble > Para jumble with phrasal filler",
    "English > Parajumble > Para jumble with a fixed sentence",
    "English > Sentence Rearrangement > Rearrangement with four/five parts",
    "English > Sentence Rearrangement > Omission of irrelevant part",
    "English > Match the columns > Basic pattern with two or three columns",
    "English > Match the columns > Match the column with the connector",
    "English > Match the columns > Columns with fillers or word swap",
    "English > Match the columns > Columns with error spotting",
    "English > Match the columns > Match the column with column fillers",
    "English > Statement based > Para completion",
    "English > Statement based > Paragraph inference or cause",
    "English > Statement based > odd one out from the theme",
    "English > Error Spotting > Correct sentence",
    "English > Error Spotting > Incorrect sentence",
    "English > Error Spotting > Number of errors in a sentence",
    "English > Error Spotting > Error parts in a sentence",
    "English > Error Spotting > Error-free parts in a sentence",
    "English > Phrasal replacement > Phrasal verb replacement",
    "English > Phrasal replacement > Phrase replacement",
    "English > Phrasal replacement > Choose the correct meaning of the highlighted phrase",
    "English > Cloze test > Basic type",
    "English > Cloze test > Blanks followed by a synonym",
    "English > Cloze test > Two or three options for a single blank",
    "English > Cloze test > Inappropriate option for the blank",
    "English > Cloze test > Blanks to be filled by a phrase or phrasal verb",
    "English > Fill in the blanks > Single filler",
    "English > Fill in the blanks > Double filler",
    "English > Fill in the blanks > Triple filler",
    "English > Word Usage > Usage of words",
    "English > Word Swap > Word swap in a sentence",
    "English > Word Swap > Word swap in a passage",
    "English > Word Swap > Word swap with inappropriate word",
    "English > Mis-spelt > Spelling error",
    "English > Mis-spelt > Inappropriate words",
    "English > Words > Synonyms",
    "English > Words > Antonyms",
    "English > Idioms > Meaning of the idioms",
    "English > Idioms > Meaning of the phrases",
    "English > Idioms > Fillers with Idioms",
    "English > Idioms > Fillers with Phrasal verbs",
    "English > Idioms > Similar usage of the Idiom",
    "English > Idioms > Similar usage of the phrase",
    "English > Connectors/starters > Grammar-based",
    "English > Connectors/starters > Context-based",
]

BANKING_TRIPLET_DICT: Dict[str, Dict[str, str]] = {
    "Reasoning > Linear Arrangement > Facing North": {
        "subject": "Reasoning",
        "topic": "Linear Arrangement",
        "subtopic": "Facing North"
    },
    "Reasoning > Linear Arrangement > Facing South": {
        "subject": "Reasoning",
        "topic": "Linear Arrangement",
        "subtopic": "Facing South"
    },
    "Reasoning > Linear Arrangement > Facing North & South": {
        "subject": "Reasoning",
        "topic": "Linear Arrangement",
        "subtopic": "Facing North & South"
    },
    "Reasoning > Linear Arrangement > Unknown no. of persons": {
        "subject": "Reasoning",
        "topic": "Linear Arrangement",
        "subtopic": "Unknown no. of persons"
    },
    "Reasoning > Linear Arrangement > Double row": {
        "subject": "Reasoning",
        "topic": "Linear Arrangement",
        "subtopic": "Double row"
    },
    "Reasoning > Linear Arrangement > Triple row": {
        "subject": "Reasoning",
        "topic": "Linear Arrangement",
        "subtopic": "Triple row"
    },
    "Reasoning > Circular Arrangement > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Circular Arrangement",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Circular Arrangement > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Circular Arrangement",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Circular Arrangement > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Circular Arrangement",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Circular Arrangement > Unknown no. of persons": {
        "subject": "Reasoning",
        "topic": "Circular Arrangement",
        "subtopic": "Unknown no. of persons"
    },
    "Reasoning > Circular Arrangement > Concentric Circle": {
        "subject": "Reasoning",
        "topic": "Circular Arrangement",
        "subtopic": "Concentric Circle"
    },
    "Reasoning > Square > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Square",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Square > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Square",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Square > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Square",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Square > Concentric Square": {
        "subject": "Reasoning",
        "topic": "Square",
        "subtopic": "Concentric Square"
    },
    "Reasoning > Rectangle > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Rectangle",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Rectangle > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Rectangle",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Rectangle > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Rectangle",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Rectangle > Concentric rectangle": {
        "subject": "Reasoning",
        "topic": "Rectangle",
        "subtopic": "Concentric rectangle"
    },
    "Reasoning > Triangular Arrangement > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Triangular Arrangement",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Triangular Arrangement > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Triangular Arrangement",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Triangular Arrangement > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Triangular Arrangement",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Triangular Arrangement > Concentric Triangle": {
        "subject": "Reasoning",
        "topic": "Triangular Arrangement",
        "subtopic": "Concentric Triangle"
    },
    "Reasoning > Hexagon Arrangement > Facing Inside": {
        "subject": "Reasoning",
        "topic": "Hexagon Arrangement",
        "subtopic": "Facing Inside"
    },
    "Reasoning > Hexagon Arrangement > Facing Outside": {
        "subject": "Reasoning",
        "topic": "Hexagon Arrangement",
        "subtopic": "Facing Outside"
    },
    "Reasoning > Hexagon Arrangement > Facing inside & Outside": {
        "subject": "Reasoning",
        "topic": "Hexagon Arrangement",
        "subtopic": "Facing inside & Outside"
    },
    "Reasoning > Hexagon Arrangement > Concentric": {
        "subject": "Reasoning",
        "topic": "Hexagon Arrangement",
        "subtopic": "Concentric"
    },
    "Reasoning > Tabular Puzzle > Designation": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzle",
        "subtopic": "Designation"
    },
    "Reasoning > Tabular Puzzle > Days": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzle",
        "subtopic": "Days"
    },
    "Reasoning > Tabular Puzzle > Month": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzle",
        "subtopic": "Month"
    },
    "Reasoning > Tabular Puzzle > Month & Date": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzle",
        "subtopic": "Month & Date"
    },
    "Reasoning > Tabular Puzzle > Year & age": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzle",
        "subtopic": "Year & age"
    },
    "Reasoning > Tabular Puzzle > Grouping": {
        "subject": "Reasoning",
        "topic": "Tabular Puzzle",
        "subtopic": "Grouping"
    },
    "Reasoning > Floor puzzle > Single floor": {
        "subject": "Reasoning",
        "topic": "Floor puzzle",
        "subtopic": "Single floor"
    },
    "Reasoning > Floor puzzle > Floor & Flat": {
        "subject": "Reasoning",
        "topic": "Floor puzzle",
        "subtopic": "Floor & Flat"
    },
    "Reasoning > Floor puzzle > Unknown no. of Floor": {
        "subject": "Reasoning",
        "topic": "Floor puzzle",
        "subtopic": "Unknown no. of Floor"
    },
    "Reasoning > Box puzzle > Single stack": {
        "subject": "Reasoning",
        "topic": "Box puzzle",
        "subtopic": "Single stack"
    },
    "Reasoning > Box puzzle > Stack 1 & Stack 2": {
        "subject": "Reasoning",
        "topic": "Box puzzle",
        "subtopic": "Stack 1 & Stack 2"
    },
    "Reasoning > Box puzzle > Unknown no. of stack": {
        "subject": "Reasoning",
        "topic": "Box puzzle",
        "subtopic": "Unknown no. of stack"
    },
    "Reasoning > Other puzzle > Sequence based puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzle",
        "subtopic": "Sequence based puzzle"
    },
    "Reasoning > Other puzzle > Quantity based puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzle",
        "subtopic": "Quantity based puzzle"
    },
    "Reasoning > Other puzzle > Matrix based puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzle",
        "subtopic": "Matrix based puzzle"
    },
    "Reasoning > Other puzzle > Order & Ranking Puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzle",
        "subtopic": "Order & Ranking Puzzle"
    },
    "Reasoning > Other puzzle > Pyramid Puzzle": {
        "subject": "Reasoning",
        "topic": "Other puzzle",
        "subtopic": "Pyramid Puzzle"
    },
    "Reasoning > Coding decoding > Letter coding": {
        "subject": "Reasoning",
        "topic": "Coding decoding",
        "subtopic": "Letter coding"
    },
    "Reasoning > Coding decoding > Symbol digit coding": {
        "subject": "Reasoning",
        "topic": "Coding decoding",
        "subtopic": "Symbol digit coding"
    },
    "Reasoning > Coding decoding > Coding in fictitious language": {
        "subject": "Reasoning",
        "topic": "Coding decoding",
        "subtopic": "Coding in fictitious language"
    },
    "Reasoning > Coding decoding > Coding based on condition": {
        "subject": "Reasoning",
        "topic": "Coding decoding",
        "subtopic": "Coding based on condition"
    },
    "Reasoning > Coding decoding > Problems based on new types: Letters; symbols and numbers": {
        "subject": "Reasoning",
        "topic": "Coding decoding",
        "subtopic": "Problems based on new types: Letters; symbols and numbers"
    },
    "Reasoning > Coding decoding > Box type coding and decoding": {
        "subject": "Reasoning",
        "topic": "Coding decoding",
        "subtopic": "Box type coding and decoding"
    },
    "Reasoning > Direction > Normal": {
        "subject": "Reasoning",
        "topic": "Direction",
        "subtopic": "Normal"
    },
    "Reasoning > Direction > Coded direction": {
        "subject": "Reasoning",
        "topic": "Direction",
        "subtopic": "Coded direction"
    },
    "Reasoning > Blood relation > Normal": {
        "subject": "Reasoning",
        "topic": "Blood relation",
        "subtopic": "Normal"
    },
    "Reasoning > Blood relation > Coded Blood relation": {
        "subject": "Reasoning",
        "topic": "Blood relation",
        "subtopic": "Coded Blood relation"
    },
    "Reasoning > Alphanumeric Symbol series > Number+Alphabets+Symbol series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Number+Alphabets+Symbol series"
    },
    "Reasoning > Alphanumeric Symbol series > Three/Four letter Word series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Three/Four letter Word series"
    },
    "Reasoning > Alphanumeric Symbol series > Three digit Number Series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Three digit Number Series"
    },
    "Reasoning > Alphanumeric Symbol series > Conditional ANS series": {
        "subject": "Reasoning",
        "topic": "Alphanumeric Symbol series",
        "subtopic": "Conditional ANS series"
    },
    "Reasoning > Syllogism > Direct": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Direct"
    },
    "Reasoning > Syllogism > Coded": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Coded"
    },
    "Reasoning > Syllogism > Reverse": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Reverse"
    },
    "Reasoning > Inequality > Direct": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Direct"
    },
    "Reasoning > Inequality > Coded": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Coded"
    },
    "Reasoning > Inequality > Reverse": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Reverse"
    },
    "Reasoning > Inequality > Missing inequality": {
        "subject": "Reasoning",
        "topic": "Inequality",
        "subtopic": "Missing inequality"
    },
    "Reasoning > Miscellaneous > Order and Ranking": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Order and Ranking"
    },
    "Reasoning > Miscellaneous > Number operation": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Number operation"
    },
    "Reasoning > Miscellaneous > Alphabet operation": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Alphabet operation"
    },
    "Reasoning > Miscellaneous > Pairs of letters": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Pairs of letters"
    },
    "Reasoning > Miscellaneous > Pairs of words": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Pairs of words"
    },
    "Reasoning > Miscellaneous > Meaningful word": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Meaningful word"
    },
    "Reasoning > Miscellaneous > Missing series": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Missing series"
    },
    "Reasoning > Miscellaneous > Odd one out": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Odd one out"
    },
    "Reasoning > Miscellaneous > Next series": {
        "subject": "Reasoning",
        "topic": "Miscellaneous",
        "subtopic": "Next series"
    },
    "Reasoning > Critical Reasoning > Statements and Arguments": {
        "subject": "Reasoning",
        "topic": "Critical Reasoning",
        "subtopic": "Statements and Arguments"
    },
    "Reasoning > Critical Reasoning > Cause and Effect": {
        "subject": "Reasoning",
        "topic": "Critical Reasoning",
        "subtopic": "Cause and Effect"
    },
    "Reasoning > Critical Reasoning > Statements and Assumption": {
        "subject": "Reasoning",
        "topic": "Critical Reasoning",
        "subtopic": "Statements and Assumption"
    },
    "Reasoning > Critical Reasoning > Statements and Course of Action": {
        "subject": "Reasoning",
        "topic": "Critical Reasoning",
        "subtopic": "Statements and Course of Action"
    },
    "Reasoning > Critical Reasoning > Statements and Conclusion": {
        "subject": "Reasoning",
        "topic": "Critical Reasoning",
        "subtopic": "Statements and Conclusion"
    },
    "Reasoning > Critical Reasoning > Statements and inferences": {
        "subject": "Reasoning",
        "topic": "Critical Reasoning",
        "subtopic": "Statements and inferences"
    },
    "Reasoning > Sequential Output Tracing > Numbers": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Numbers"
    },
    "Reasoning > Sequential Output Tracing > Words": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Words"
    },
    "Reasoning > Sequential Output Tracing > Numbers and words": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Numbers and words"
    },
    "Reasoning > Sequential Output Tracing > Box type": {
        "subject": "Reasoning",
        "topic": "Sequential Output Tracing",
        "subtopic": "Box type"
    },
    "Reasoning > Statements - Data Sufficiency > 2 statements": {
        "subject": "Reasoning",
        "topic": "Statements - Data Sufficiency",
        "subtopic": "2 statements"
    },
    "Reasoning > Statements - Data Sufficiency > 3 Statements": {
        "subject": "Reasoning",
        "topic": "Statements - Data Sufficiency",
        "subtopic": "3 Statements"
    },
    "Aptitude > Single Graph DI > DI Line": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Line"
    },
    "Aptitude > Single Graph DI > DI Bar": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Bar"
    },
    "Aptitude > Single Graph DI > DI Table": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Table"
    },
    "Aptitude > Single Graph DI > DI Pie": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Pie"
    },
    "Aptitude > Single Graph DI > DI Missing": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Missing"
    },
    "Aptitude > Single Graph DI > DI Radar": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Radar"
    },
    "Aptitude > Single Graph DI > DI Funnel": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Funnel"
    },
    "Aptitude > Single Graph DI > DI Candle stick": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Candle stick"
    },
    "Aptitude > Single Graph DI > DI Caselet": {
        "subject": "Aptitude",
        "topic": "Single Graph DI",
        "subtopic": "DI Caselet"
    },
    "Aptitude > Mixed DI > DI Table + Pie": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Table + Pie"
    },
    "Aptitude > Mixed DI > DI Table + Bar": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Table + Bar"
    },
    "Aptitude > Mixed DI > DI Table + Line": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Table + Line"
    },
    "Aptitude > Mixed DI > Double Pie DI": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "Double Pie DI"
    },
    "Aptitude > Mixed DI > Double Bar DI": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "Double Bar DI"
    },
    "Aptitude > Mixed DI > Double Line DI": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "Double Line DI"
    },
    "Aptitude > Mixed DI > DI Pie + Line": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Pie + Line"
    },
    "Aptitude > Mixed DI > DI Pie + Bar": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Pie + Bar"
    },
    "Aptitude > Mixed DI > DI line + Bar": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI line + Bar"
    },
    "Aptitude > Mixed DI > DI Graph with Note": {
        "subject": "Aptitude",
        "topic": "Mixed DI",
        "subtopic": "DI Graph with Note"
    },
    "Aptitude > Application DI > Arithematic question based DI": {
        "subject": "Aptitude",
        "topic": "Application DI",
        "subtopic": "Arithematic question based DI"
    },
    "Aptitude > Missing Number > Single series": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Single series"
    },
    "Aptitude > Missing Number > Double series with statement": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Double series with statement"
    },
    "Aptitude > Missing Number > Triple series with statement": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Triple series with statement"
    },
    "Aptitude > Missing Number > Single series with Quadratic equation": {
        "subject": "Aptitude",
        "topic": "Missing Number",
        "subtopic": "Single series with Quadratic equation"
    },
    "Aptitude > Wrong Number > Single series": {
        "subject": "Aptitude",
        "topic": "Wrong Number",
        "subtopic": "Single series"
    },
    "Aptitude > Wrong Number > Double series with statement": {
        "subject": "Aptitude",
        "topic": "Wrong Number",
        "subtopic": "Double series with statement"
    },
    "Aptitude > Wrong Number > Triple series with statement": {
        "subject": "Aptitude",
        "topic": "Wrong Number",
        "subtopic": "Triple series with statement"
    },
    "Aptitude > Quadratic Equation > Linear Equation": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Linear Equation"
    },
    "Aptitude > Quadratic Equation > Quadratic Equation with Coefficient": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Quadratic Equation with Coefficient"
    },
    "Aptitude > Quadratic Equation > Quadratic Equation with out Coefficient": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Quadratic Equation with out Coefficient"
    },
    "Aptitude > Quadratic Equation > New pattern QE": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "New pattern QE"
    },
    "Aptitude > Quadratic Equation > Simplification": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Simplification"
    },
    "Aptitude > Quadratic Equation > Approximation": {
        "subject": "Aptitude",
        "topic": "Quadratic Equation",
        "subtopic": "Approximation"
    },
    "Aptitude > Quantity Comparison > Quantity I & II (All Arithmetic topic)": {
        "subject": "Aptitude",
        "topic": "Quantity Comparison",
        "subtopic": "Quantity I & II (All Arithmetic topic)"
    },
    "Aptitude > Data sufficiency > 2 statement (All Arithmetic topic)": {
        "subject": "Aptitude",
        "topic": "Data sufficiency",
        "subtopic": "2 statement (All Arithmetic topic)"
    },
    "Aptitude > Data sufficiency > 3 Statement (All Arithmetic topic)": {
        "subject": "Aptitude",
        "topic": "Data sufficiency",
        "subtopic": "3 Statement (All Arithmetic topic)"
    },
    "Aptitude > Ratio Proportion > Statement Question": {
        "subject": "Aptitude",
        "topic": "Ratio Proportion",
        "subtopic": "Statement Question"
    },
    "Aptitude > Ratio Proportion > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Ratio Proportion",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Ratio Proportion > Double filler question": {
        "subject": "Aptitude",
        "topic": "Ratio Proportion",
        "subtopic": "Double filler question"
    },
    "Aptitude > Average > Statement Question": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Statement Question"
    },
    "Aptitude > Average > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Average > Double filler question": {
        "subject": "Aptitude",
        "topic": "Average",
        "subtopic": "Double filler question"
    },
    "Aptitude > Percentage > Statement Question": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Statement Question"
    },
    "Aptitude > Percentage > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Percentage > Double filler question": {
        "subject": "Aptitude",
        "topic": "Percentage",
        "subtopic": "Double filler question"
    },
    "Aptitude > Ages > Statement Question": {
        "subject": "Aptitude",
        "topic": "Ages",
        "subtopic": "Statement Question"
    },
    "Aptitude > Ages > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Ages",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Ages > Double filler question": {
        "subject": "Aptitude",
        "topic": "Ages",
        "subtopic": "Double filler question"
    },
    "Aptitude > Partnership > Statement Question": {
        "subject": "Aptitude",
        "topic": "Partnership",
        "subtopic": "Statement Question"
    },
    "Aptitude > Partnership > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Partnership",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Partnership > Double filler question": {
        "subject": "Aptitude",
        "topic": "Partnership",
        "subtopic": "Double filler question"
    },
    "Aptitude > Profit & Loss > Statement Question": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Statement Question"
    },
    "Aptitude > Profit & Loss > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Profit & Loss > Double filler question": {
        "subject": "Aptitude",
        "topic": "Profit & Loss",
        "subtopic": "Double filler question"
    },
    "Aptitude > Time Speed Distance > Statement Question": {
        "subject": "Aptitude",
        "topic": "Time Speed Distance",
        "subtopic": "Statement Question"
    },
    "Aptitude > Time Speed Distance > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Time Speed Distance",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Time Speed Distance > Double filler question": {
        "subject": "Aptitude",
        "topic": "Time Speed Distance",
        "subtopic": "Double filler question"
    },
    "Aptitude > Problems on Trains > Statement Question": {
        "subject": "Aptitude",
        "topic": "Problems on Trains",
        "subtopic": "Statement Question"
    },
    "Aptitude > Problems on Trains > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Problems on Trains",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Problems on Trains > Double filler question": {
        "subject": "Aptitude",
        "topic": "Problems on Trains",
        "subtopic": "Double filler question"
    },
    "Aptitude > Boats & Stream > Statement Question": {
        "subject": "Aptitude",
        "topic": "Boats & Stream",
        "subtopic": "Statement Question"
    },
    "Aptitude > Boats & Stream > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Boats & Stream",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Boats & Stream > Double filler question": {
        "subject": "Aptitude",
        "topic": "Boats & Stream",
        "subtopic": "Double filler question"
    },
    "Aptitude > Time & Work > Statement Question": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Statement Question"
    },
    "Aptitude > Time & Work > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Time & Work > Double filler question": {
        "subject": "Aptitude",
        "topic": "Time & Work",
        "subtopic": "Double filler question"
    },
    "Aptitude > Pipes & Cistern > Statement Question": {
        "subject": "Aptitude",
        "topic": "Pipes & Cistern",
        "subtopic": "Statement Question"
    },
    "Aptitude > Pipes & Cistern > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Pipes & Cistern",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Pipes & Cistern > Double filler question": {
        "subject": "Aptitude",
        "topic": "Pipes & Cistern",
        "subtopic": "Double filler question"
    },
    "Aptitude > Simple Interest > Statement Question": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Statement Question"
    },
    "Aptitude > Simple Interest > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Simple Interest > Double filler question": {
        "subject": "Aptitude",
        "topic": "Simple Interest",
        "subtopic": "Double filler question"
    },
    "Aptitude > Compound Interest > Statement Question": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Statement Question"
    },
    "Aptitude > Compound Interest > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Compound Interest > Double filler question": {
        "subject": "Aptitude",
        "topic": "Compound Interest",
        "subtopic": "Double filler question"
    },
    "Aptitude > Mixture Allegation > Statement Question": {
        "subject": "Aptitude",
        "topic": "Mixture Allegation",
        "subtopic": "Statement Question"
    },
    "Aptitude > Mixture Allegation > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Mixture Allegation",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Mixture Allegation > Double filler question": {
        "subject": "Aptitude",
        "topic": "Mixture Allegation",
        "subtopic": "Double filler question"
    },
    "Aptitude > Permutation & Combination > Statement Question": {
        "subject": "Aptitude",
        "topic": "Permutation & Combination",
        "subtopic": "Statement Question"
    },
    "Aptitude > Permutation & Combination > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Permutation & Combination",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Permutation & Combination > Double filler question": {
        "subject": "Aptitude",
        "topic": "Permutation & Combination",
        "subtopic": "Double filler question"
    },
    "Aptitude > Probability > Statement Question": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Statement Question"
    },
    "Aptitude > Probability > Passage based Question": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Passage based Question"
    },
    "Aptitude > Probability > Double filler question": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Double filler question"
    },
    "English > Reading Comprehension > Analytical passage": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Analytical passage"
    },
    "English > Reading Comprehension > Informative passage": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Informative passage"
    },
    "English > Reading Comprehension > Banking and Economy": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Banking and Economy"
    },
    "English > Reading Comprehension > Story-based passage": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Story-based passage"
    },
    "English > Reading Comprehension > Technology": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Technology"
    },
    "English > Reading Comprehension > Research-based": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Research-based"
    },
    "English > Reading Comprehension > Health and Self-improvement": {
        "subject": "English",
        "topic": "Reading Comprehension",
        "subtopic": "Health and Self-improvement"
    },
    "English > Parajumble > Basic para jumble": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Basic para jumble"
    },
    "English > Parajumble > Para jumble with exclusion or inclusion": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with exclusion or inclusion"
    },
    "English > Parajumble > Para jumble with error spotting": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with error spotting"
    },
    "English > Parajumble > Para jumble with rearrangement": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with rearrangement"
    },
    "English > Parajumble > Para jumble with a blank": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with a blank"
    },
    "English > Parajumble > Para jumble with match the columns": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with match the columns"
    },
    "English > Parajumble > Para jumble with phrasal filler": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with phrasal filler"
    },
    "English > Parajumble > Para jumble with a fixed sentence": {
        "subject": "English",
        "topic": "Parajumble",
        "subtopic": "Para jumble with a fixed sentence"
    },
    "English > Sentence Rearrangement > Rearrangement with four/five parts": {
        "subject": "English",
        "topic": "Sentence Rearrangement",
        "subtopic": "Rearrangement with four/five parts"
    },
    "English > Sentence Rearrangement > Omission of irrelevant part": {
        "subject": "English",
        "topic": "Sentence Rearrangement",
        "subtopic": "Omission of irrelevant part"
    },
    "English > Match the columns > Basic pattern with two or three columns": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Basic pattern with two or three columns"
    },
    "English > Match the columns > Match the column with the connector": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Match the column with the connector"
    },
    "English > Match the columns > Columns with fillers or word swap": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Columns with fillers or word swap"
    },
    "English > Match the columns > Columns with error spotting": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Columns with error spotting"
    },
    "English > Match the columns > Match the column with column fillers": {
        "subject": "English",
        "topic": "Match the columns",
        "subtopic": "Match the column with column fillers"
    },
    "English > Statement based > Para completion": {
        "subject": "English",
        "topic": "Statement based",
        "subtopic": "Para completion"
    },
    "English > Statement based > Paragraph inference or cause": {
        "subject": "English",
        "topic": "Statement based",
        "subtopic": "Paragraph inference or cause"
    },
    "English > Statement based > odd one out from the theme": {
        "subject": "English",
        "topic": "Statement based",
        "subtopic": "odd one out from the theme"
    },
    "English > Error Spotting > Correct sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Correct sentence"
    },
    "English > Error Spotting > Incorrect sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Incorrect sentence"
    },
    "English > Error Spotting > Number of errors in a sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Number of errors in a sentence"
    },
    "English > Error Spotting > Error parts in a sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Error parts in a sentence"
    },
    "English > Error Spotting > Error-free parts in a sentence": {
        "subject": "English",
        "topic": "Error Spotting",
        "subtopic": "Error-free parts in a sentence"
    },
    "English > Phrasal replacement > Phrasal verb replacement": {
        "subject": "English",
        "topic": "Phrasal replacement",
        "subtopic": "Phrasal verb replacement"
    },
    "English > Phrasal replacement > Phrase replacement": {
        "subject": "English",
        "topic": "Phrasal replacement",
        "subtopic": "Phrase replacement"
    },
    "English > Phrasal replacement > Choose the correct meaning of the highlighted phrase": {
        "subject": "English",
        "topic": "Phrasal replacement",
        "subtopic": "Choose the correct meaning of the highlighted phrase"
    },
    "English > Cloze test > Basic type": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Basic type"
    },
    "English > Cloze test > Blanks followed by a synonym": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Blanks followed by a synonym"
    },
    "English > Cloze test > Two or three options for a single blank": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Two or three options for a single blank"
    },
    "English > Cloze test > Inappropriate option for the blank": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Inappropriate option for the blank"
    },
    "English > Cloze test > Blanks to be filled by a phrase or phrasal verb": {
        "subject": "English",
        "topic": "Cloze test",
        "subtopic": "Blanks to be filled by a phrase or phrasal verb"
    },
    "English > Fill in the blanks > Single filler": {
        "subject": "English",
        "topic": "Fill in the blanks",
        "subtopic": "Single filler"
    },
    "English > Fill in the blanks > Double filler": {
        "subject": "English",
        "topic": "Fill in the blanks",
        "subtopic": "Double filler"
    },
    "English > Fill in the blanks > Triple filler": {
        "subject": "English",
        "topic": "Fill in the blanks",
        "subtopic": "Triple filler"
    },
    "English > Word Usage > Usage of words": {
        "subject": "English",
        "topic": "Word Usage",
        "subtopic": "Usage of words"
    },
    "English > Word Swap > Word swap in a sentence": {
        "subject": "English",
        "topic": "Word Swap",
        "subtopic": "Word swap in a sentence"
    },
    "English > Word Swap > Word swap in a passage": {
        "subject": "English",
        "topic": "Word Swap",
        "subtopic": "Word swap in a passage"
    },
    "English > Word Swap > Word swap with inappropriate word": {
        "subject": "English",
        "topic": "Word Swap",
        "subtopic": "Word swap with inappropriate word"
    },
    "English > Mis-spelt > Spelling error": {
        "subject": "English",
        "topic": "Mis-spelt",
        "subtopic": "Spelling error"
    },
    "English > Mis-spelt > Inappropriate words": {
        "subject": "English",
        "topic": "Mis-spelt",
        "subtopic": "Inappropriate words"
    },
    "English > Words > Synonyms": {
        "subject": "English",
        "topic": "Words",
        "subtopic": "Synonyms"
    },
    "English > Words > Antonyms": {
        "subject": "English",
        "topic": "Words",
        "subtopic": "Antonyms"
    },
    "English > Idioms > Meaning of the idioms": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Meaning of the idioms"
    },
    "English > Idioms > Meaning of the phrases": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Meaning of the phrases"
    },
    "English > Idioms > Fillers with Idioms": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Fillers with Idioms"
    },
    "English > Idioms > Fillers with Phrasal verbs": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Fillers with Phrasal verbs"
    },
    "English > Idioms > Similar usage of the Idiom": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Similar usage of the Idiom"
    },
    "English > Idioms > Similar usage of the phrase": {
        "subject": "English",
        "topic": "Idioms",
        "subtopic": "Similar usage of the phrase"
    },
    "English > Connectors/starters > Grammar-based": {
        "subject": "English",
        "topic": "Connectors/starters",
        "subtopic": "Grammar-based"
    },
    "English > Connectors/starters > Context-based": {
        "subject": "English",
        "topic": "Connectors/starters",
        "subtopic": "Context-based"
    },
}


# ===== SSC_RAILWAYS TAXONOMY =====

SSC_RAILWAYS_SUBJECTS: List[str] = [
    "Aptitude",
    "COMPUTER AWARENESS",
    "English",
    "General Studies",
    "Miscellaneous",
    "Reasoning",
]

SSC_RAILWAYS_TRIPLETS: List[str] = [
    "Reasoning > Analogy, odd one out > based on numbers",
    "Reasoning > Analogy, odd one out > based on alphabets",
    "Reasoning > Analogy, odd one out > based on general things",
    "Reasoning > Analogy, odd one out > based on figures",
    "Reasoning > Analogy, odd one out > analogy based questions",
    "Reasoning > Number series > based on sum and difference",
    "Reasoning > Number series > based on double difference",
    "Reasoning > Number series > based on multiplication and division",
    "Reasoning > Number series > based on squares",
    "Reasoning > Number series > based on cubes",
    "Reasoning > Number series > wrong number",
    "Reasoning > Number series > box and other shapes based problems",
    "Reasoning > Number series > Number Rearrangement",
    "Reasoning > alphabet test > Logical Order",
    "Reasoning > alphabet test > alphabet series",
    "Reasoning > alphabet test > alphabet and number series",
    "Reasoning > alphabet test > word formation unscrambbling",
    "Reasoning > alphabet test > dictionary",
    "Reasoning > alphabet test > fillers",
    "Reasoning > alphabet test > Word Rearrangement",
    "Reasoning > coding decoding > letter coding-1",
    "Reasoning > coding decoding > letter coding-2",
    "Reasoning > coding decoding > letter and number coding 1",
    "Reasoning > coding decoding > letter and number coding 2",
    "Reasoning > coding decoding > symbol coding and message coding",
    "Reasoning > coding decoding > substitution coding",
    "Reasoning > mathematical operation > Whether the given equations are correct",
    "Reasoning > mathematical operation > coding decoding based",
    "Reasoning > mathematical operation > Interchanging the signs",
    "Reasoning > mathematical operation > equation balancing",
    "Reasoning > Seating arrangement > Linear Arrangement",
    "Reasoning > Seating arrangement > Double Row Arrangement",
    "Reasoning > Seating arrangement > Circular Seating Arrangement",
    "Reasoning > Seating arrangement > Rectangular Arrangement",
    "Reasoning > Seating arrangement > direction based",
    "Reasoning > Blood relations > Introduction",
    "Reasoning > Blood relations > ssc model questions",
    "Reasoning > Blood relations > morethan 3 person relationship",
    "Reasoning > Blood relations > Coded relations",
    "Reasoning > Ranking > Total number of person given data",
    "Reasoning > Ranking > Rank from left or right",
    "Reasoning > Ranking > number of person btw two pwesons and eather sides of presons",
    "Reasoning > Ranking > rank of a person after inchanging",
    "Reasoning > Ranking > ascending and descending",
    "Reasoning > Direction Sense > Introduction to directions",
    "Reasoning > Direction Sense > finding direction and distance",
    "Reasoning > Direction Sense > distance and direction with refercence to a certain place or person 1",
    "Reasoning > Direction Sense > distance and direction with refercence to a certain place or person 2",
    "Reasoning > Direction Sense > shadow & (upside down) related problems",
    "Reasoning > Direction Sense > angle related problems",
    "Reasoning > Syllogism > Introduction",
    "Reasoning > Syllogism > positive conclusions",
    "Reasoning > Syllogism > negative conclusions",
    "Reasoning > Syllogism > either or",
    "Reasoning > Syllogism > possibility",
    "Reasoning > Venn Diagrams > finding relationship",
    "Reasoning > Venn Diagrams > finding exact region",
    "Reasoning > Assumption or Inference or Conclusion > one statement with two conclusion",
    "Reasoning > Assumption or Inference or Conclusion > more than two statments and conclusion",
    "Reasoning > Assumption or Inference or Conclusion > Cause & Effect",
    "Reasoning > Clock > Introduction to clocks",
    "Reasoning > Clock > angle based",
    "Reasoning > Clock > based on coincidence",
    "Reasoning > Clock > mirror clock",
    "Reasoning > Clock > wrong reading and other problems related to time",
    "Reasoning > Calendar > Introduction",
    "Reasoning > Calendar > Time sequence( lies between )",
    "Reasoning > Calendar > single statement( ex, what is the day on 20th feb 2012)",
    "Reasoning > Calendar > reference statement (ex, if 20th feb 2012 is saturday. what is the day on 13 th march 2021)",
    "Reasoning > miscellaneous > meaningful order",
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > mirror image",
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > water image",
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > triangular paper cutting",
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > circular paper cutting",
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > square & rectangular paper cutting",
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > transparent sheets",
    "Reasoning > Cubes and Dices > constructed and deconstructed (unfolded cubes)",
    "Reasoning > Cubes and Dices > 2 figures",
    "Reasoning > Cubes and Dices > painted cubes",
    "Reasoning > Embedde Figures Matrix & Figure Complition > simple models",
    "Reasoning > Embedde Figures Matrix & Figure Complition > figure series",
    "Reasoning > counting of figues > squares and rectangle",
    "Reasoning > counting of figues > triangle",
    "Reasoning > counting of figues > combination of triangle, squares and rectangle",
    "Reasoning > counting of figues > other shapes",
    "Reasoning > Data sufficiency > triangle -",
    "Reasoning > Statement and Course of action > Statement and Course of action",
    "Aptitude > SIMPLIFICATION > BODMAS",
    "Aptitude > SIMPLIFICATION > FRACTIONS",
    "Aptitude > SIMPLIFICATION > RECURRING FRACTIONS",
    "Aptitude > SIMPLIFICATION > CONTINUED FRACTIONS",
    "Aptitude > SIMPLIFICATION > SPECIAL TYPE MULTIPLES IN FRACTION",
    "Aptitude > SIMPLIFICATION > FORMULA BASED (ALGEBRA)",
    "Aptitude > SIMPLIFICATION > MULTIPLES BASED ON 9'S",
    "Aptitude > SIMPLIFICATION > MISCELLANEOUS",
    "Aptitude > SIMPLIFICATION > LAW OF SURDS & INDICES",
    "Aptitude > SIMPLIFICATION > CONJUGATION",
    "Aptitude > SIMPLIFICATION > COMPARISON OF SURDS (ROOT AND POWER)",
    "Aptitude > SIMPLIFICATION > COMPARISON OF SURDS (ADDITION & SUBTRACTION)",
    "Aptitude > SIMPLIFICATION > SQUARE ROOT OF AN IRRATIONAL NUMBER",
    "Aptitude > SIMPLIFICATION > SQUARE ROOT & CUBE ROOT",
    "Aptitude > SIMPLIFICATION > SPECIAL ROOT ADDITION, SUBTRACTION & MULTIPLICATION SERIES",
    "Aptitude > NUMBER SYSTEM > Types of Numbers",
    "Aptitude > NUMBER SYSTEM > Number of Zeros",
    "Aptitude > NUMBER SYSTEM > Divisibility Rules",
    "Aptitude > NUMBER SYSTEM > Successive Division",
    "Aptitude > NUMBER SYSTEM > Factors",
    "Aptitude > NUMBER SYSTEM > Squares",
    "Aptitude > NUMBER SYSTEM > Cubes",
    "Aptitude > NUMBER SYSTEM > Remainder Theorem",
    "Aptitude > NUMBER SYSTEM > Arithmetic Progression",
    "Aptitude > NUMBER SYSTEM > Geometric Progression",
    "Aptitude > NUMBER SYSTEM > Natural Numbers",
    "Aptitude > NUMBER SYSTEM > Unit Digit",
    "Aptitude > NUMBER SYSTEM > Last Two Digits",
    "Aptitude > HCF LCM > HCF & LCM OF DECIMALS AND FRACTIONS",
    "Aptitude > HCF LCM > HCF USING LONG DIVISION METHOD",
    "Aptitude > HCF LCM > HCF & LCM OF POWERS",
    "Aptitude > HCF LCM > HCF (BASIC, SAME REMAINDER)",
    "Aptitude > HCF LCM > HCF (DIFFERENT REMAINDER , SAME REMAINDER)",
    "Aptitude > HCF LCM > LCM BASICS",
    "Aptitude > HCF LCM > LCM (SAME REMAINDER , DIFFERENT REMAINDER)",
    "Aptitude > HCF LCM > LCM (GREATEST (OR) LEAST 'N' DIGIT NUMBER)",
    "Aptitude > HCF LCM > LCM (EXACTLY DIVISIBLE BY ANOTHER NUMBER)",
    "Aptitude > HCF LCM > RELATION BETWEEN HCF & LCM",
    "Aptitude > HCF LCM > NUMBER OF PAIRS",
    "Aptitude > HCF LCM > APPLICATION SUMS (HCF)",
    "Aptitude > HCF LCM > APPLICATION SUMS (LCM)",
    "Aptitude > AVERAGE > AVERAGE (BASIC) SIMPLE & WEIGHTED",
    "Aptitude > AVERAGE > FINDING AVERAGE OF GIVEN SERIES",
    "Aptitude > AVERAGE > CHANGE IN AVERAGE (ADDED TO ALL NUMBERS)",
    "Aptitude > AVERAGE > FINDING THE MISSING NUMBER / REPEATED NUMBER",
    "Aptitude > AVERAGE > WITHOUT REPLACEMENT",
    "Aptitude > AVERAGE > WITH REPLACEMENT",
    "Aptitude > AVERAGE > ERROR ON MARKS (CORRECTED AVERAGE)",
    "Aptitude > AVERAGE > CRICKET (BASIC)",
    "Aptitude > AVERAGE > BATTING & BOWLING",
    "Aptitude > AVERAGE > AVERAGE EXPENDITURE",
    "Aptitude > AVERAGE > MISCELLANEOUS",
    "Aptitude > RATIO PROPORTION > COMPOUND RATIO",
    "Aptitude > RATIO PROPORTION > PROPORTION PROPERTIES",
    "Aptitude > RATIO PROPORTION > THIRD , FOURTH & MEAN PROPORTION",
    "Aptitude > RATIO PROPORTION > ADDITION / SUBTRACTION NUMBER TO MAKE A PROPORTION",
    "Aptitude > RATIO PROPORTION > BASED ON COINS",
    "Aptitude > RATIO PROPORTION > MIXTURE BASED QUESTIONS",
    "Aptitude > RATIO PROPORTION > IN RATIO LEFT / ADD SOME STUDENT",
    "Aptitude > RATIO PROPORTION > INCOME , EXPENDITURE & SAVING",
    "Aptitude > RATIO PROPORTION > BASED ON PERCENTAGE (I = E + S)",
    "Aptitude > RATIO PROPORTION > BASED ON PREVIOUS YEAR & CURRENT YEAR",
    "Aptitude > RATIO PROPORTION > BASED ON A = B X C , B = A/C, C = A/B",
    "Aptitude > RATIO PROPORTION > BASED ON DIRECT & INVERSELY PROPORTIONAL",
    "Aptitude > RATIO PROPORTION > BASED ON FRACTIONS",
    "Aptitude > RATIO PROPORTION > AGES",
    "Aptitude > RATIO PROPORTION > PARTNERSHIP - BASICS",
    "Aptitude > RATIO PROPORTION > INTRODUCTION - CAPITAL OF PARTNERS ARE INVESTED FOR A DIFFERENT PERIOD OF TIME",
    "Aptitude > RATIO PROPORTION > CAPITAL OF PARTNERS ARE INVESTED FOR A DIFFERENT PERIOD OF TIME",
    "Aptitude > RATIO PROPORTION > WORKING ON SLEEPING PARTNERS",
    "Aptitude > RATIO PROPORTION > MISCELLANENOUS - BASED ON PREVIOUS SUMS",
    "Aptitude > MIXTURE ALLIGATION > Alligation",
    "Aptitude > MIXTURE ALLIGATION > BASED ON MIXTURE SELLING AT PROFIT",
    "Aptitude > MIXTURE ALLIGATION > BASED ON AVERAGE CONCEPT",
    "Aptitude > MIXTURE ALLIGATION > BASED ON THREE VARIABLES (ALLIGATIONS)",
    "Aptitude > MIXTURE ALLIGATION > BASED ON PROFIT PERCENTAGE & TIME , SPEED & DISTANCE",
    "Aptitude > MIXTURE ALLIGATION > BASED ON AMOUNT=VALUEX NUMBER OF PERSONS",
    "Aptitude > MIXTURE ALLIGATION > QUESTIONS RELATED TO OTHER TOPICS PERCENTAGE, SIMPLE INTEREST, ZOO (ANIMAL BASED QUESTIONS) AND INCOME , EXPENDITURE AND SAVINGS",
    "Aptitude > MIXTURE ALLIGATION > ADD OR REMOVAL OF SOME QUANTITY",
    "Aptitude > MIXTURE ALLIGATION > REMOVE MIXTURE AND ADD SAME OR DIFFERENT QUANTITIES OF EITHER OF THESE SOLUTIONS",
    "Aptitude > MIXTURE ALLIGATION > ALLEGATIONS BASED MIXTURE QUESTIONS",
    "Aptitude > MIXTURE ALLIGATION > REPEATED PROCESS OF REMOVAL AND ADDITION",
    "Aptitude > MIXTURE ALLIGATION > FIND RATIO OF REPEATED PROCESS ARE GIVEN",
    "Aptitude > MIXTURE ALLIGATION > MIXTURE OF TWO THINGS SAME QUANTITY",
    "Aptitude > MIXTURE ALLIGATION > MXITURE OF TWO THINGS DIFFERENT QUANTITIES",
    "Aptitude > PERCENTAGE > Percentage to Fraction",
    "Aptitude > PERCENTAGE > Basic Problems",
    "Aptitude > PERCENTAGE > Comparing 2 Values",
    "Aptitude > PERCENTAGE > Price & Consumption",
    "Aptitude > PERCENTAGE > Price,Consumption & Quantity",
    "Aptitude > PERCENTAGE > Comparison of Numbers",
    "Aptitude > PERCENTAGE > Net Percent Change",
    "Aptitude > PERCENTAGE > Examination",
    "Aptitude > PERCENTAGE > Income, Expenditure & Savings",
    "Aptitude > PERCENTAGE > Price & Population & Depreciation",
    "Aptitude > PERCENTAGE > Election",
    "Aptitude > PERCENTAGE > Venn Diagram",
    "Aptitude > PERCENTAGE > Questions on Remaining Values",
    "Aptitude > PERCENTAGE > Fresh / Dry Fruit",
    "Aptitude > PERCENTAGE > Income tax & Error %",
    "Aptitude > PROFIT LOSS > PROFIT ON SELLING PRICE",
    "Aptitude > PROFIT LOSS > PROFIT/LOSS ON NUMBER OF ARTICLES",
    "Aptitude > PROFIT LOSS > Variation in Selling Price",
    "Aptitude > PROFIT LOSS > Variation in Cost Price & Selling Price",
    "Aptitude > PROFIT LOSS > Same Cost Price (or) Selling price",
    "Aptitude > PROFIT LOSS > Total Cost Price of Two Articles",
    "Aptitude > PROFIT LOSS > PARTIAL SELLING",
    "Aptitude > PROFIT LOSS > Rotation among Different Sellers",
    "Aptitude > PROFIT LOSS > Ratio between Profit & Loss",
    "Aptitude > PROFIT LOSS > Successive Discount",
    "Aptitude > PROFIT LOSS > Cost Price Marked Price & Selling Price",
    "Aptitude > PROFIT LOSS > Dishonest Seller",
    "Aptitude > PROFIT LOSS > Profit by Alligation",
    "Aptitude > PROFIT LOSS > Miscellaneous Questions",
    "Aptitude > SIMPLE INTEREST > Basic Question",
    "Aptitude > SIMPLE INTEREST > Finding Principal, Rate & Time",
    "Aptitude > SIMPLE INTEREST > Change in Rate and Time",
    "Aptitude > SIMPLE INTEREST > Based on Ratio",
    "Aptitude > SIMPLE INTEREST > Based on Distribution",
    "Aptitude > SIMPLE INTEREST > Based on Alligation",
    "Aptitude > SIMPLE INTEREST > Installment",
    "Aptitude > SIMPLE INTEREST > Miscellaneous",
    "Aptitude > COMPOUND INTEREST > Basic Questions",
    "Aptitude > COMPOUND INTEREST > Half - Yearly Basis",
    "Aptitude > COMPOUND INTEREST > Quarterly Basis",
    "Aptitude > COMPOUND INTEREST > Half - yearly / Quarterly Basis",
    "Aptitude > COMPOUND INTEREST > Different amounts at the same rate",
    "Aptitude > COMPOUND INTEREST > ‘n’ times of principal",
    "Aptitude > COMPOUND INTEREST > Mixed of SI and CI",
    "Aptitude > COMPOUND INTEREST > Difference between SI and CI",
    "Aptitude > COMPOUND INTEREST > Installment",
    "Aptitude > COMPOUND INTEREST > Miscellaneous",
    "Aptitude > TIME AND WORK > Alternate Days",
    "Aptitude > TIME AND WORK > Wages",
    "Aptitude > TIME AND WORK > Remaining Work or Partial Work",
    "Aptitude > TIME AND WORK > Efficiency",
    "Aptitude > TIME AND WORK > Chain Rule",
    "Aptitude > TIME AND WORK > Miscellaneous",
    "Aptitude > TIME AND WORK > Pipes and Cisterns",
    "Aptitude > TIME AND DISTANCE > USUAL SPEED AND TIME",
    "Aptitude > TIME AND DISTANCE > AVERAGE SPEED",
    "Aptitude > TIME AND DISTANCE > RATIO",
    "Aptitude > TIME AND DISTANCE > RELATIVE SPEED 1",
    "Aptitude > TIME AND DISTANCE > CHANGE IN SPEED 2",
    "Aptitude > TIME AND DISTANCE > MISCELLANEOUS",
    "Aptitude > TIME AND DISTANCE > RACE",
    "Aptitude > TRAIN > BASIC CONCEPT TRAIN",
    "Aptitude > TRAIN > TRAIN THEORY",
    "Aptitude > TRAIN > RELATIVE SPEED QUESTION",
    "Aptitude > TRAIN > SPEED RATIO`S",
    "Aptitude > TRAIN > PROBLEMS ON DIRECTION",
    "Aptitude > BOAT & STREAMS > Boats & Streams",
    "Aptitude > BOAT & STREAMS > Boats & Streams QUESTIONS",
    "Aptitude > BOAT & STREAMS > EQUATION BASED PROBLEMS",
    "Aptitude > BOAT & STREAMS > DOWNSTREAM AS MUCH AS UPSTREAMEQUAITON BASED PROBLEMS",
    "Aptitude > DATA INTERPRETATION > Pie-chart",
    "Aptitude > DATA INTERPRETATION > Line Graph",
    "Aptitude > DATA INTERPRETATION > Simple Bar",
    "Aptitude > DATA INTERPRETATION > Horizontal and Divide Bar",
    "Aptitude > DATA INTERPRETATION > Multi Bar",
    "Aptitude > DATA INTERPRETATION > Histogram",
    "Aptitude > DATA INTERPRETATION > Table Chart",
    "Aptitude > DATA INTERPRETATION > Miscellaneous - 1",
    "Aptitude > ALGEBRA > Polynomials",
    "Aptitude > ALGEBRA > Linear equation in 2 variables",
    "Aptitude > ALGEBRA > Solubility of Linear Equation",
    "Aptitude > ALGEBRA > Linear Equation in 3 Variables",
    "Aptitude > ALGEBRA > Roots of Quadratic Equation",
    "Aptitude > ALGEBRA > Problems on Roots of Quadratic Equation",
    "Aptitude > ALGEBRA > Max & Min of Quadratic expression",
    "Aptitude > ALGEBRA > Maximum & Minimum Value",
    "Aptitude > ALGEBRA > Roots of Cubic Equation",
    "Aptitude > ALGEBRA > Factors & Remainders",
    "Aptitude > ALGEBRA > Algebraic Identities",
    "Aptitude > ALGEBRA > Squares",
    "Aptitude > ALGEBRA > Cube",
    "Aptitude > ALGEBRA > Square Root & Cube Root",
    "Aptitude > ALGEBRA > Special Formula Part",
    "Aptitude > ALGEBRA > Sum of squares = 0",
    "Aptitude > ALGEBRA > Inverse Functions - 1",
    "Aptitude > ALGEBRA > Reverse order - 1",
    "Aptitude > ALGEBRA > Special Stats - 1",
    "Aptitude > ALGEBRA > Symmetric - 2",
    "Aptitude > ALGEBRA > Symmetric equation",
    "Aptitude > ALGEBRA > Value Putting - 1",
    "Aptitude > ALGEBRA > Square Root of Irrational Numbers",
    "Aptitude > ALGEBRA > Componendo - Dividendo",
    "Aptitude > GEOMETRY > Types of Angles",
    "Aptitude > GEOMETRY > Lines & angles concepts",
    "Aptitude > GEOMETRY > Triangles-Properties of a triangle",
    "Aptitude > GEOMETRY > Triangles-Exterior angle property",
    "Aptitude > GEOMETRY > Triangles-basic question",
    "Aptitude > GEOMETRY > Condition for formation of a triangle",
    "Aptitude > GEOMETRY > Sine Rule",
    "Aptitude > GEOMETRY > Triangles-Stewart’s Theorem",
    "Aptitude > GEOMETRY > Triangles-Internal bisector",
    "Aptitude > GEOMETRY > Types of triangle",
    "Aptitude > GEOMETRY > Isosceles Triangle",
    "Aptitude > GEOMETRY > Equilateral Triangle",
    "Aptitude > GEOMETRY > Triangles-On the basis of angles",
    "Aptitude > GEOMETRY > Congruent Triangle",
    "Aptitude > GEOMETRY > Triangles-Similarality",
    "Aptitude > GEOMETRY > Similarity of right angle triangle",
    "Aptitude > GEOMETRY > Basic Proportionality Theorem",
    "Aptitude > GEOMETRY > Centers of Triangle",
    "Aptitude > GEOMETRY > Median Property",
    "Aptitude > GEOMETRY > Apollonius's Theorem",
    "Aptitude > GEOMETRY > Median in a Right-Angled Triangle",
    "Aptitude > GEOMETRY > Incentre",
    "Aptitude > GEOMETRY > Inradius",
    "Aptitude > GEOMETRY > Ex-Circle",
    "Aptitude > GEOMETRY > Circumcenter",
    "Aptitude > GEOMETRY > Circumcentre in Triangles",
    "Aptitude > GEOMETRY > Circumcentre in Right Angle Triangle",
    "Aptitude > GEOMETRY > Orthocentre",
    "Aptitude > GEOMETRY > Orthocentre-Height and Side Ratio",
    "Aptitude > GEOMETRY > Orthocenter-Altitude in Terms of the Sides",
    "Aptitude > GEOMETRY > Interior Angle Bisector Theorem",
    "Aptitude > GEOMETRY > Interior Angle Bisector Theorem-Length of Angle Bisector",
    "Aptitude > GEOMETRY > Length of Angle Bisector",
    "Aptitude > GEOMETRY > Mass Point Geometry",
    "Aptitude > GEOMETRY > Circle-Intro",
    "Aptitude > GEOMETRY > Circle-Chord",
    "Aptitude > GEOMETRY > Circles-Property",
    "Aptitude > GEOMETRY > Circles-basic qustion",
    "Aptitude > GEOMETRY > Circles-two chords",
    "Aptitude > GEOMETRY > Circles-Secants intersect",
    "Aptitude > GEOMETRY > Circles-Secants & Tagent",
    "Aptitude > GEOMETRY > Circles-Length of the chord",
    "Aptitude > GEOMETRY > Circles-Two parallel chords",
    "Aptitude > GEOMETRY > Circles-Tangent",
    "Aptitude > GEOMETRY > Circles-Alternate Segment Theorem",
    "Aptitude > GEOMETRY > Circles-circumscribing a circle",
    "Aptitude > GEOMETRY > Circle-Touch Externally",
    "Aptitude > GEOMETRY > Circle-Intersect each other",
    "Aptitude > GEOMETRY > Circle-Intersecting Circles",
    "Aptitude > GEOMETRY > Circle-Concentric Circles",
    "Aptitude > GEOMETRY > Circle-three circle with radii",
    "Aptitude > GEOMETRY > Direct Common Tangent",
    "Aptitude > GEOMETRY > Transverse Common Tangent",
    "Aptitude > GEOMETRY > Circle- two circle intersecting internally",
    "Aptitude > GEOMETRY > Cyclic Quadrilateral",
    "Aptitude > GEOMETRY > Area of Cyclic Quadrilateral",
    "Aptitude > GEOMETRY > Quadrilateral",
    "Aptitude > GEOMETRY > Quadrilateral-Types",
    "Aptitude > GEOMETRY > Parallelogram",
    "Aptitude > GEOMETRY > Rectangle",
    "Aptitude > GEOMETRY > Square",
    "Aptitude > GEOMETRY > Rhombus",
    "Aptitude > GEOMETRY > Trapezium",
    "Aptitude > GEOMETRY > Polygon",
    "Aptitude > GEOMETRY > Angles of polygon",
    "Aptitude > GEOMETRY > Area of Regular Polygon",
    "Aptitude > GEOMETRY > Hexagon",
    "Aptitude > GEOMETRY > Hexagon-Equal Divisions of Area",
    "Aptitude > GEOMETRY > Hexagon-Basic Question",
    "Aptitude > GEOMETRY > Octagon",
    "Aptitude > COORDINATE GEOMETRY > Distance between Two Points",
    "Aptitude > COORDINATE GEOMETRY > Section of a Line",
    "Aptitude > COORDINATE GEOMETRY > Slope of a Line",
    "Aptitude > COORDINATE GEOMETRY > Angle between Two Lines",
    "Aptitude > COORDINATE GEOMETRY > Equation of lines",
    "Aptitude > COORDINATE GEOMETRY > Distance of a Point from a Line",
    "Aptitude > COORDINATE GEOMETRY > Distance between Parallel Lines",
    "Aptitude > COORDINATE GEOMETRY > Reflection of a Point",
    "Aptitude > MENSURATION > Polygons",
    "Aptitude > MENSURATION > Triangles",
    "Aptitude > MENSURATION > Classification of Triangles",
    "Aptitude > MENSURATION > Area and Perimeter of Triangle",
    "Aptitude > MENSURATION > Area of cyclic Quadrilateral",
    "Aptitude > MENSURATION > Square",
    "Aptitude > MENSURATION > Rectangle",
    "Aptitude > MENSURATION > Rhombus",
    "Aptitude > MENSURATION > Parallelogram",
    "Aptitude > MENSURATION > Trapezium",
    "Aptitude > MENSURATION > Hexagon",
    "Aptitude > MENSURATION > Octagon",
    "Aptitude > MENSURATION > Circle",
    "Aptitude > MENSURATION > Ratio of Radius, Perimeter & Area of Circle",
    "Aptitude > MENSURATION > Circular Ring",
    "Aptitude > MENSURATION > Area and Perimeter of Semi Circle & Quarter Circle",
    "Aptitude > MENSURATION > Sector of a Circle",
    "Aptitude > MENSURATION > Square and Circle",
    "Aptitude > MENSURATION > Triangles & Circles",
    "Aptitude > MENSURATION > Square,Rectangle & Triangle",
    "Aptitude > MENSURATION > Same perimeter",
    "Aptitude > MENSURATION > Rectangle path",
    "Aptitude > MENSURATION > Cost based on Area & Perimeter",
    "Aptitude > MENSURATION > Band Around Circles",
    "Aptitude > MENSURATION > Prism",
    "Aptitude > MENSURATION > Cube",
    "Aptitude > MENSURATION > Cuboid",
    "Aptitude > MENSURATION > Right Circular Cylinder",
    "Aptitude > MENSURATION > Pyramid",
    "Aptitude > MENSURATION > Cone",
    "Aptitude > MENSURATION > Frustom of a Cone",
    "Aptitude > MENSURATION > Ratio of Volume of Pyramid",
    "Aptitude > MENSURATION > Sphere",
    "Aptitude > MENSURATION > Hollow Sphere",
    "Aptitude > MENSURATION > Hemisphere",
    "Aptitude > MENSURATION > Relation between Volumes of Cylinder, Cone and Hemisphere",
    "Aptitude > MENSURATION > Conversion of Solids from One Form to Another",
    "Aptitude > MENSURATION > Area or Volume after Removal of Solids",
    "Aptitude > MENSURATION > Volume of Water Flowing from a Pipe",
    "Aptitude > MENSURATION > Useful Results",
    "Aptitude > MENSURATION > One Figure inside Another",
    "Aptitude > MENSURATION > Figure Based Questions",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Trigonometry circular measure of angles",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Circular system",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Basic Identities of trigonometry",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Trigonometric Ratios of some specific angles",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Quadrant System",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > basic question",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Sum of two angles (𝛼+𝛽)=90",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Basic identities",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Based on putting value",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > x+1/x=2",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Basic identity (compound angles)",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Maximum & minimum value of trigonometrix",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > HEIGHT & DISTANCE-basic concept",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Based on Angle Changed",
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > HEIGHT & DISTANCE-Complementary Angle",
    "Aptitude > Probability > Probability",
    "Aptitude > Statistics > Class intervals , Frequency",
    "Aptitude > Statistics > Mean,Mode,Median",
    "English > NOUN > Noun",
    "English > NOUN > Types of Nouns",
    "English > NOUN > Countable and Uncountable",
    "English > NOUN > Rules Based on Numbers",
    "English > NOUN > Based on Gender",
    "English > NOUN > Based On Noun - Case",
    "English > NOUN > Confusing Words",
    "English > NOUN > Find the Correct One",
    "English > PRONOUN > Pronoun",
    "English > PRONOUN > Rules Based on Possessive Pronoun",
    "English > PRONOUN > Relative Pronoun",
    "English > PRONOUN > Reciprocal Pronoun",
    "English > PRONOUN > Pronoun Workout",
    "English > VERB > Forms of Verb",
    "English > VERB > Regular Verbs",
    "English > VERB > Modal verbs",
    "English > VERB > Rules Based on Verbs",
    "English > ADVERB > Adverb-Intro",
    "English > ADVERB > Adverb of Place",
    "English > ADVERB > Rules for Adverb",
    "English > ADVERB > workouts",
    "English > Adjectives > Adjectives-Intro",
    "English > Adjectives > Distributive Adjectives",
    "English > Adjectives > Rules - Degrees of Comparison",
    "English > SUBJECT VERB AGREEMENT > Introduction",
    "English > SUBJECT VERB AGREEMENT > Rule 1-5",
    "English > SUBJECT VERB AGREEMENT > Rule 06-12",
    "English > SUBJECT VERB AGREEMENT > Rule 13-19",
    "English > SUBJECT VERB AGREEMENT > Rule 20-24",
    "English > SUBJECT VERB AGREEMENT > Rule 25-28",
    "English > SUBJECT VERB AGREEMENT > Sentence Improvement & Error Spotting",
    "English > ARTICLES > ARTICLES-Intro",
    "English > ARTICLES > ARTICLES-Use of a/an",
    "English > ARTICLES > ARTICLES-Use of The",
    "English > ARTICLES > Omission",
    "English > ARTICLES > Excersice",
    "English > CONJUNCTION > Co-ordinating Conjunctions",
    "English > CONJUNCTION > Subordinating Conjunction",
    "English > CONJUNCTION > Subordinating conjunctions & Correlative conjunctions",
    "English > CONJUNCTION > Rules",
    "English > SPEECH > Introduction and Sentence types",
    "English > SPEECH > Change of Persons",
    "English > SPEECH > Change of Time",
    "English > SPEECH > Change of Time-Type 2",
    "English > SPEECH > Other Parts of Speech and Assertive Sentence",
    "English > SPEECH > Interrogative Sentence",
    "English > SPEECH > Imperative",
    "English > SPEECH > Optative and Exclamatory Sentences",
    "English > SPEECH > Previous year Question",
    "English > SPEECH > Revision",
    "English > Voice > Introduction",
    "English > Voice > 5 Rules",
    "English > Voice > Passive Formation of the Types of Tenses",
    "English > Voice > Continous tense",
    "English > Voice > Perfect tense",
    "English > Voice > Modal auxillary verb",
    "English > Voice > Imperative",
    "English > Voice > Interrogative-I",
    "English > Voice > Prepositions",
    "English > Voice > Miscellaneous",
    "English > Voice > Excersice",
    "English > READING COMPREHENSION > Questions",
    "English > CLOZE TEST > CLOZE TEST",
    "English > VOCABULARY > SYNONYMS",
    "English > VOCABULARY > ANTONYMS",
    "English > ONE WORD SUBSTITUTION > ONE WORD SUBSTITUTION-1(UNDERLINED)",
    "English > ONE WORD SUBSTITUTION > ONE WORD SUBSTITUTION-2",
    "English > IDIOMS PHRASES > Basic",
    "English > IDIOMS PHRASES > Idiom-based on weather",
    "English > IDIOMS PHRASES > Idiom-based on colour",
    "English > IDIOMS PHRASES > Idiom-based on body parts",
    "English > IDIOMS PHRASES > Idiom-based on numbers",
    "English > IDIOMS PHRASES > Phrasal Verbs",
    "English > QUESTION TAG > Introduction",
    "English > QUESTION TAG > Rules 1-5",
    "English > QUESTION TAG > Rules 6-11",
    "English > QUESTION TAG > Excersice",
    "English > CONDITIONAL CLAUSES > Introduction-Zero and first",
    "English > CONDITIONAL CLAUSES > Second & three Conditional",
    "English > CONDITIONAL CLAUSES > Mixed and Unless",
    "English > CONDITIONAL CLAUSES > Spot the Error",
    "General Studies > ANCIENT - History > Prehistoric And Indus Valley",
    "General Studies > ANCIENT - History > Vedic Age",
    "General Studies > ANCIENT - History > Jainism",
    "General Studies > ANCIENT - History > Buddhism",
    "General Studies > ANCIENT - History > Mahajanapadas",
    "General Studies > ANCIENT - History > Mauryan Dynasty",
    "General Studies > ANCIENT - History > Gupta Dynasty",
    "General Studies > ANCIENT - History > Vardhana Dynasty",
    "General Studies > ANCIENT - History > sangam",
    "General Studies > ANCIENT - History > Chola Dynasty",
    "General Studies > ANCIENT - History > Pallavas",
    "General Studies > ANCIENT - History > SAKA ERA",
    "General Studies > ANCIENT - History > Kushanas",
    "General Studies > MEDIVEAL - History > Foreign Invasions",
    "General Studies > MEDIVEAL - History > Delhi Sultanate",
    "General Studies > MEDIVEAL - History > Slave Dynasty",
    "General Studies > MEDIVEAL - History > Khilji Dynasty",
    "General Studies > MEDIVEAL - History > Tughlaq Dynasty",
    "General Studies > MEDIVEAL - History > Sayyid Dynasty",
    "General Studies > MEDIVEAL - History > Lodi Dynasty",
    "General Studies > MEDIVEAL - History > Mughal Period",
    "General Studies > MEDIVEAL - History > Babur",
    "General Studies > MEDIVEAL - History > Humayun and Sher Shah Suri",
    "General Studies > MEDIVEAL - History > Akbar",
    "General Studies > MEDIVEAL - History > Jahangir",
    "General Studies > MEDIVEAL - History > Shah Jahan",
    "General Studies > MEDIVEAL - History > Aurangzeb",
    "General Studies > MEDIVEAL - History > SUFISM",
    "General Studies > MEDIVEAL - History > Sikh Guru",
    "General Studies > MEDIVEAL - History > Maratha Empire",
    "General Studies > MEDIVEAL - History > Vijaynagar Empire",
    "General Studies > MEDIVEAL - History > Wars and Treaties",
    "General Studies > MEDIVEAL - History > Miscellaneous",
    "General Studies > MODERN - History > The Revolt of 1857",
    "General Studies > MODERN - History > Governors and Viceroys",
    "General Studies > MODERN - History > British acts and Policies",
    "General Studies > MODERN - History > Partition of Bengal and Swadeshi Movements",
    "General Studies > MODERN - History > Gandhian Era",
    "General Studies > MODERN - History > Expansion of British Rule",
    "General Studies > MODERN - History > The Revolutionaries",
    "General Studies > MODERN - History > Struggle for Independence",
    "General Studies > MODERN - History > Socio Religious Reforms",
    "General Studies > MODERN - History > Indian National Congress and Its Sessions",
    "General Studies > MODERN - History > Muslim league",
    "General Studies > MODERN - History > LEADERS",
    "General Studies > MODERN - History > Miscellaneous",
    "General Studies > GEOGRAPHY > Solar system and its planets 290 - 293 01 - 44 44",
    "General Studies > GEOGRAPHY > Longitudes and latitudes",
    "General Studies > GEOGRAPHY > Continents and Oceans",
    "General Studies > GEOGRAPHY > Neighbouring Countries of India",
    "General Studies > GEOGRAPHY > Indian Drainage System",
    "General Studies > GEOGRAPHY > World Drainage System",
    "General Studies > GEOGRAPHY > Minerals and Energy Resources in India",
    "General Studies > GEOGRAPHY > Agriculture",
    "General Studies > GEOGRAPHY > Soil",
    "General Studies > GEOGRAPHY > Crops",
    "General Studies > GEOGRAPHY > Vegetation",
    "General Studies > GEOGRAPHY > Climate",
    "General Studies > GEOGRAPHY > Industries",
    "General Studies > GEOGRAPHY > NAP/WLS/Biosphere Reserves/VARIOUS INITIATIVES",
    "General Studies > GEOGRAPHY > Physiographic Division of India",
    "General Studies > GEOGRAPHY > Transportation",
    "General Studies > GEOGRAPHY > Population",
    "General Studies > GEOGRAPHY > Atmosphere",
    "General Studies > GEOGRAPHY > Rocks",
    "General Studies > GEOGRAPHY > Mountain",
    "General Studies > GEOGRAPHY > Volcano",
    "General Studies > GEOGRAPHY > World geography and Map",
    "General Studies > GEOGRAPHY > ENVIRONMENT",
    "General Studies > POLITY > Constitution",
    "General Studies > POLITY > Sources of Indian Constitution",
    "General Studies > POLITY > Article, Schedule, Parts and list",
    "General Studies > POLITY > Amendments",
    "General Studies > POLITY > DPSP",
    "General Studies > POLITY > Fundamental Rights and Duties",
    "General Studies > POLITY > Committee Reports",
    "General Studies > POLITY > Parliament",
    "General Studies > POLITY > President, Vice President and Prime Minister",
    "General Studies > POLITY > Judiciary",
    "General Studies > POLITY > Government Bodies",
    "General Studies > POLITY > Polity of neighbouring countries",
    "General Studies > POLITY > Important Case",
    "General Studies > ECONOMICS > Basics of Economy",
    "General Studies > ECONOMICS > Concepts of Demand and Supply",
    "General Studies > ECONOMICS > Cost, Production, Consumption and Market",
    "General Studies > ECONOMICS > National Income, Inflation, Budget,Taxation and GDP",
    "General Studies > ECONOMICS > Money Banking and Financial Institutions",
    "General Studies > ECONOMICS > Navratna / Maharatna / PSUs",
    "General Studies > ECONOMICS > International Organisations",
    "General Studies > ECONOMICS > Government Schemes",
    "General Studies > ECONOMICS > Five - Year Plans",
    "General Studies > ECONOMICS > LPG",
    "General Studies > ECONOMICS > Indian Economy : Central Problems and Planning",
    "General Studies > ECONOMICS > Stock, Debentures and Foreign trade",
    "General Studies > ECONOMICS > Fiscal Policy and Monetary Policy",
    "General Studies > ECONOMICS > Miscellaneous",
    "General Studies > PHYSICS > Light and Optics",
    "General Studies > PHYSICS > Heat and Thermodynamics",
    "General Studies > PHYSICS > Fluid Mechanics",
    "General Studies > PHYSICS > Electric Current and Its Effects",
    "General Studies > PHYSICS > LAWS",
    "General Studies > PHYSICS > Force and Pressure",
    "General Studies > PHYSICS > Sound",
    "General Studies > PHYSICS > Gravitation",
    "General Studies > PHYSICS > Work and Energy",
    "General Studies > PHYSICS > Wave",
    "General Studies > PHYSICS > Radioactivity",
    "General Studies > PHYSICS > Discoveries",
    "General Studies > PHYSICS > Units and Measurements",
    "General Studies > PHYSICS > Miscellaneous",
    "General Studies > CHEMISTRY > Structure of Atom",
    "General Studies > CHEMISTRY > COMPOUNDS",
    "General Studies > CHEMISTRY > Metals, Non-metals and Alloys",
    "General Studies > CHEMISTRY > Acid, Bases and Salt",
    "General Studies > CHEMISTRY > Metallurgy",
    "General Studies > CHEMISTRY > Organic Chemistry",
    "General Studies > CHEMISTRY > Periodic table",
    "General Studies > CHEMISTRY > Ideal Gas Law",
    "General Studies > CHEMISTRY > Chemical Properties",
    "General Studies > CHEMISTRY > Solutions",
    "General Studies > CHEMISTRY > Chemistry in Everyday life",
    "General Studies > CHEMISTRY > Discoveries",
    "General Studies > CHEMISTRY > Common Name",
    "General Studies > CHEMISTRY > Miscellaneous",
    "General Studies > BIOLOGY > Scientific Name",
    "General Studies > BIOLOGY > Nutrition in Animals",
    "General Studies > BIOLOGY > Nutrition in plants",
    "General Studies > BIOLOGY > Deficiency and Diseases",
    "General Studies > BIOLOGY > Reproduction in Animals",
    "General Studies > BIOLOGY > Reproduction in Plants",
    "General Studies > BIOLOGY > Cell: Basic Unit of life",
    "General Studies > BIOLOGY > Sensory Organs",
    "General Studies > BIOLOGY > Circulatory System",
    "General Studies > BIOLOGY > Excretory System",
    "General Studies > BIOLOGY > Endocrine/Exocrine system",
    "General Studies > BIOLOGY > Respiratory system",
    "General Studies > BIOLOGY > Digestive system",
    "General Studies > BIOLOGY > Nervous system",
    "General Studies > BIOLOGY > Skeleton system",
    "General Studies > BIOLOGY > Plant Kingdom",
    "General Studies > BIOLOGY > Animal Kingdom",
    "General Studies > BIOLOGY > Micro organism",
    "General Studies > BIOLOGY > Enzymes and Hormones",
    "General Studies > BIOLOGY > Discoveries and vaccines",
    "General Studies > BIOLOGY > Scientific Study",
    "General Studies > BIOLOGY > Miscellaneous",
    "COMPUTER AWARENESS > Computer Basics > Organization of a computer",
    "COMPUTER AWARENESS > Computer Basics > Central Processing Unit (CPU)",
    "COMPUTER AWARENESS > Computer Basics > Input/Output devices",
    "COMPUTER AWARENESS > Computer Basics > Computer memory",
    "COMPUTER AWARENESS > Computer Basics > Memory organization",
    "COMPUTER AWARENESS > Computer Basics > Backup devices",
    "COMPUTER AWARENESS > Computer Basics > PORTs",
    "COMPUTER AWARENESS > Computer Basics > Windows Explorer",
    "COMPUTER AWARENESS > Computer Basics > Keyboard shortcuts",
    "COMPUTER AWARENESS > Software > Windows Operating System",
    "COMPUTER AWARENESS > Software > Basics of Microsoft Office (MS Word, MS Excel, PowerPoint)",
    "COMPUTER AWARENESS > Working with Internet and E-mails > Web Browsing & Searching",
    "COMPUTER AWARENESS > Working with Internet and E-mails > Downloading & Uploading",
    "COMPUTER AWARENESS > Working with Internet and E-mails > Managing an E-mail Account",
    "COMPUTER AWARENESS > Working with Internet and E-mails > e-Banking",
    "COMPUTER AWARENESS > Networking and Cyber Security > Networking devices and protocols",
    "COMPUTER AWARENESS > Networking and Cyber Security > Network and information security threats (hacking, virus, worms, Trojan, etc.)",
    "COMPUTER AWARENESS > Networking and Cyber Security > Preventive measures",
    "Miscellaneous > STATIC GK > IMPORTANT DAYS",
    "Miscellaneous > STATIC GK > Appointments",
    "Miscellaneous > STATIC GK > Places",
    "Miscellaneous > STATIC GK > Arts Personality",
    "Miscellaneous > STATIC GK > HEAD QUARTERS",
    "Miscellaneous > STATIC GK > Arts Awards",
    "Miscellaneous > STATIC GK > Musical Instruments",
    "Miscellaneous > STATIC GK > Festivals",
    "Miscellaneous > STATIC GK > DANCES",
    "Miscellaneous > STATIC GK > Fairs",
    "Miscellaneous > STATIC GK > Songs",
    "Miscellaneous > STATIC GK > Painting/dress/Tribes",
    "Miscellaneous > STATIC GK > First in india/world",
    "Miscellaneous > STATIC GK > Sports",
    "Miscellaneous > STATIC GK > Books and Authors",
    "Miscellaneous > STATIC GK > Famous Personality",
    "Miscellaneous > STATIC GK > States G.K",
    "Miscellaneous > STATIC GK > Organisation",
    "Miscellaneous > STATIC GK > World G.K",
    "Miscellaneous > STATIC GK > Full forms",
    "Miscellaneous > STATIC GK > Religious Place",
    "Miscellaneous > STATIC GK > Awards",
    "Miscellaneous > STATIC GK > Important events",
    "Miscellaneous > STATIC GK > Founders",
    "Miscellaneous > STATIC GK > Schemes",
    "Miscellaneous > STATIC GK > DISCOVERIES",
    "Miscellaneous > STATIC GK > IUCN RED LIST",
    "Miscellaneous > STATIC GK > THEMES",
    "Miscellaneous > STATIC GK > Miscellaneous",
]

SSC_RAILWAYS_TRIPLET_DICT: Dict[str, Dict[str, str]] = {
    "Reasoning > Analogy, odd one out > based on numbers": {
        "subject": "Reasoning",
        "topic": "Analogy, odd one out",
        "subtopic": "based on numbers"
    },
    "Reasoning > Analogy, odd one out > based on alphabets": {
        "subject": "Reasoning",
        "topic": "Analogy, odd one out",
        "subtopic": "based on alphabets"
    },
    "Reasoning > Analogy, odd one out > based on general things": {
        "subject": "Reasoning",
        "topic": "Analogy, odd one out",
        "subtopic": "based on general things"
    },
    "Reasoning > Analogy, odd one out > based on figures": {
        "subject": "Reasoning",
        "topic": "Analogy, odd one out",
        "subtopic": "based on figures"
    },
    "Reasoning > Analogy, odd one out > analogy based questions": {
        "subject": "Reasoning",
        "topic": "Analogy, odd one out",
        "subtopic": "analogy based questions"
    },
    "Reasoning > Number series > based on sum and difference": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "based on sum and difference"
    },
    "Reasoning > Number series > based on double difference": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "based on double difference"
    },
    "Reasoning > Number series > based on multiplication and division": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "based on multiplication and division"
    },
    "Reasoning > Number series > based on squares": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "based on squares"
    },
    "Reasoning > Number series > based on cubes": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "based on cubes"
    },
    "Reasoning > Number series > wrong number": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "wrong number"
    },
    "Reasoning > Number series > box and other shapes based problems": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "box and other shapes based problems"
    },
    "Reasoning > Number series > Number Rearrangement": {
        "subject": "Reasoning",
        "topic": "Number series",
        "subtopic": "Number Rearrangement"
    },
    "Reasoning > alphabet test > Logical Order": {
        "subject": "Reasoning",
        "topic": "alphabet test",
        "subtopic": "Logical Order"
    },
    "Reasoning > alphabet test > alphabet series": {
        "subject": "Reasoning",
        "topic": "alphabet test",
        "subtopic": "alphabet series"
    },
    "Reasoning > alphabet test > alphabet and number series": {
        "subject": "Reasoning",
        "topic": "alphabet test",
        "subtopic": "alphabet and number series"
    },
    "Reasoning > alphabet test > word formation unscrambbling": {
        "subject": "Reasoning",
        "topic": "alphabet test",
        "subtopic": "word formation unscrambbling"
    },
    "Reasoning > alphabet test > dictionary": {
        "subject": "Reasoning",
        "topic": "alphabet test",
        "subtopic": "dictionary"
    },
    "Reasoning > alphabet test > fillers": {
        "subject": "Reasoning",
        "topic": "alphabet test",
        "subtopic": "fillers"
    },
    "Reasoning > alphabet test > Word Rearrangement": {
        "subject": "Reasoning",
        "topic": "alphabet test",
        "subtopic": "Word Rearrangement"
    },
    "Reasoning > coding decoding > letter coding-1": {
        "subject": "Reasoning",
        "topic": "coding decoding",
        "subtopic": "letter coding-1"
    },
    "Reasoning > coding decoding > letter coding-2": {
        "subject": "Reasoning",
        "topic": "coding decoding",
        "subtopic": "letter coding-2"
    },
    "Reasoning > coding decoding > letter and number coding 1": {
        "subject": "Reasoning",
        "topic": "coding decoding",
        "subtopic": "letter and number coding 1"
    },
    "Reasoning > coding decoding > letter and number coding 2": {
        "subject": "Reasoning",
        "topic": "coding decoding",
        "subtopic": "letter and number coding 2"
    },
    "Reasoning > coding decoding > symbol coding and message coding": {
        "subject": "Reasoning",
        "topic": "coding decoding",
        "subtopic": "symbol coding and message coding"
    },
    "Reasoning > coding decoding > substitution coding": {
        "subject": "Reasoning",
        "topic": "coding decoding",
        "subtopic": "substitution coding"
    },
    "Reasoning > mathematical operation > Whether the given equations are correct": {
        "subject": "Reasoning",
        "topic": "mathematical operation",
        "subtopic": "Whether the given equations are correct"
    },
    "Reasoning > mathematical operation > coding decoding based": {
        "subject": "Reasoning",
        "topic": "mathematical operation",
        "subtopic": "coding decoding based"
    },
    "Reasoning > mathematical operation > Interchanging the signs": {
        "subject": "Reasoning",
        "topic": "mathematical operation",
        "subtopic": "Interchanging the signs"
    },
    "Reasoning > mathematical operation > equation balancing": {
        "subject": "Reasoning",
        "topic": "mathematical operation",
        "subtopic": "equation balancing"
    },
    "Reasoning > Seating arrangement > Linear Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating arrangement",
        "subtopic": "Linear Arrangement"
    },
    "Reasoning > Seating arrangement > Double Row Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating arrangement",
        "subtopic": "Double Row Arrangement"
    },
    "Reasoning > Seating arrangement > Circular Seating Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating arrangement",
        "subtopic": "Circular Seating Arrangement"
    },
    "Reasoning > Seating arrangement > Rectangular Arrangement": {
        "subject": "Reasoning",
        "topic": "Seating arrangement",
        "subtopic": "Rectangular Arrangement"
    },
    "Reasoning > Seating arrangement > direction based": {
        "subject": "Reasoning",
        "topic": "Seating arrangement",
        "subtopic": "direction based"
    },
    "Reasoning > Blood relations > Introduction": {
        "subject": "Reasoning",
        "topic": "Blood relations",
        "subtopic": "Introduction"
    },
    "Reasoning > Blood relations > ssc model questions": {
        "subject": "Reasoning",
        "topic": "Blood relations",
        "subtopic": "ssc model questions"
    },
    "Reasoning > Blood relations > morethan 3 person relationship": {
        "subject": "Reasoning",
        "topic": "Blood relations",
        "subtopic": "morethan 3 person relationship"
    },
    "Reasoning > Blood relations > Coded relations": {
        "subject": "Reasoning",
        "topic": "Blood relations",
        "subtopic": "Coded relations"
    },
    "Reasoning > Ranking > Total number of person given data": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "Total number of person given data"
    },
    "Reasoning > Ranking > Rank from left or right": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "Rank from left or right"
    },
    "Reasoning > Ranking > number of person btw two pwesons and eather sides of presons": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "number of person btw two pwesons and eather sides of presons"
    },
    "Reasoning > Ranking > rank of a person after inchanging": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "rank of a person after inchanging"
    },
    "Reasoning > Ranking > ascending and descending": {
        "subject": "Reasoning",
        "topic": "Ranking",
        "subtopic": "ascending and descending"
    },
    "Reasoning > Direction Sense > Introduction to directions": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "Introduction to directions"
    },
    "Reasoning > Direction Sense > finding direction and distance": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "finding direction and distance"
    },
    "Reasoning > Direction Sense > distance and direction with refercence to a certain place or person 1": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "distance and direction with refercence to a certain place or person 1"
    },
    "Reasoning > Direction Sense > distance and direction with refercence to a certain place or person 2": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "distance and direction with refercence to a certain place or person 2"
    },
    "Reasoning > Direction Sense > shadow & (upside down) related problems": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "shadow & (upside down) related problems"
    },
    "Reasoning > Direction Sense > angle related problems": {
        "subject": "Reasoning",
        "topic": "Direction Sense",
        "subtopic": "angle related problems"
    },
    "Reasoning > Syllogism > Introduction": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "Introduction"
    },
    "Reasoning > Syllogism > positive conclusions": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "positive conclusions"
    },
    "Reasoning > Syllogism > negative conclusions": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "negative conclusions"
    },
    "Reasoning > Syllogism > either or": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "either or"
    },
    "Reasoning > Syllogism > possibility": {
        "subject": "Reasoning",
        "topic": "Syllogism",
        "subtopic": "possibility"
    },
    "Reasoning > Venn Diagrams > finding relationship": {
        "subject": "Reasoning",
        "topic": "Venn Diagrams",
        "subtopic": "finding relationship"
    },
    "Reasoning > Venn Diagrams > finding exact region": {
        "subject": "Reasoning",
        "topic": "Venn Diagrams",
        "subtopic": "finding exact region"
    },
    "Reasoning > Assumption or Inference or Conclusion > one statement with two conclusion": {
        "subject": "Reasoning",
        "topic": "Assumption or Inference or Conclusion",
        "subtopic": "one statement with two conclusion"
    },
    "Reasoning > Assumption or Inference or Conclusion > more than two statments and conclusion": {
        "subject": "Reasoning",
        "topic": "Assumption or Inference or Conclusion",
        "subtopic": "more than two statments and conclusion"
    },
    "Reasoning > Assumption or Inference or Conclusion > Cause & Effect": {
        "subject": "Reasoning",
        "topic": "Assumption or Inference or Conclusion",
        "subtopic": "Cause & Effect"
    },
    "Reasoning > Clock > Introduction to clocks": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "Introduction to clocks"
    },
    "Reasoning > Clock > angle based": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "angle based"
    },
    "Reasoning > Clock > based on coincidence": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "based on coincidence"
    },
    "Reasoning > Clock > mirror clock": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "mirror clock"
    },
    "Reasoning > Clock > wrong reading and other problems related to time": {
        "subject": "Reasoning",
        "topic": "Clock",
        "subtopic": "wrong reading and other problems related to time"
    },
    "Reasoning > Calendar > Introduction": {
        "subject": "Reasoning",
        "topic": "Calendar",
        "subtopic": "Introduction"
    },
    "Reasoning > Calendar > Time sequence( lies between )": {
        "subject": "Reasoning",
        "topic": "Calendar",
        "subtopic": "Time sequence( lies between )"
    },
    "Reasoning > Calendar > single statement( ex, what is the day on 20th feb 2012)": {
        "subject": "Reasoning",
        "topic": "Calendar",
        "subtopic": "single statement( ex, what is the day on 20th feb 2012)"
    },
    "Reasoning > Calendar > reference statement (ex, if 20th feb 2012 is saturday. what is the day on 13 th march 2021)": {
        "subject": "Reasoning",
        "topic": "Calendar",
        "subtopic": "reference statement (ex, if 20th feb 2012 is saturday. what is the day on 13 th march 2021)"
    },
    "Reasoning > miscellaneous > meaningful order": {
        "subject": "Reasoning",
        "topic": "miscellaneous",
        "subtopic": "meaningful order"
    },
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > mirror image": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image & Paper Cutting and Folding",
        "subtopic": "mirror image"
    },
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > water image": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image & Paper Cutting and Folding",
        "subtopic": "water image"
    },
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > triangular paper cutting": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image & Paper Cutting and Folding",
        "subtopic": "triangular paper cutting"
    },
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > circular paper cutting": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image & Paper Cutting and Folding",
        "subtopic": "circular paper cutting"
    },
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > square & rectangular paper cutting": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image & Paper Cutting and Folding",
        "subtopic": "square & rectangular paper cutting"
    },
    "Reasoning > Mirror and Water Image & Paper Cutting and Folding > transparent sheets": {
        "subject": "Reasoning",
        "topic": "Mirror and Water Image & Paper Cutting and Folding",
        "subtopic": "transparent sheets"
    },
    "Reasoning > Cubes and Dices > constructed and deconstructed (unfolded cubes)": {
        "subject": "Reasoning",
        "topic": "Cubes and Dices",
        "subtopic": "constructed and deconstructed (unfolded cubes)"
    },
    "Reasoning > Cubes and Dices > 2 figures": {
        "subject": "Reasoning",
        "topic": "Cubes and Dices",
        "subtopic": "2 figures"
    },
    "Reasoning > Cubes and Dices > painted cubes": {
        "subject": "Reasoning",
        "topic": "Cubes and Dices",
        "subtopic": "painted cubes"
    },
    "Reasoning > Embedde Figures Matrix & Figure Complition > simple models": {
        "subject": "Reasoning",
        "topic": "Embedde Figures Matrix & Figure Complition",
        "subtopic": "simple models"
    },
    "Reasoning > Embedde Figures Matrix & Figure Complition > figure series": {
        "subject": "Reasoning",
        "topic": "Embedde Figures Matrix & Figure Complition",
        "subtopic": "figure series"
    },
    "Reasoning > counting of figues > squares and rectangle": {
        "subject": "Reasoning",
        "topic": "counting of figues",
        "subtopic": "squares and rectangle"
    },
    "Reasoning > counting of figues > triangle": {
        "subject": "Reasoning",
        "topic": "counting of figues",
        "subtopic": "triangle"
    },
    "Reasoning > counting of figues > combination of triangle, squares and rectangle": {
        "subject": "Reasoning",
        "topic": "counting of figues",
        "subtopic": "combination of triangle, squares and rectangle"
    },
    "Reasoning > counting of figues > other shapes": {
        "subject": "Reasoning",
        "topic": "counting of figues",
        "subtopic": "other shapes"
    },
    "Reasoning > Data sufficiency > triangle -": {
        "subject": "Reasoning",
        "topic": "Data sufficiency",
        "subtopic": "triangle -"
    },
    "Reasoning > Statement and Course of action > Statement and Course of action": {
        "subject": "Reasoning",
        "topic": "Statement and Course of action",
        "subtopic": "Statement and Course of action"
    },
    "Aptitude > SIMPLIFICATION > BODMAS": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "BODMAS"
    },
    "Aptitude > SIMPLIFICATION > FRACTIONS": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "FRACTIONS"
    },
    "Aptitude > SIMPLIFICATION > RECURRING FRACTIONS": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "RECURRING FRACTIONS"
    },
    "Aptitude > SIMPLIFICATION > CONTINUED FRACTIONS": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "CONTINUED FRACTIONS"
    },
    "Aptitude > SIMPLIFICATION > SPECIAL TYPE MULTIPLES IN FRACTION": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "SPECIAL TYPE MULTIPLES IN FRACTION"
    },
    "Aptitude > SIMPLIFICATION > FORMULA BASED (ALGEBRA)": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "FORMULA BASED (ALGEBRA)"
    },
    "Aptitude > SIMPLIFICATION > MULTIPLES BASED ON 9'S": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "MULTIPLES BASED ON 9'S"
    },
    "Aptitude > SIMPLIFICATION > MISCELLANEOUS": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "MISCELLANEOUS"
    },
    "Aptitude > SIMPLIFICATION > LAW OF SURDS & INDICES": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "LAW OF SURDS & INDICES"
    },
    "Aptitude > SIMPLIFICATION > CONJUGATION": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "CONJUGATION"
    },
    "Aptitude > SIMPLIFICATION > COMPARISON OF SURDS (ROOT AND POWER)": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "COMPARISON OF SURDS (ROOT AND POWER)"
    },
    "Aptitude > SIMPLIFICATION > COMPARISON OF SURDS (ADDITION & SUBTRACTION)": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "COMPARISON OF SURDS (ADDITION & SUBTRACTION)"
    },
    "Aptitude > SIMPLIFICATION > SQUARE ROOT OF AN IRRATIONAL NUMBER": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "SQUARE ROOT OF AN IRRATIONAL NUMBER"
    },
    "Aptitude > SIMPLIFICATION > SQUARE ROOT & CUBE ROOT": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "SQUARE ROOT & CUBE ROOT"
    },
    "Aptitude > SIMPLIFICATION > SPECIAL ROOT ADDITION, SUBTRACTION & MULTIPLICATION SERIES": {
        "subject": "Aptitude",
        "topic": "SIMPLIFICATION",
        "subtopic": "SPECIAL ROOT ADDITION, SUBTRACTION & MULTIPLICATION SERIES"
    },
    "Aptitude > NUMBER SYSTEM > Types of Numbers": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Types of Numbers"
    },
    "Aptitude > NUMBER SYSTEM > Number of Zeros": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Number of Zeros"
    },
    "Aptitude > NUMBER SYSTEM > Divisibility Rules": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Divisibility Rules"
    },
    "Aptitude > NUMBER SYSTEM > Successive Division": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Successive Division"
    },
    "Aptitude > NUMBER SYSTEM > Factors": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Factors"
    },
    "Aptitude > NUMBER SYSTEM > Squares": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Squares"
    },
    "Aptitude > NUMBER SYSTEM > Cubes": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Cubes"
    },
    "Aptitude > NUMBER SYSTEM > Remainder Theorem": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Remainder Theorem"
    },
    "Aptitude > NUMBER SYSTEM > Arithmetic Progression": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Arithmetic Progression"
    },
    "Aptitude > NUMBER SYSTEM > Geometric Progression": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Geometric Progression"
    },
    "Aptitude > NUMBER SYSTEM > Natural Numbers": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Natural Numbers"
    },
    "Aptitude > NUMBER SYSTEM > Unit Digit": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Unit Digit"
    },
    "Aptitude > NUMBER SYSTEM > Last Two Digits": {
        "subject": "Aptitude",
        "topic": "NUMBER SYSTEM",
        "subtopic": "Last Two Digits"
    },
    "Aptitude > HCF LCM > HCF & LCM OF DECIMALS AND FRACTIONS": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "HCF & LCM OF DECIMALS AND FRACTIONS"
    },
    "Aptitude > HCF LCM > HCF USING LONG DIVISION METHOD": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "HCF USING LONG DIVISION METHOD"
    },
    "Aptitude > HCF LCM > HCF & LCM OF POWERS": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "HCF & LCM OF POWERS"
    },
    "Aptitude > HCF LCM > HCF (BASIC, SAME REMAINDER)": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "HCF (BASIC, SAME REMAINDER)"
    },
    "Aptitude > HCF LCM > HCF (DIFFERENT REMAINDER , SAME REMAINDER)": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "HCF (DIFFERENT REMAINDER , SAME REMAINDER)"
    },
    "Aptitude > HCF LCM > LCM BASICS": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "LCM BASICS"
    },
    "Aptitude > HCF LCM > LCM (SAME REMAINDER , DIFFERENT REMAINDER)": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "LCM (SAME REMAINDER , DIFFERENT REMAINDER)"
    },
    "Aptitude > HCF LCM > LCM (GREATEST (OR) LEAST 'N' DIGIT NUMBER)": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "LCM (GREATEST (OR) LEAST 'N' DIGIT NUMBER)"
    },
    "Aptitude > HCF LCM > LCM (EXACTLY DIVISIBLE BY ANOTHER NUMBER)": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "LCM (EXACTLY DIVISIBLE BY ANOTHER NUMBER)"
    },
    "Aptitude > HCF LCM > RELATION BETWEEN HCF & LCM": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "RELATION BETWEEN HCF & LCM"
    },
    "Aptitude > HCF LCM > NUMBER OF PAIRS": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "NUMBER OF PAIRS"
    },
    "Aptitude > HCF LCM > APPLICATION SUMS (HCF)": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "APPLICATION SUMS (HCF)"
    },
    "Aptitude > HCF LCM > APPLICATION SUMS (LCM)": {
        "subject": "Aptitude",
        "topic": "HCF LCM",
        "subtopic": "APPLICATION SUMS (LCM)"
    },
    "Aptitude > AVERAGE > AVERAGE (BASIC) SIMPLE & WEIGHTED": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "AVERAGE (BASIC) SIMPLE & WEIGHTED"
    },
    "Aptitude > AVERAGE > FINDING AVERAGE OF GIVEN SERIES": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "FINDING AVERAGE OF GIVEN SERIES"
    },
    "Aptitude > AVERAGE > CHANGE IN AVERAGE (ADDED TO ALL NUMBERS)": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "CHANGE IN AVERAGE (ADDED TO ALL NUMBERS)"
    },
    "Aptitude > AVERAGE > FINDING THE MISSING NUMBER / REPEATED NUMBER": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "FINDING THE MISSING NUMBER / REPEATED NUMBER"
    },
    "Aptitude > AVERAGE > WITHOUT REPLACEMENT": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "WITHOUT REPLACEMENT"
    },
    "Aptitude > AVERAGE > WITH REPLACEMENT": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "WITH REPLACEMENT"
    },
    "Aptitude > AVERAGE > ERROR ON MARKS (CORRECTED AVERAGE)": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "ERROR ON MARKS (CORRECTED AVERAGE)"
    },
    "Aptitude > AVERAGE > CRICKET (BASIC)": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "CRICKET (BASIC)"
    },
    "Aptitude > AVERAGE > BATTING & BOWLING": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "BATTING & BOWLING"
    },
    "Aptitude > AVERAGE > AVERAGE EXPENDITURE": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "AVERAGE EXPENDITURE"
    },
    "Aptitude > AVERAGE > MISCELLANEOUS": {
        "subject": "Aptitude",
        "topic": "AVERAGE",
        "subtopic": "MISCELLANEOUS"
    },
    "Aptitude > RATIO PROPORTION > COMPOUND RATIO": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "COMPOUND RATIO"
    },
    "Aptitude > RATIO PROPORTION > PROPORTION PROPERTIES": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "PROPORTION PROPERTIES"
    },
    "Aptitude > RATIO PROPORTION > THIRD , FOURTH & MEAN PROPORTION": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "THIRD , FOURTH & MEAN PROPORTION"
    },
    "Aptitude > RATIO PROPORTION > ADDITION / SUBTRACTION NUMBER TO MAKE A PROPORTION": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "ADDITION / SUBTRACTION NUMBER TO MAKE A PROPORTION"
    },
    "Aptitude > RATIO PROPORTION > BASED ON COINS": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "BASED ON COINS"
    },
    "Aptitude > RATIO PROPORTION > MIXTURE BASED QUESTIONS": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "MIXTURE BASED QUESTIONS"
    },
    "Aptitude > RATIO PROPORTION > IN RATIO LEFT / ADD SOME STUDENT": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "IN RATIO LEFT / ADD SOME STUDENT"
    },
    "Aptitude > RATIO PROPORTION > INCOME , EXPENDITURE & SAVING": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "INCOME , EXPENDITURE & SAVING"
    },
    "Aptitude > RATIO PROPORTION > BASED ON PERCENTAGE (I = E + S)": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "BASED ON PERCENTAGE (I = E + S)"
    },
    "Aptitude > RATIO PROPORTION > BASED ON PREVIOUS YEAR & CURRENT YEAR": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "BASED ON PREVIOUS YEAR & CURRENT YEAR"
    },
    "Aptitude > RATIO PROPORTION > BASED ON A = B X C , B = A/C, C = A/B": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "BASED ON A = B X C , B = A/C, C = A/B"
    },
    "Aptitude > RATIO PROPORTION > BASED ON DIRECT & INVERSELY PROPORTIONAL": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "BASED ON DIRECT & INVERSELY PROPORTIONAL"
    },
    "Aptitude > RATIO PROPORTION > BASED ON FRACTIONS": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "BASED ON FRACTIONS"
    },
    "Aptitude > RATIO PROPORTION > AGES": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "AGES"
    },
    "Aptitude > RATIO PROPORTION > PARTNERSHIP - BASICS": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "PARTNERSHIP - BASICS"
    },
    "Aptitude > RATIO PROPORTION > INTRODUCTION - CAPITAL OF PARTNERS ARE INVESTED FOR A DIFFERENT PERIOD OF TIME": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "INTRODUCTION - CAPITAL OF PARTNERS ARE INVESTED FOR A DIFFERENT PERIOD OF TIME"
    },
    "Aptitude > RATIO PROPORTION > CAPITAL OF PARTNERS ARE INVESTED FOR A DIFFERENT PERIOD OF TIME": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "CAPITAL OF PARTNERS ARE INVESTED FOR A DIFFERENT PERIOD OF TIME"
    },
    "Aptitude > RATIO PROPORTION > WORKING ON SLEEPING PARTNERS": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "WORKING ON SLEEPING PARTNERS"
    },
    "Aptitude > RATIO PROPORTION > MISCELLANENOUS - BASED ON PREVIOUS SUMS": {
        "subject": "Aptitude",
        "topic": "RATIO PROPORTION",
        "subtopic": "MISCELLANENOUS - BASED ON PREVIOUS SUMS"
    },
    "Aptitude > MIXTURE ALLIGATION > Alligation": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "Alligation"
    },
    "Aptitude > MIXTURE ALLIGATION > BASED ON MIXTURE SELLING AT PROFIT": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "BASED ON MIXTURE SELLING AT PROFIT"
    },
    "Aptitude > MIXTURE ALLIGATION > BASED ON AVERAGE CONCEPT": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "BASED ON AVERAGE CONCEPT"
    },
    "Aptitude > MIXTURE ALLIGATION > BASED ON THREE VARIABLES (ALLIGATIONS)": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "BASED ON THREE VARIABLES (ALLIGATIONS)"
    },
    "Aptitude > MIXTURE ALLIGATION > BASED ON PROFIT PERCENTAGE & TIME , SPEED & DISTANCE": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "BASED ON PROFIT PERCENTAGE & TIME , SPEED & DISTANCE"
    },
    "Aptitude > MIXTURE ALLIGATION > BASED ON AMOUNT=VALUEX NUMBER OF PERSONS": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "BASED ON AMOUNT=VALUEX NUMBER OF PERSONS"
    },
    "Aptitude > MIXTURE ALLIGATION > QUESTIONS RELATED TO OTHER TOPICS PERCENTAGE, SIMPLE INTEREST, ZOO (ANIMAL BASED QUESTIONS) AND INCOME , EXPENDITURE AND SAVINGS": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "QUESTIONS RELATED TO OTHER TOPICS PERCENTAGE, SIMPLE INTEREST, ZOO (ANIMAL BASED QUESTIONS) AND INCOME , EXPENDITURE AND SAVINGS"
    },
    "Aptitude > MIXTURE ALLIGATION > ADD OR REMOVAL OF SOME QUANTITY": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "ADD OR REMOVAL OF SOME QUANTITY"
    },
    "Aptitude > MIXTURE ALLIGATION > REMOVE MIXTURE AND ADD SAME OR DIFFERENT QUANTITIES OF EITHER OF THESE SOLUTIONS": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "REMOVE MIXTURE AND ADD SAME OR DIFFERENT QUANTITIES OF EITHER OF THESE SOLUTIONS"
    },
    "Aptitude > MIXTURE ALLIGATION > ALLEGATIONS BASED MIXTURE QUESTIONS": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "ALLEGATIONS BASED MIXTURE QUESTIONS"
    },
    "Aptitude > MIXTURE ALLIGATION > REPEATED PROCESS OF REMOVAL AND ADDITION": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "REPEATED PROCESS OF REMOVAL AND ADDITION"
    },
    "Aptitude > MIXTURE ALLIGATION > FIND RATIO OF REPEATED PROCESS ARE GIVEN": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "FIND RATIO OF REPEATED PROCESS ARE GIVEN"
    },
    "Aptitude > MIXTURE ALLIGATION > MIXTURE OF TWO THINGS SAME QUANTITY": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "MIXTURE OF TWO THINGS SAME QUANTITY"
    },
    "Aptitude > MIXTURE ALLIGATION > MXITURE OF TWO THINGS DIFFERENT QUANTITIES": {
        "subject": "Aptitude",
        "topic": "MIXTURE ALLIGATION",
        "subtopic": "MXITURE OF TWO THINGS DIFFERENT QUANTITIES"
    },
    "Aptitude > PERCENTAGE > Percentage to Fraction": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Percentage to Fraction"
    },
    "Aptitude > PERCENTAGE > Basic Problems": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Basic Problems"
    },
    "Aptitude > PERCENTAGE > Comparing 2 Values": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Comparing 2 Values"
    },
    "Aptitude > PERCENTAGE > Price & Consumption": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Price & Consumption"
    },
    "Aptitude > PERCENTAGE > Price,Consumption & Quantity": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Price,Consumption & Quantity"
    },
    "Aptitude > PERCENTAGE > Comparison of Numbers": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Comparison of Numbers"
    },
    "Aptitude > PERCENTAGE > Net Percent Change": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Net Percent Change"
    },
    "Aptitude > PERCENTAGE > Examination": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Examination"
    },
    "Aptitude > PERCENTAGE > Income, Expenditure & Savings": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Income, Expenditure & Savings"
    },
    "Aptitude > PERCENTAGE > Price & Population & Depreciation": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Price & Population & Depreciation"
    },
    "Aptitude > PERCENTAGE > Election": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Election"
    },
    "Aptitude > PERCENTAGE > Venn Diagram": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Venn Diagram"
    },
    "Aptitude > PERCENTAGE > Questions on Remaining Values": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Questions on Remaining Values"
    },
    "Aptitude > PERCENTAGE > Fresh / Dry Fruit": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Fresh / Dry Fruit"
    },
    "Aptitude > PERCENTAGE > Income tax & Error %": {
        "subject": "Aptitude",
        "topic": "PERCENTAGE",
        "subtopic": "Income tax & Error %"
    },
    "Aptitude > PROFIT LOSS > PROFIT ON SELLING PRICE": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "PROFIT ON SELLING PRICE"
    },
    "Aptitude > PROFIT LOSS > PROFIT/LOSS ON NUMBER OF ARTICLES": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "PROFIT/LOSS ON NUMBER OF ARTICLES"
    },
    "Aptitude > PROFIT LOSS > Variation in Selling Price": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Variation in Selling Price"
    },
    "Aptitude > PROFIT LOSS > Variation in Cost Price & Selling Price": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Variation in Cost Price & Selling Price"
    },
    "Aptitude > PROFIT LOSS > Same Cost Price (or) Selling price": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Same Cost Price (or) Selling price"
    },
    "Aptitude > PROFIT LOSS > Total Cost Price of Two Articles": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Total Cost Price of Two Articles"
    },
    "Aptitude > PROFIT LOSS > PARTIAL SELLING": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "PARTIAL SELLING"
    },
    "Aptitude > PROFIT LOSS > Rotation among Different Sellers": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Rotation among Different Sellers"
    },
    "Aptitude > PROFIT LOSS > Ratio between Profit & Loss": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Ratio between Profit & Loss"
    },
    "Aptitude > PROFIT LOSS > Successive Discount": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Successive Discount"
    },
    "Aptitude > PROFIT LOSS > Cost Price Marked Price & Selling Price": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Cost Price Marked Price & Selling Price"
    },
    "Aptitude > PROFIT LOSS > Dishonest Seller": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Dishonest Seller"
    },
    "Aptitude > PROFIT LOSS > Profit by Alligation": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Profit by Alligation"
    },
    "Aptitude > PROFIT LOSS > Miscellaneous Questions": {
        "subject": "Aptitude",
        "topic": "PROFIT LOSS",
        "subtopic": "Miscellaneous Questions"
    },
    "Aptitude > SIMPLE INTEREST > Basic Question": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Basic Question"
    },
    "Aptitude > SIMPLE INTEREST > Finding Principal, Rate & Time": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Finding Principal, Rate & Time"
    },
    "Aptitude > SIMPLE INTEREST > Change in Rate and Time": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Change in Rate and Time"
    },
    "Aptitude > SIMPLE INTEREST > Based on Ratio": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Based on Ratio"
    },
    "Aptitude > SIMPLE INTEREST > Based on Distribution": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Based on Distribution"
    },
    "Aptitude > SIMPLE INTEREST > Based on Alligation": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Based on Alligation"
    },
    "Aptitude > SIMPLE INTEREST > Installment": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Installment"
    },
    "Aptitude > SIMPLE INTEREST > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "SIMPLE INTEREST",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > COMPOUND INTEREST > Basic Questions": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Basic Questions"
    },
    "Aptitude > COMPOUND INTEREST > Half - Yearly Basis": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Half - Yearly Basis"
    },
    "Aptitude > COMPOUND INTEREST > Quarterly Basis": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Quarterly Basis"
    },
    "Aptitude > COMPOUND INTEREST > Half - yearly / Quarterly Basis": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Half - yearly / Quarterly Basis"
    },
    "Aptitude > COMPOUND INTEREST > Different amounts at the same rate": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Different amounts at the same rate"
    },
    "Aptitude > COMPOUND INTEREST > ‘n’ times of principal": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "‘n’ times of principal"
    },
    "Aptitude > COMPOUND INTEREST > Mixed of SI and CI": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Mixed of SI and CI"
    },
    "Aptitude > COMPOUND INTEREST > Difference between SI and CI": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Difference between SI and CI"
    },
    "Aptitude > COMPOUND INTEREST > Installment": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Installment"
    },
    "Aptitude > COMPOUND INTEREST > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "COMPOUND INTEREST",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > TIME AND WORK > Alternate Days": {
        "subject": "Aptitude",
        "topic": "TIME AND WORK",
        "subtopic": "Alternate Days"
    },
    "Aptitude > TIME AND WORK > Wages": {
        "subject": "Aptitude",
        "topic": "TIME AND WORK",
        "subtopic": "Wages"
    },
    "Aptitude > TIME AND WORK > Remaining Work or Partial Work": {
        "subject": "Aptitude",
        "topic": "TIME AND WORK",
        "subtopic": "Remaining Work or Partial Work"
    },
    "Aptitude > TIME AND WORK > Efficiency": {
        "subject": "Aptitude",
        "topic": "TIME AND WORK",
        "subtopic": "Efficiency"
    },
    "Aptitude > TIME AND WORK > Chain Rule": {
        "subject": "Aptitude",
        "topic": "TIME AND WORK",
        "subtopic": "Chain Rule"
    },
    "Aptitude > TIME AND WORK > Miscellaneous": {
        "subject": "Aptitude",
        "topic": "TIME AND WORK",
        "subtopic": "Miscellaneous"
    },
    "Aptitude > TIME AND WORK > Pipes and Cisterns": {
        "subject": "Aptitude",
        "topic": "TIME AND WORK",
        "subtopic": "Pipes and Cisterns"
    },
    "Aptitude > TIME AND DISTANCE > USUAL SPEED AND TIME": {
        "subject": "Aptitude",
        "topic": "TIME AND DISTANCE",
        "subtopic": "USUAL SPEED AND TIME"
    },
    "Aptitude > TIME AND DISTANCE > AVERAGE SPEED": {
        "subject": "Aptitude",
        "topic": "TIME AND DISTANCE",
        "subtopic": "AVERAGE SPEED"
    },
    "Aptitude > TIME AND DISTANCE > RATIO": {
        "subject": "Aptitude",
        "topic": "TIME AND DISTANCE",
        "subtopic": "RATIO"
    },
    "Aptitude > TIME AND DISTANCE > RELATIVE SPEED 1": {
        "subject": "Aptitude",
        "topic": "TIME AND DISTANCE",
        "subtopic": "RELATIVE SPEED 1"
    },
    "Aptitude > TIME AND DISTANCE > CHANGE IN SPEED 2": {
        "subject": "Aptitude",
        "topic": "TIME AND DISTANCE",
        "subtopic": "CHANGE IN SPEED 2"
    },
    "Aptitude > TIME AND DISTANCE > MISCELLANEOUS": {
        "subject": "Aptitude",
        "topic": "TIME AND DISTANCE",
        "subtopic": "MISCELLANEOUS"
    },
    "Aptitude > TIME AND DISTANCE > RACE": {
        "subject": "Aptitude",
        "topic": "TIME AND DISTANCE",
        "subtopic": "RACE"
    },
    "Aptitude > TRAIN > BASIC CONCEPT TRAIN": {
        "subject": "Aptitude",
        "topic": "TRAIN",
        "subtopic": "BASIC CONCEPT TRAIN"
    },
    "Aptitude > TRAIN > TRAIN THEORY": {
        "subject": "Aptitude",
        "topic": "TRAIN",
        "subtopic": "TRAIN THEORY"
    },
    "Aptitude > TRAIN > RELATIVE SPEED QUESTION": {
        "subject": "Aptitude",
        "topic": "TRAIN",
        "subtopic": "RELATIVE SPEED QUESTION"
    },
    "Aptitude > TRAIN > SPEED RATIO`S": {
        "subject": "Aptitude",
        "topic": "TRAIN",
        "subtopic": "SPEED RATIO`S"
    },
    "Aptitude > TRAIN > PROBLEMS ON DIRECTION": {
        "subject": "Aptitude",
        "topic": "TRAIN",
        "subtopic": "PROBLEMS ON DIRECTION"
    },
    "Aptitude > BOAT & STREAMS > Boats & Streams": {
        "subject": "Aptitude",
        "topic": "BOAT & STREAMS",
        "subtopic": "Boats & Streams"
    },
    "Aptitude > BOAT & STREAMS > Boats & Streams QUESTIONS": {
        "subject": "Aptitude",
        "topic": "BOAT & STREAMS",
        "subtopic": "Boats & Streams QUESTIONS"
    },
    "Aptitude > BOAT & STREAMS > EQUATION BASED PROBLEMS": {
        "subject": "Aptitude",
        "topic": "BOAT & STREAMS",
        "subtopic": "EQUATION BASED PROBLEMS"
    },
    "Aptitude > BOAT & STREAMS > DOWNSTREAM AS MUCH AS UPSTREAMEQUAITON BASED PROBLEMS": {
        "subject": "Aptitude",
        "topic": "BOAT & STREAMS",
        "subtopic": "DOWNSTREAM AS MUCH AS UPSTREAMEQUAITON BASED PROBLEMS"
    },
    "Aptitude > DATA INTERPRETATION > Pie-chart": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Pie-chart"
    },
    "Aptitude > DATA INTERPRETATION > Line Graph": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Line Graph"
    },
    "Aptitude > DATA INTERPRETATION > Simple Bar": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Simple Bar"
    },
    "Aptitude > DATA INTERPRETATION > Horizontal and Divide Bar": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Horizontal and Divide Bar"
    },
    "Aptitude > DATA INTERPRETATION > Multi Bar": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Multi Bar"
    },
    "Aptitude > DATA INTERPRETATION > Histogram": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Histogram"
    },
    "Aptitude > DATA INTERPRETATION > Table Chart": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Table Chart"
    },
    "Aptitude > DATA INTERPRETATION > Miscellaneous - 1": {
        "subject": "Aptitude",
        "topic": "DATA INTERPRETATION",
        "subtopic": "Miscellaneous - 1"
    },
    "Aptitude > ALGEBRA > Polynomials": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Polynomials"
    },
    "Aptitude > ALGEBRA > Linear equation in 2 variables": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Linear equation in 2 variables"
    },
    "Aptitude > ALGEBRA > Solubility of Linear Equation": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Solubility of Linear Equation"
    },
    "Aptitude > ALGEBRA > Linear Equation in 3 Variables": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Linear Equation in 3 Variables"
    },
    "Aptitude > ALGEBRA > Roots of Quadratic Equation": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Roots of Quadratic Equation"
    },
    "Aptitude > ALGEBRA > Problems on Roots of Quadratic Equation": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Problems on Roots of Quadratic Equation"
    },
    "Aptitude > ALGEBRA > Max & Min of Quadratic expression": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Max & Min of Quadratic expression"
    },
    "Aptitude > ALGEBRA > Maximum & Minimum Value": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Maximum & Minimum Value"
    },
    "Aptitude > ALGEBRA > Roots of Cubic Equation": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Roots of Cubic Equation"
    },
    "Aptitude > ALGEBRA > Factors & Remainders": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Factors & Remainders"
    },
    "Aptitude > ALGEBRA > Algebraic Identities": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Algebraic Identities"
    },
    "Aptitude > ALGEBRA > Squares": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Squares"
    },
    "Aptitude > ALGEBRA > Cube": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Cube"
    },
    "Aptitude > ALGEBRA > Square Root & Cube Root": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Square Root & Cube Root"
    },
    "Aptitude > ALGEBRA > Special Formula Part": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Special Formula Part"
    },
    "Aptitude > ALGEBRA > Sum of squares = 0": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Sum of squares = 0"
    },
    "Aptitude > ALGEBRA > Inverse Functions - 1": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Inverse Functions - 1"
    },
    "Aptitude > ALGEBRA > Reverse order - 1": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Reverse order - 1"
    },
    "Aptitude > ALGEBRA > Special Stats - 1": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Special Stats - 1"
    },
    "Aptitude > ALGEBRA > Symmetric - 2": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Symmetric - 2"
    },
    "Aptitude > ALGEBRA > Symmetric equation": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Symmetric equation"
    },
    "Aptitude > ALGEBRA > Value Putting - 1": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Value Putting - 1"
    },
    "Aptitude > ALGEBRA > Square Root of Irrational Numbers": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Square Root of Irrational Numbers"
    },
    "Aptitude > ALGEBRA > Componendo - Dividendo": {
        "subject": "Aptitude",
        "topic": "ALGEBRA",
        "subtopic": "Componendo - Dividendo"
    },
    "Aptitude > GEOMETRY > Types of Angles": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Types of Angles"
    },
    "Aptitude > GEOMETRY > Lines & angles concepts": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Lines & angles concepts"
    },
    "Aptitude > GEOMETRY > Triangles-Properties of a triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Triangles-Properties of a triangle"
    },
    "Aptitude > GEOMETRY > Triangles-Exterior angle property": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Triangles-Exterior angle property"
    },
    "Aptitude > GEOMETRY > Triangles-basic question": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Triangles-basic question"
    },
    "Aptitude > GEOMETRY > Condition for formation of a triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Condition for formation of a triangle"
    },
    "Aptitude > GEOMETRY > Sine Rule": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Sine Rule"
    },
    "Aptitude > GEOMETRY > Triangles-Stewart’s Theorem": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Triangles-Stewart’s Theorem"
    },
    "Aptitude > GEOMETRY > Triangles-Internal bisector": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Triangles-Internal bisector"
    },
    "Aptitude > GEOMETRY > Types of triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Types of triangle"
    },
    "Aptitude > GEOMETRY > Isosceles Triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Isosceles Triangle"
    },
    "Aptitude > GEOMETRY > Equilateral Triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Equilateral Triangle"
    },
    "Aptitude > GEOMETRY > Triangles-On the basis of angles": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Triangles-On the basis of angles"
    },
    "Aptitude > GEOMETRY > Congruent Triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Congruent Triangle"
    },
    "Aptitude > GEOMETRY > Triangles-Similarality": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Triangles-Similarality"
    },
    "Aptitude > GEOMETRY > Similarity of right angle triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Similarity of right angle triangle"
    },
    "Aptitude > GEOMETRY > Basic Proportionality Theorem": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Basic Proportionality Theorem"
    },
    "Aptitude > GEOMETRY > Centers of Triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Centers of Triangle"
    },
    "Aptitude > GEOMETRY > Median Property": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Median Property"
    },
    "Aptitude > GEOMETRY > Apollonius's Theorem": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Apollonius's Theorem"
    },
    "Aptitude > GEOMETRY > Median in a Right-Angled Triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Median in a Right-Angled Triangle"
    },
    "Aptitude > GEOMETRY > Incentre": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Incentre"
    },
    "Aptitude > GEOMETRY > Inradius": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Inradius"
    },
    "Aptitude > GEOMETRY > Ex-Circle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Ex-Circle"
    },
    "Aptitude > GEOMETRY > Circumcenter": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circumcenter"
    },
    "Aptitude > GEOMETRY > Circumcentre in Triangles": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circumcentre in Triangles"
    },
    "Aptitude > GEOMETRY > Circumcentre in Right Angle Triangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circumcentre in Right Angle Triangle"
    },
    "Aptitude > GEOMETRY > Orthocentre": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Orthocentre"
    },
    "Aptitude > GEOMETRY > Orthocentre-Height and Side Ratio": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Orthocentre-Height and Side Ratio"
    },
    "Aptitude > GEOMETRY > Orthocenter-Altitude in Terms of the Sides": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Orthocenter-Altitude in Terms of the Sides"
    },
    "Aptitude > GEOMETRY > Interior Angle Bisector Theorem": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Interior Angle Bisector Theorem"
    },
    "Aptitude > GEOMETRY > Interior Angle Bisector Theorem-Length of Angle Bisector": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Interior Angle Bisector Theorem-Length of Angle Bisector"
    },
    "Aptitude > GEOMETRY > Length of Angle Bisector": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Length of Angle Bisector"
    },
    "Aptitude > GEOMETRY > Mass Point Geometry": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Mass Point Geometry"
    },
    "Aptitude > GEOMETRY > Circle-Intro": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle-Intro"
    },
    "Aptitude > GEOMETRY > Circle-Chord": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle-Chord"
    },
    "Aptitude > GEOMETRY > Circles-Property": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-Property"
    },
    "Aptitude > GEOMETRY > Circles-basic qustion": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-basic qustion"
    },
    "Aptitude > GEOMETRY > Circles-two chords": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-two chords"
    },
    "Aptitude > GEOMETRY > Circles-Secants intersect": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-Secants intersect"
    },
    "Aptitude > GEOMETRY > Circles-Secants & Tagent": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-Secants & Tagent"
    },
    "Aptitude > GEOMETRY > Circles-Length of the chord": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-Length of the chord"
    },
    "Aptitude > GEOMETRY > Circles-Two parallel chords": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-Two parallel chords"
    },
    "Aptitude > GEOMETRY > Circles-Tangent": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-Tangent"
    },
    "Aptitude > GEOMETRY > Circles-Alternate Segment Theorem": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-Alternate Segment Theorem"
    },
    "Aptitude > GEOMETRY > Circles-circumscribing a circle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circles-circumscribing a circle"
    },
    "Aptitude > GEOMETRY > Circle-Touch Externally": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle-Touch Externally"
    },
    "Aptitude > GEOMETRY > Circle-Intersect each other": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle-Intersect each other"
    },
    "Aptitude > GEOMETRY > Circle-Intersecting Circles": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle-Intersecting Circles"
    },
    "Aptitude > GEOMETRY > Circle-Concentric Circles": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle-Concentric Circles"
    },
    "Aptitude > GEOMETRY > Circle-three circle with radii": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle-three circle with radii"
    },
    "Aptitude > GEOMETRY > Direct Common Tangent": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Direct Common Tangent"
    },
    "Aptitude > GEOMETRY > Transverse Common Tangent": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Transverse Common Tangent"
    },
    "Aptitude > GEOMETRY > Circle- two circle intersecting internally": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Circle- two circle intersecting internally"
    },
    "Aptitude > GEOMETRY > Cyclic Quadrilateral": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Cyclic Quadrilateral"
    },
    "Aptitude > GEOMETRY > Area of Cyclic Quadrilateral": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Area of Cyclic Quadrilateral"
    },
    "Aptitude > GEOMETRY > Quadrilateral": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Quadrilateral"
    },
    "Aptitude > GEOMETRY > Quadrilateral-Types": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Quadrilateral-Types"
    },
    "Aptitude > GEOMETRY > Parallelogram": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Parallelogram"
    },
    "Aptitude > GEOMETRY > Rectangle": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Rectangle"
    },
    "Aptitude > GEOMETRY > Square": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Square"
    },
    "Aptitude > GEOMETRY > Rhombus": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Rhombus"
    },
    "Aptitude > GEOMETRY > Trapezium": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Trapezium"
    },
    "Aptitude > GEOMETRY > Polygon": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Polygon"
    },
    "Aptitude > GEOMETRY > Angles of polygon": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Angles of polygon"
    },
    "Aptitude > GEOMETRY > Area of Regular Polygon": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Area of Regular Polygon"
    },
    "Aptitude > GEOMETRY > Hexagon": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Hexagon"
    },
    "Aptitude > GEOMETRY > Hexagon-Equal Divisions of Area": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Hexagon-Equal Divisions of Area"
    },
    "Aptitude > GEOMETRY > Hexagon-Basic Question": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Hexagon-Basic Question"
    },
    "Aptitude > GEOMETRY > Octagon": {
        "subject": "Aptitude",
        "topic": "GEOMETRY",
        "subtopic": "Octagon"
    },
    "Aptitude > COORDINATE GEOMETRY > Distance between Two Points": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Distance between Two Points"
    },
    "Aptitude > COORDINATE GEOMETRY > Section of a Line": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Section of a Line"
    },
    "Aptitude > COORDINATE GEOMETRY > Slope of a Line": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Slope of a Line"
    },
    "Aptitude > COORDINATE GEOMETRY > Angle between Two Lines": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Angle between Two Lines"
    },
    "Aptitude > COORDINATE GEOMETRY > Equation of lines": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Equation of lines"
    },
    "Aptitude > COORDINATE GEOMETRY > Distance of a Point from a Line": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Distance of a Point from a Line"
    },
    "Aptitude > COORDINATE GEOMETRY > Distance between Parallel Lines": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Distance between Parallel Lines"
    },
    "Aptitude > COORDINATE GEOMETRY > Reflection of a Point": {
        "subject": "Aptitude",
        "topic": "COORDINATE GEOMETRY",
        "subtopic": "Reflection of a Point"
    },
    "Aptitude > MENSURATION > Polygons": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Polygons"
    },
    "Aptitude > MENSURATION > Triangles": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Triangles"
    },
    "Aptitude > MENSURATION > Classification of Triangles": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Classification of Triangles"
    },
    "Aptitude > MENSURATION > Area and Perimeter of Triangle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Area and Perimeter of Triangle"
    },
    "Aptitude > MENSURATION > Area of cyclic Quadrilateral": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Area of cyclic Quadrilateral"
    },
    "Aptitude > MENSURATION > Square": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Square"
    },
    "Aptitude > MENSURATION > Rectangle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Rectangle"
    },
    "Aptitude > MENSURATION > Rhombus": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Rhombus"
    },
    "Aptitude > MENSURATION > Parallelogram": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Parallelogram"
    },
    "Aptitude > MENSURATION > Trapezium": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Trapezium"
    },
    "Aptitude > MENSURATION > Hexagon": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Hexagon"
    },
    "Aptitude > MENSURATION > Octagon": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Octagon"
    },
    "Aptitude > MENSURATION > Circle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Circle"
    },
    "Aptitude > MENSURATION > Ratio of Radius, Perimeter & Area of Circle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Ratio of Radius, Perimeter & Area of Circle"
    },
    "Aptitude > MENSURATION > Circular Ring": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Circular Ring"
    },
    "Aptitude > MENSURATION > Area and Perimeter of Semi Circle & Quarter Circle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Area and Perimeter of Semi Circle & Quarter Circle"
    },
    "Aptitude > MENSURATION > Sector of a Circle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Sector of a Circle"
    },
    "Aptitude > MENSURATION > Square and Circle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Square and Circle"
    },
    "Aptitude > MENSURATION > Triangles & Circles": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Triangles & Circles"
    },
    "Aptitude > MENSURATION > Square,Rectangle & Triangle": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Square,Rectangle & Triangle"
    },
    "Aptitude > MENSURATION > Same perimeter": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Same perimeter"
    },
    "Aptitude > MENSURATION > Rectangle path": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Rectangle path"
    },
    "Aptitude > MENSURATION > Cost based on Area & Perimeter": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Cost based on Area & Perimeter"
    },
    "Aptitude > MENSURATION > Band Around Circles": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Band Around Circles"
    },
    "Aptitude > MENSURATION > Prism": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Prism"
    },
    "Aptitude > MENSURATION > Cube": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Cube"
    },
    "Aptitude > MENSURATION > Cuboid": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Cuboid"
    },
    "Aptitude > MENSURATION > Right Circular Cylinder": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Right Circular Cylinder"
    },
    "Aptitude > MENSURATION > Pyramid": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Pyramid"
    },
    "Aptitude > MENSURATION > Cone": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Cone"
    },
    "Aptitude > MENSURATION > Frustom of a Cone": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Frustom of a Cone"
    },
    "Aptitude > MENSURATION > Ratio of Volume of Pyramid": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Ratio of Volume of Pyramid"
    },
    "Aptitude > MENSURATION > Sphere": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Sphere"
    },
    "Aptitude > MENSURATION > Hollow Sphere": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Hollow Sphere"
    },
    "Aptitude > MENSURATION > Hemisphere": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Hemisphere"
    },
    "Aptitude > MENSURATION > Relation between Volumes of Cylinder, Cone and Hemisphere": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Relation between Volumes of Cylinder, Cone and Hemisphere"
    },
    "Aptitude > MENSURATION > Conversion of Solids from One Form to Another": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Conversion of Solids from One Form to Another"
    },
    "Aptitude > MENSURATION > Area or Volume after Removal of Solids": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Area or Volume after Removal of Solids"
    },
    "Aptitude > MENSURATION > Volume of Water Flowing from a Pipe": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Volume of Water Flowing from a Pipe"
    },
    "Aptitude > MENSURATION > Useful Results": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Useful Results"
    },
    "Aptitude > MENSURATION > One Figure inside Another": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "One Figure inside Another"
    },
    "Aptitude > MENSURATION > Figure Based Questions": {
        "subject": "Aptitude",
        "topic": "MENSURATION",
        "subtopic": "Figure Based Questions"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Trigonometry circular measure of angles": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Trigonometry circular measure of angles"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Circular system": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Circular system"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Basic Identities of trigonometry": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Basic Identities of trigonometry"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Trigonometric Ratios of some specific angles": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Trigonometric Ratios of some specific angles"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Quadrant System": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Quadrant System"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > basic question": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "basic question"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Sum of two angles (𝛼+𝛽)=90": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Sum of two angles (𝛼+𝛽)=90"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Basic identities": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Basic identities"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Based on putting value": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Based on putting value"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > x+1/x=2": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "x+1/x=2"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Basic identity (compound angles)": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Basic identity (compound angles)"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Maximum & minimum value of trigonometrix": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Maximum & minimum value of trigonometrix"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > HEIGHT & DISTANCE-basic concept": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "HEIGHT & DISTANCE-basic concept"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > Based on Angle Changed": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "Based on Angle Changed"
    },
    "Aptitude > Trigonometry & HEIGHT AND DISTANCE > HEIGHT & DISTANCE-Complementary Angle": {
        "subject": "Aptitude",
        "topic": "Trigonometry & HEIGHT AND DISTANCE",
        "subtopic": "HEIGHT & DISTANCE-Complementary Angle"
    },
    "Aptitude > Probability > Probability": {
        "subject": "Aptitude",
        "topic": "Probability",
        "subtopic": "Probability"
    },
    "Aptitude > Statistics > Class intervals , Frequency": {
        "subject": "Aptitude",
        "topic": "Statistics",
        "subtopic": "Class intervals , Frequency"
    },
    "Aptitude > Statistics > Mean,Mode,Median": {
        "subject": "Aptitude",
        "topic": "Statistics",
        "subtopic": "Mean,Mode,Median"
    },
    "English > NOUN > Noun": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Noun"
    },
    "English > NOUN > Types of Nouns": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Types of Nouns"
    },
    "English > NOUN > Countable and Uncountable": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Countable and Uncountable"
    },
    "English > NOUN > Rules Based on Numbers": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Rules Based on Numbers"
    },
    "English > NOUN > Based on Gender": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Based on Gender"
    },
    "English > NOUN > Based On Noun - Case": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Based On Noun - Case"
    },
    "English > NOUN > Confusing Words": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Confusing Words"
    },
    "English > NOUN > Find the Correct One": {
        "subject": "English",
        "topic": "NOUN",
        "subtopic": "Find the Correct One"
    },
    "English > PRONOUN > Pronoun": {
        "subject": "English",
        "topic": "PRONOUN",
        "subtopic": "Pronoun"
    },
    "English > PRONOUN > Rules Based on Possessive Pronoun": {
        "subject": "English",
        "topic": "PRONOUN",
        "subtopic": "Rules Based on Possessive Pronoun"
    },
    "English > PRONOUN > Relative Pronoun": {
        "subject": "English",
        "topic": "PRONOUN",
        "subtopic": "Relative Pronoun"
    },
    "English > PRONOUN > Reciprocal Pronoun": {
        "subject": "English",
        "topic": "PRONOUN",
        "subtopic": "Reciprocal Pronoun"
    },
    "English > PRONOUN > Pronoun Workout": {
        "subject": "English",
        "topic": "PRONOUN",
        "subtopic": "Pronoun Workout"
    },
    "English > VERB > Forms of Verb": {
        "subject": "English",
        "topic": "VERB",
        "subtopic": "Forms of Verb"
    },
    "English > VERB > Regular Verbs": {
        "subject": "English",
        "topic": "VERB",
        "subtopic": "Regular Verbs"
    },
    "English > VERB > Modal verbs": {
        "subject": "English",
        "topic": "VERB",
        "subtopic": "Modal verbs"
    },
    "English > VERB > Rules Based on Verbs": {
        "subject": "English",
        "topic": "VERB",
        "subtopic": "Rules Based on Verbs"
    },
    "English > ADVERB > Adverb-Intro": {
        "subject": "English",
        "topic": "ADVERB",
        "subtopic": "Adverb-Intro"
    },
    "English > ADVERB > Adverb of Place": {
        "subject": "English",
        "topic": "ADVERB",
        "subtopic": "Adverb of Place"
    },
    "English > ADVERB > Rules for Adverb": {
        "subject": "English",
        "topic": "ADVERB",
        "subtopic": "Rules for Adverb"
    },
    "English > ADVERB > workouts": {
        "subject": "English",
        "topic": "ADVERB",
        "subtopic": "workouts"
    },
    "English > Adjectives > Adjectives-Intro": {
        "subject": "English",
        "topic": "Adjectives",
        "subtopic": "Adjectives-Intro"
    },
    "English > Adjectives > Distributive Adjectives": {
        "subject": "English",
        "topic": "Adjectives",
        "subtopic": "Distributive Adjectives"
    },
    "English > Adjectives > Rules - Degrees of Comparison": {
        "subject": "English",
        "topic": "Adjectives",
        "subtopic": "Rules - Degrees of Comparison"
    },
    "English > SUBJECT VERB AGREEMENT > Introduction": {
        "subject": "English",
        "topic": "SUBJECT VERB AGREEMENT",
        "subtopic": "Introduction"
    },
    "English > SUBJECT VERB AGREEMENT > Rule 1-5": {
        "subject": "English",
        "topic": "SUBJECT VERB AGREEMENT",
        "subtopic": "Rule 1-5"
    },
    "English > SUBJECT VERB AGREEMENT > Rule 06-12": {
        "subject": "English",
        "topic": "SUBJECT VERB AGREEMENT",
        "subtopic": "Rule 06-12"
    },
    "English > SUBJECT VERB AGREEMENT > Rule 13-19": {
        "subject": "English",
        "topic": "SUBJECT VERB AGREEMENT",
        "subtopic": "Rule 13-19"
    },
    "English > SUBJECT VERB AGREEMENT > Rule 20-24": {
        "subject": "English",
        "topic": "SUBJECT VERB AGREEMENT",
        "subtopic": "Rule 20-24"
    },
    "English > SUBJECT VERB AGREEMENT > Rule 25-28": {
        "subject": "English",
        "topic": "SUBJECT VERB AGREEMENT",
        "subtopic": "Rule 25-28"
    },
    "English > SUBJECT VERB AGREEMENT > Sentence Improvement & Error Spotting": {
        "subject": "English",
        "topic": "SUBJECT VERB AGREEMENT",
        "subtopic": "Sentence Improvement & Error Spotting"
    },
    "English > ARTICLES > ARTICLES-Intro": {
        "subject": "English",
        "topic": "ARTICLES",
        "subtopic": "ARTICLES-Intro"
    },
    "English > ARTICLES > ARTICLES-Use of a/an": {
        "subject": "English",
        "topic": "ARTICLES",
        "subtopic": "ARTICLES-Use of a/an"
    },
    "English > ARTICLES > ARTICLES-Use of The": {
        "subject": "English",
        "topic": "ARTICLES",
        "subtopic": "ARTICLES-Use of The"
    },
    "English > ARTICLES > Omission": {
        "subject": "English",
        "topic": "ARTICLES",
        "subtopic": "Omission"
    },
    "English > ARTICLES > Excersice": {
        "subject": "English",
        "topic": "ARTICLES",
        "subtopic": "Excersice"
    },
    "English > CONJUNCTION > Co-ordinating Conjunctions": {
        "subject": "English",
        "topic": "CONJUNCTION",
        "subtopic": "Co-ordinating Conjunctions"
    },
    "English > CONJUNCTION > Subordinating Conjunction": {
        "subject": "English",
        "topic": "CONJUNCTION",
        "subtopic": "Subordinating Conjunction"
    },
    "English > CONJUNCTION > Subordinating conjunctions & Correlative conjunctions": {
        "subject": "English",
        "topic": "CONJUNCTION",
        "subtopic": "Subordinating conjunctions & Correlative conjunctions"
    },
    "English > CONJUNCTION > Rules": {
        "subject": "English",
        "topic": "CONJUNCTION",
        "subtopic": "Rules"
    },
    "English > SPEECH > Introduction and Sentence types": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Introduction and Sentence types"
    },
    "English > SPEECH > Change of Persons": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Change of Persons"
    },
    "English > SPEECH > Change of Time": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Change of Time"
    },
    "English > SPEECH > Change of Time-Type 2": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Change of Time-Type 2"
    },
    "English > SPEECH > Other Parts of Speech and Assertive Sentence": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Other Parts of Speech and Assertive Sentence"
    },
    "English > SPEECH > Interrogative Sentence": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Interrogative Sentence"
    },
    "English > SPEECH > Imperative": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Imperative"
    },
    "English > SPEECH > Optative and Exclamatory Sentences": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Optative and Exclamatory Sentences"
    },
    "English > SPEECH > Previous year Question": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Previous year Question"
    },
    "English > SPEECH > Revision": {
        "subject": "English",
        "topic": "SPEECH",
        "subtopic": "Revision"
    },
    "English > Voice > Introduction": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Introduction"
    },
    "English > Voice > 5 Rules": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "5 Rules"
    },
    "English > Voice > Passive Formation of the Types of Tenses": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Passive Formation of the Types of Tenses"
    },
    "English > Voice > Continous tense": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Continous tense"
    },
    "English > Voice > Perfect tense": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Perfect tense"
    },
    "English > Voice > Modal auxillary verb": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Modal auxillary verb"
    },
    "English > Voice > Imperative": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Imperative"
    },
    "English > Voice > Interrogative-I": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Interrogative-I"
    },
    "English > Voice > Prepositions": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Prepositions"
    },
    "English > Voice > Miscellaneous": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Miscellaneous"
    },
    "English > Voice > Excersice": {
        "subject": "English",
        "topic": "Voice",
        "subtopic": "Excersice"
    },
    "English > READING COMPREHENSION > Questions": {
        "subject": "English",
        "topic": "READING COMPREHENSION",
        "subtopic": "Questions"
    },
    "English > CLOZE TEST > CLOZE TEST": {
        "subject": "English",
        "topic": "CLOZE TEST",
        "subtopic": "CLOZE TEST"
    },
    "English > VOCABULARY > SYNONYMS": {
        "subject": "English",
        "topic": "VOCABULARY",
        "subtopic": "SYNONYMS"
    },
    "English > VOCABULARY > ANTONYMS": {
        "subject": "English",
        "topic": "VOCABULARY",
        "subtopic": "ANTONYMS"
    },
    "English > ONE WORD SUBSTITUTION > ONE WORD SUBSTITUTION-1(UNDERLINED)": {
        "subject": "English",
        "topic": "ONE WORD SUBSTITUTION",
        "subtopic": "ONE WORD SUBSTITUTION-1(UNDERLINED)"
    },
    "English > ONE WORD SUBSTITUTION > ONE WORD SUBSTITUTION-2": {
        "subject": "English",
        "topic": "ONE WORD SUBSTITUTION",
        "subtopic": "ONE WORD SUBSTITUTION-2"
    },
    "English > IDIOMS PHRASES > Basic": {
        "subject": "English",
        "topic": "IDIOMS PHRASES",
        "subtopic": "Basic"
    },
    "English > IDIOMS PHRASES > Idiom-based on weather": {
        "subject": "English",
        "topic": "IDIOMS PHRASES",
        "subtopic": "Idiom-based on weather"
    },
    "English > IDIOMS PHRASES > Idiom-based on colour": {
        "subject": "English",
        "topic": "IDIOMS PHRASES",
        "subtopic": "Idiom-based on colour"
    },
    "English > IDIOMS PHRASES > Idiom-based on body parts": {
        "subject": "English",
        "topic": "IDIOMS PHRASES",
        "subtopic": "Idiom-based on body parts"
    },
    "English > IDIOMS PHRASES > Idiom-based on numbers": {
        "subject": "English",
        "topic": "IDIOMS PHRASES",
        "subtopic": "Idiom-based on numbers"
    },
    "English > IDIOMS PHRASES > Phrasal Verbs": {
        "subject": "English",
        "topic": "IDIOMS PHRASES",
        "subtopic": "Phrasal Verbs"
    },
    "English > QUESTION TAG > Introduction": {
        "subject": "English",
        "topic": "QUESTION TAG",
        "subtopic": "Introduction"
    },
    "English > QUESTION TAG > Rules 1-5": {
        "subject": "English",
        "topic": "QUESTION TAG",
        "subtopic": "Rules 1-5"
    },
    "English > QUESTION TAG > Rules 6-11": {
        "subject": "English",
        "topic": "QUESTION TAG",
        "subtopic": "Rules 6-11"
    },
    "English > QUESTION TAG > Excersice": {
        "subject": "English",
        "topic": "QUESTION TAG",
        "subtopic": "Excersice"
    },
    "English > CONDITIONAL CLAUSES > Introduction-Zero and first": {
        "subject": "English",
        "topic": "CONDITIONAL CLAUSES",
        "subtopic": "Introduction-Zero and first"
    },
    "English > CONDITIONAL CLAUSES > Second & three Conditional": {
        "subject": "English",
        "topic": "CONDITIONAL CLAUSES",
        "subtopic": "Second & three Conditional"
    },
    "English > CONDITIONAL CLAUSES > Mixed and Unless": {
        "subject": "English",
        "topic": "CONDITIONAL CLAUSES",
        "subtopic": "Mixed and Unless"
    },
    "English > CONDITIONAL CLAUSES > Spot the Error": {
        "subject": "English",
        "topic": "CONDITIONAL CLAUSES",
        "subtopic": "Spot the Error"
    },
    "General Studies > ANCIENT - History > Prehistoric And Indus Valley": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Prehistoric And Indus Valley"
    },
    "General Studies > ANCIENT - History > Vedic Age": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Vedic Age"
    },
    "General Studies > ANCIENT - History > Jainism": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Jainism"
    },
    "General Studies > ANCIENT - History > Buddhism": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Buddhism"
    },
    "General Studies > ANCIENT - History > Mahajanapadas": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Mahajanapadas"
    },
    "General Studies > ANCIENT - History > Mauryan Dynasty": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Mauryan Dynasty"
    },
    "General Studies > ANCIENT - History > Gupta Dynasty": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Gupta Dynasty"
    },
    "General Studies > ANCIENT - History > Vardhana Dynasty": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Vardhana Dynasty"
    },
    "General Studies > ANCIENT - History > sangam": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "sangam"
    },
    "General Studies > ANCIENT - History > Chola Dynasty": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Chola Dynasty"
    },
    "General Studies > ANCIENT - History > Pallavas": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Pallavas"
    },
    "General Studies > ANCIENT - History > SAKA ERA": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "SAKA ERA"
    },
    "General Studies > ANCIENT - History > Kushanas": {
        "subject": "General Studies",
        "topic": "ANCIENT - History",
        "subtopic": "Kushanas"
    },
    "General Studies > MEDIVEAL - History > Foreign Invasions": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Foreign Invasions"
    },
    "General Studies > MEDIVEAL - History > Delhi Sultanate": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Delhi Sultanate"
    },
    "General Studies > MEDIVEAL - History > Slave Dynasty": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Slave Dynasty"
    },
    "General Studies > MEDIVEAL - History > Khilji Dynasty": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Khilji Dynasty"
    },
    "General Studies > MEDIVEAL - History > Tughlaq Dynasty": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Tughlaq Dynasty"
    },
    "General Studies > MEDIVEAL - History > Sayyid Dynasty": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Sayyid Dynasty"
    },
    "General Studies > MEDIVEAL - History > Lodi Dynasty": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Lodi Dynasty"
    },
    "General Studies > MEDIVEAL - History > Mughal Period": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Mughal Period"
    },
    "General Studies > MEDIVEAL - History > Babur": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Babur"
    },
    "General Studies > MEDIVEAL - History > Humayun and Sher Shah Suri": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Humayun and Sher Shah Suri"
    },
    "General Studies > MEDIVEAL - History > Akbar": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Akbar"
    },
    "General Studies > MEDIVEAL - History > Jahangir": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Jahangir"
    },
    "General Studies > MEDIVEAL - History > Shah Jahan": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Shah Jahan"
    },
    "General Studies > MEDIVEAL - History > Aurangzeb": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Aurangzeb"
    },
    "General Studies > MEDIVEAL - History > SUFISM": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "SUFISM"
    },
    "General Studies > MEDIVEAL - History > Sikh Guru": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Sikh Guru"
    },
    "General Studies > MEDIVEAL - History > Maratha Empire": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Maratha Empire"
    },
    "General Studies > MEDIVEAL - History > Vijaynagar Empire": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Vijaynagar Empire"
    },
    "General Studies > MEDIVEAL - History > Wars and Treaties": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Wars and Treaties"
    },
    "General Studies > MEDIVEAL - History > Miscellaneous": {
        "subject": "General Studies",
        "topic": "MEDIVEAL - History",
        "subtopic": "Miscellaneous"
    },
    "General Studies > MODERN - History > The Revolt of 1857": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "The Revolt of 1857"
    },
    "General Studies > MODERN - History > Governors and Viceroys": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Governors and Viceroys"
    },
    "General Studies > MODERN - History > British acts and Policies": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "British acts and Policies"
    },
    "General Studies > MODERN - History > Partition of Bengal and Swadeshi Movements": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Partition of Bengal and Swadeshi Movements"
    },
    "General Studies > MODERN - History > Gandhian Era": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Gandhian Era"
    },
    "General Studies > MODERN - History > Expansion of British Rule": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Expansion of British Rule"
    },
    "General Studies > MODERN - History > The Revolutionaries": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "The Revolutionaries"
    },
    "General Studies > MODERN - History > Struggle for Independence": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Struggle for Independence"
    },
    "General Studies > MODERN - History > Socio Religious Reforms": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Socio Religious Reforms"
    },
    "General Studies > MODERN - History > Indian National Congress and Its Sessions": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Indian National Congress and Its Sessions"
    },
    "General Studies > MODERN - History > Muslim league": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Muslim league"
    },
    "General Studies > MODERN - History > LEADERS": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "LEADERS"
    },
    "General Studies > MODERN - History > Miscellaneous": {
        "subject": "General Studies",
        "topic": "MODERN - History",
        "subtopic": "Miscellaneous"
    },
    "General Studies > GEOGRAPHY > Solar system and its planets 290 - 293 01 - 44 44": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Solar system and its planets 290 - 293 01 - 44 44"
    },
    "General Studies > GEOGRAPHY > Longitudes and latitudes": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Longitudes and latitudes"
    },
    "General Studies > GEOGRAPHY > Continents and Oceans": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Continents and Oceans"
    },
    "General Studies > GEOGRAPHY > Neighbouring Countries of India": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Neighbouring Countries of India"
    },
    "General Studies > GEOGRAPHY > Indian Drainage System": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Indian Drainage System"
    },
    "General Studies > GEOGRAPHY > World Drainage System": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "World Drainage System"
    },
    "General Studies > GEOGRAPHY > Minerals and Energy Resources in India": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Minerals and Energy Resources in India"
    },
    "General Studies > GEOGRAPHY > Agriculture": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Agriculture"
    },
    "General Studies > GEOGRAPHY > Soil": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Soil"
    },
    "General Studies > GEOGRAPHY > Crops": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Crops"
    },
    "General Studies > GEOGRAPHY > Vegetation": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Vegetation"
    },
    "General Studies > GEOGRAPHY > Climate": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Climate"
    },
    "General Studies > GEOGRAPHY > Industries": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Industries"
    },
    "General Studies > GEOGRAPHY > NAP/WLS/Biosphere Reserves/VARIOUS INITIATIVES": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "NAP/WLS/Biosphere Reserves/VARIOUS INITIATIVES"
    },
    "General Studies > GEOGRAPHY > Physiographic Division of India": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Physiographic Division of India"
    },
    "General Studies > GEOGRAPHY > Transportation": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Transportation"
    },
    "General Studies > GEOGRAPHY > Population": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Population"
    },
    "General Studies > GEOGRAPHY > Atmosphere": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Atmosphere"
    },
    "General Studies > GEOGRAPHY > Rocks": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Rocks"
    },
    "General Studies > GEOGRAPHY > Mountain": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Mountain"
    },
    "General Studies > GEOGRAPHY > Volcano": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "Volcano"
    },
    "General Studies > GEOGRAPHY > World geography and Map": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "World geography and Map"
    },
    "General Studies > GEOGRAPHY > ENVIRONMENT": {
        "subject": "General Studies",
        "topic": "GEOGRAPHY",
        "subtopic": "ENVIRONMENT"
    },
    "General Studies > POLITY > Constitution": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Constitution"
    },
    "General Studies > POLITY > Sources of Indian Constitution": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Sources of Indian Constitution"
    },
    "General Studies > POLITY > Article, Schedule, Parts and list": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Article, Schedule, Parts and list"
    },
    "General Studies > POLITY > Amendments": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Amendments"
    },
    "General Studies > POLITY > DPSP": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "DPSP"
    },
    "General Studies > POLITY > Fundamental Rights and Duties": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Fundamental Rights and Duties"
    },
    "General Studies > POLITY > Committee Reports": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Committee Reports"
    },
    "General Studies > POLITY > Parliament": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Parliament"
    },
    "General Studies > POLITY > President, Vice President and Prime Minister": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "President, Vice President and Prime Minister"
    },
    "General Studies > POLITY > Judiciary": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Judiciary"
    },
    "General Studies > POLITY > Government Bodies": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Government Bodies"
    },
    "General Studies > POLITY > Polity of neighbouring countries": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Polity of neighbouring countries"
    },
    "General Studies > POLITY > Important Case": {
        "subject": "General Studies",
        "topic": "POLITY",
        "subtopic": "Important Case"
    },
    "General Studies > ECONOMICS > Basics of Economy": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Basics of Economy"
    },
    "General Studies > ECONOMICS > Concepts of Demand and Supply": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Concepts of Demand and Supply"
    },
    "General Studies > ECONOMICS > Cost, Production, Consumption and Market": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Cost, Production, Consumption and Market"
    },
    "General Studies > ECONOMICS > National Income, Inflation, Budget,Taxation and GDP": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "National Income, Inflation, Budget,Taxation and GDP"
    },
    "General Studies > ECONOMICS > Money Banking and Financial Institutions": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Money Banking and Financial Institutions"
    },
    "General Studies > ECONOMICS > Navratna / Maharatna / PSUs": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Navratna / Maharatna / PSUs"
    },
    "General Studies > ECONOMICS > International Organisations": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "International Organisations"
    },
    "General Studies > ECONOMICS > Government Schemes": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Government Schemes"
    },
    "General Studies > ECONOMICS > Five - Year Plans": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Five - Year Plans"
    },
    "General Studies > ECONOMICS > LPG": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "LPG"
    },
    "General Studies > ECONOMICS > Indian Economy : Central Problems and Planning": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Indian Economy : Central Problems and Planning"
    },
    "General Studies > ECONOMICS > Stock, Debentures and Foreign trade": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Stock, Debentures and Foreign trade"
    },
    "General Studies > ECONOMICS > Fiscal Policy and Monetary Policy": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Fiscal Policy and Monetary Policy"
    },
    "General Studies > ECONOMICS > Miscellaneous": {
        "subject": "General Studies",
        "topic": "ECONOMICS",
        "subtopic": "Miscellaneous"
    },
    "General Studies > PHYSICS > Light and Optics": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Light and Optics"
    },
    "General Studies > PHYSICS > Heat and Thermodynamics": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Heat and Thermodynamics"
    },
    "General Studies > PHYSICS > Fluid Mechanics": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Fluid Mechanics"
    },
    "General Studies > PHYSICS > Electric Current and Its Effects": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Electric Current and Its Effects"
    },
    "General Studies > PHYSICS > LAWS": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "LAWS"
    },
    "General Studies > PHYSICS > Force and Pressure": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Force and Pressure"
    },
    "General Studies > PHYSICS > Sound": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Sound"
    },
    "General Studies > PHYSICS > Gravitation": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Gravitation"
    },
    "General Studies > PHYSICS > Work and Energy": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Work and Energy"
    },
    "General Studies > PHYSICS > Wave": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Wave"
    },
    "General Studies > PHYSICS > Radioactivity": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Radioactivity"
    },
    "General Studies > PHYSICS > Discoveries": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Discoveries"
    },
    "General Studies > PHYSICS > Units and Measurements": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Units and Measurements"
    },
    "General Studies > PHYSICS > Miscellaneous": {
        "subject": "General Studies",
        "topic": "PHYSICS",
        "subtopic": "Miscellaneous"
    },
    "General Studies > CHEMISTRY > Structure of Atom": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Structure of Atom"
    },
    "General Studies > CHEMISTRY > COMPOUNDS": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "COMPOUNDS"
    },
    "General Studies > CHEMISTRY > Metals, Non-metals and Alloys": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Metals, Non-metals and Alloys"
    },
    "General Studies > CHEMISTRY > Acid, Bases and Salt": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Acid, Bases and Salt"
    },
    "General Studies > CHEMISTRY > Metallurgy": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Metallurgy"
    },
    "General Studies > CHEMISTRY > Organic Chemistry": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Organic Chemistry"
    },
    "General Studies > CHEMISTRY > Periodic table": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Periodic table"
    },
    "General Studies > CHEMISTRY > Ideal Gas Law": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Ideal Gas Law"
    },
    "General Studies > CHEMISTRY > Chemical Properties": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Chemical Properties"
    },
    "General Studies > CHEMISTRY > Solutions": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Solutions"
    },
    "General Studies > CHEMISTRY > Chemistry in Everyday life": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Chemistry in Everyday life"
    },
    "General Studies > CHEMISTRY > Discoveries": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Discoveries"
    },
    "General Studies > CHEMISTRY > Common Name": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Common Name"
    },
    "General Studies > CHEMISTRY > Miscellaneous": {
        "subject": "General Studies",
        "topic": "CHEMISTRY",
        "subtopic": "Miscellaneous"
    },
    "General Studies > BIOLOGY > Scientific Name": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Scientific Name"
    },
    "General Studies > BIOLOGY > Nutrition in Animals": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Nutrition in Animals"
    },
    "General Studies > BIOLOGY > Nutrition in plants": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Nutrition in plants"
    },
    "General Studies > BIOLOGY > Deficiency and Diseases": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Deficiency and Diseases"
    },
    "General Studies > BIOLOGY > Reproduction in Animals": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Reproduction in Animals"
    },
    "General Studies > BIOLOGY > Reproduction in Plants": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Reproduction in Plants"
    },
    "General Studies > BIOLOGY > Cell: Basic Unit of life": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Cell: Basic Unit of life"
    },
    "General Studies > BIOLOGY > Sensory Organs": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Sensory Organs"
    },
    "General Studies > BIOLOGY > Circulatory System": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Circulatory System"
    },
    "General Studies > BIOLOGY > Excretory System": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Excretory System"
    },
    "General Studies > BIOLOGY > Endocrine/Exocrine system": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Endocrine/Exocrine system"
    },
    "General Studies > BIOLOGY > Respiratory system": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Respiratory system"
    },
    "General Studies > BIOLOGY > Digestive system": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Digestive system"
    },
    "General Studies > BIOLOGY > Nervous system": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Nervous system"
    },
    "General Studies > BIOLOGY > Skeleton system": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Skeleton system"
    },
    "General Studies > BIOLOGY > Plant Kingdom": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Plant Kingdom"
    },
    "General Studies > BIOLOGY > Animal Kingdom": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Animal Kingdom"
    },
    "General Studies > BIOLOGY > Micro organism": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Micro organism"
    },
    "General Studies > BIOLOGY > Enzymes and Hormones": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Enzymes and Hormones"
    },
    "General Studies > BIOLOGY > Discoveries and vaccines": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Discoveries and vaccines"
    },
    "General Studies > BIOLOGY > Scientific Study": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Scientific Study"
    },
    "General Studies > BIOLOGY > Miscellaneous": {
        "subject": "General Studies",
        "topic": "BIOLOGY",
        "subtopic": "Miscellaneous"
    },
    "COMPUTER AWARENESS > Computer Basics > Organization of a computer": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Organization of a computer"
    },
    "COMPUTER AWARENESS > Computer Basics > Central Processing Unit (CPU)": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Central Processing Unit (CPU)"
    },
    "COMPUTER AWARENESS > Computer Basics > Input/Output devices": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Input/Output devices"
    },
    "COMPUTER AWARENESS > Computer Basics > Computer memory": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Computer memory"
    },
    "COMPUTER AWARENESS > Computer Basics > Memory organization": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Memory organization"
    },
    "COMPUTER AWARENESS > Computer Basics > Backup devices": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Backup devices"
    },
    "COMPUTER AWARENESS > Computer Basics > PORTs": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "PORTs"
    },
    "COMPUTER AWARENESS > Computer Basics > Windows Explorer": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Windows Explorer"
    },
    "COMPUTER AWARENESS > Computer Basics > Keyboard shortcuts": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Computer Basics",
        "subtopic": "Keyboard shortcuts"
    },
    "COMPUTER AWARENESS > Software > Windows Operating System": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Software",
        "subtopic": "Windows Operating System"
    },
    "COMPUTER AWARENESS > Software > Basics of Microsoft Office (MS Word, MS Excel, PowerPoint)": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Software",
        "subtopic": "Basics of Microsoft Office (MS Word, MS Excel, PowerPoint)"
    },
    "COMPUTER AWARENESS > Working with Internet and E-mails > Web Browsing & Searching": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Working with Internet and E-mails",
        "subtopic": "Web Browsing & Searching"
    },
    "COMPUTER AWARENESS > Working with Internet and E-mails > Downloading & Uploading": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Working with Internet and E-mails",
        "subtopic": "Downloading & Uploading"
    },
    "COMPUTER AWARENESS > Working with Internet and E-mails > Managing an E-mail Account": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Working with Internet and E-mails",
        "subtopic": "Managing an E-mail Account"
    },
    "COMPUTER AWARENESS > Working with Internet and E-mails > e-Banking": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Working with Internet and E-mails",
        "subtopic": "e-Banking"
    },
    "COMPUTER AWARENESS > Networking and Cyber Security > Networking devices and protocols": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Networking and Cyber Security",
        "subtopic": "Networking devices and protocols"
    },
    "COMPUTER AWARENESS > Networking and Cyber Security > Network and information security threats (hacking, virus, worms, Trojan, etc.)": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Networking and Cyber Security",
        "subtopic": "Network and information security threats (hacking, virus, worms, Trojan, etc.)"
    },
    "COMPUTER AWARENESS > Networking and Cyber Security > Preventive measures": {
        "subject": "COMPUTER AWARENESS",
        "topic": "Networking and Cyber Security",
        "subtopic": "Preventive measures"
    },
    "Miscellaneous > STATIC GK > IMPORTANT DAYS": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "IMPORTANT DAYS"
    },
    "Miscellaneous > STATIC GK > Appointments": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Appointments"
    },
    "Miscellaneous > STATIC GK > Places": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Places"
    },
    "Miscellaneous > STATIC GK > Arts Personality": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Arts Personality"
    },
    "Miscellaneous > STATIC GK > HEAD QUARTERS": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "HEAD QUARTERS"
    },
    "Miscellaneous > STATIC GK > Arts Awards": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Arts Awards"
    },
    "Miscellaneous > STATIC GK > Musical Instruments": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Musical Instruments"
    },
    "Miscellaneous > STATIC GK > Festivals": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Festivals"
    },
    "Miscellaneous > STATIC GK > DANCES": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "DANCES"
    },
    "Miscellaneous > STATIC GK > Fairs": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Fairs"
    },
    "Miscellaneous > STATIC GK > Songs": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Songs"
    },
    "Miscellaneous > STATIC GK > Painting/dress/Tribes": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Painting/dress/Tribes"
    },
    "Miscellaneous > STATIC GK > First in india/world": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "First in india/world"
    },
    "Miscellaneous > STATIC GK > Sports": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Sports"
    },
    "Miscellaneous > STATIC GK > Books and Authors": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Books and Authors"
    },
    "Miscellaneous > STATIC GK > Famous Personality": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Famous Personality"
    },
    "Miscellaneous > STATIC GK > States G.K": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "States G.K"
    },
    "Miscellaneous > STATIC GK > Organisation": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Organisation"
    },
    "Miscellaneous > STATIC GK > World G.K": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "World G.K"
    },
    "Miscellaneous > STATIC GK > Full forms": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Full forms"
    },
    "Miscellaneous > STATIC GK > Religious Place": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Religious Place"
    },
    "Miscellaneous > STATIC GK > Awards": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Awards"
    },
    "Miscellaneous > STATIC GK > Important events": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Important events"
    },
    "Miscellaneous > STATIC GK > Founders": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Founders"
    },
    "Miscellaneous > STATIC GK > Schemes": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Schemes"
    },
    "Miscellaneous > STATIC GK > DISCOVERIES": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "DISCOVERIES"
    },
    "Miscellaneous > STATIC GK > IUCN RED LIST": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "IUCN RED LIST"
    },
    "Miscellaneous > STATIC GK > THEMES": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "THEMES"
    },
    "Miscellaneous > STATIC GK > Miscellaneous": {
        "subject": "Miscellaneous",
        "topic": "STATIC GK",
        "subtopic": "Miscellaneous"
    },
}


# ===== SUMMARY STATISTICS =====
TAXONOMY_STATS = {
    "TNPSC": 693,
    "BANKING": 227,
    "SSC_RAILWAYS": 686,
}

TOTAL_TRIPLETS = 1606

# ===== HELPER FUNCTIONS =====
def get_taxonomy_for_exam(exam_type: str):
    """Get taxonomy constants for a specific exam type"""
    exam_map = {
        "TNPSC": {
            "subjects": TNPSC_SUBJECTS,
            "triplets": TNPSC_TRIPLETS,
            "triplet_dict": TNPSC_TRIPLET_DICT
        },
        "Banking": {
            "subjects": BANKING_SUBJECTS,
            "triplets": BANKING_TRIPLETS,
            "triplet_dict": BANKING_TRIPLET_DICT
        },
        "SSC-Railways": {
            "subjects": SSC_RAILWAYS_SUBJECTS,
            "triplets": SSC_RAILWAYS_TRIPLETS,
            "triplet_dict": SSC_RAILWAYS_TRIPLET_DICT
        }
    }
    return exam_map.get(exam_type)
