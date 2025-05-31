from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter

TYPO_GRAMMAR_PROMPT = ChatPromptTemplate.from_template("""
You are an AI specialized in typos and grammatical mistakes in scientific paper.

You'll be given a JSON object with key value pairs.
                                                       
Keys are sections code, showing various sections.
The possible sections code are:
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

And value will be the content inside the sections of the paper.
Paper JSON Format:
```json
{{
  "ABS": "content of the abstract...",
  "INT": "content of the introduction...",
  ...
}}
```                                    

JSON Object:
{paper_obj}

Every error are of two types with error codes:
TYP: "Typo"
GMR: "Grammatical Errors"                                                       

Every error should be represented in a form of dictionary with two key value pairs:
```json                                                    
{{
    "INC": "incorrect text from the section",
    "SEC": "section code of the paper where error occured",
    "CRT": "corrected text to replace the incorrected text"
}}
```
                                                       
Provide your output as a JSON object with error codes as keys and an array of dictionaries of error as values. Format:
```json
{{
  "TYP": [
        {{
            "INC": "incorrect text from the section",
            "SEC": "section code of the paper where error occured",
            "CRT": "corrected text to replace the incorrected text"                                          
        }},
        ...                                              
    ]
  "GMR": [
        {{
            "INC": "incorrect text from the section",
            "SEC": "section code of the paper where error occured",
            "CRT": "corrected text to replace the incorrected text"                                          
        }},
        ...                                              
    ]
}}
```

Check for errors in all the sections, and include the incorrect, corrected and section code properly for each error. Don't missout on any section, even if it is empty.
""")