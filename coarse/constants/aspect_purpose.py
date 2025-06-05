from langchain_core.prompts import ChatPromptTemplate

ASPECT_PURPOSE_PROMPT = ChatPromptTemplate.from_template("""
You are an AI specialized in labeling the purpose and aspect each section of a scientific paper.

You'll be given a JSON object with key value pairs.
                                                       
Keys are section codes, showing various sections.
The possible section codes are:
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
{{{{  
  "ABS": "content of the abstract...",
  "INT": "content of the introduction..."
}}}}                                  

JSON Object:
{paper_obj}

First you will be dividing each sections into different parts and labelling each part with a purpose label and a sentiment for every aspect label.

The possible purpose labels are:
SMY = "Summary"
SUG = "Suggestion"
DFT = "Deficit"
APC = "Appreciation"
DIS = "Discussion"
QSN = "Question"
CRT = "Criticism"
FBK = "Feedback"

The possible aspect labels are:
APR = "Appropriateness"
NOV = "Originality or Novelty"
IMP = "Significance or Impact"
CMP = "Meaningful Comparison"
PNF = "Presentation & Formatting"
REC = "Recommendation"
EMP = "Empirical & Theoretical Soundness"
SUB = "Substance"
CLA = "Clarity"                                              

You will be ranking each section with every aspect in three categories:
NEG = "Negative"
NEU = "Neutral"
POS = "Positive"

Every annotation dictionary should be in the following format:
```json
{{{{  
   "SEC": "<section_code>",
   "PRT": "part of the section",                                                         
   "PUR": "purpose label for the part of the section",
   "APR": "NEG or NEU or POS",
   "NOV": "NEG or NEU or POS",
   "IMP": "NEG or NEU or POS",
   "CMP": "NEG or NEU or POS",
   "PNF": "NEG or NEU or POS",
   "REC": "NEG or NEU or POS",
   "EMP": "NEG or NEU or POS",
   "SUB": "NEG or NEU or POS",
   "CLA": "NEG or NEU or POS"
}}}}     
                                                       
Provide your output as an array of annotation dictionaries for each part of the section. Format:
```json
{{{{  
[
    {{
      "PUR": "purpose label for the section",
      "<SECTION CODE>": "content of the section",
      "APR": "NEG or NEU or POS",
      "NOV": "NEG or NEU or POS",
      "IMP": "NEG or NEU or POS",
      "CMP": "NEG or NEU or POS",
      "PNF": "NEG or NEU or POS",
      "REC": "NEG or NEU or POS",
      "EMP": "NEG or NEU or POS",
      "SUB": "NEG or NEU or POS",
      "CLA": "NEG or NEU or POS"
    }},
    ...
]
}}}}                                                      

Do this for all the parts of all the sections. Don't miss out on any part or section, even if it is empty.
""")
