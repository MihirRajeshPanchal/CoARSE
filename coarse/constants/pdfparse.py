from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter

PDF_PARSER_PROMPT = ChatPromptTemplate.from_template("""
You are an AI specialized in analyzing scientific papers.

You'll be given chunks of a scientific paper. Your task is to:
1. Identify the sections present in the text
2. Extract the complete content for each identified section
3. Don't miss any section, even if it is empty

The possible sections are:
ABS = "Abstract"
INT = "Introduction"
RWK = "Related Works"
PDI = "Problem Definition/Idea"
DAT = "Data/Datasets"
MET = "Methodology"
EXP = "Experiments"
RES = "Results"
TNF = "Tables & Figures"
ANA = "Analysis"
FWK = "Future Work"
OAL = "Overall"
BIB = "Bibliography"
EXT = "External"

Paper text:
{text}

Provide your output as a JSON object with section codes as keys and content as values. Format:
```json
{{
  "ABS": "content of the abstract...",
  "INT": "content of the introduction...",
  ...
}}
```

Only include sections that are clearly present in the text. If content doesn't fit any section, include it under "EXT".
""")