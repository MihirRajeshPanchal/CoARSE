from langchain_core.prompts import ChatPromptTemplate
from langchain.text_splitter import CharacterTextSplitter

SIGNIFICANCE_PROMPT = ChatPromptTemplate.from_template("""
You are an AI specialized in labeling the significance each section of a scientific paper.

You'll be given a JSON object with an array of aspect-purpose dictionaries, containing aspect label, purpose label and section code with the content of the section for each section.
                                                       
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
                       
Input Format:
```json
{[
    {
        "ASP": "aspect label for the section",
        "PUR": "purpose label for the section",
        "<SECTION CODE>": "content of the section"                                                               
    },
    ...                                                    
]}
```                                    

JSON Object:
{aspect_purpose_json}

You will be labellling each section with a label of significance.
  
The possible significance labels are:
MAJ = "Major Comment"
MIN = "Minor Comment"
GEN = "General Comment"                                            

You have to add a key value to every dictionary for every section. Key should be SIG and value shoud be one of the significance label.     
                                                                                                      
Every section should be of following format:
```json
{{
    "ASP": "aspect label for the section",
    "PUR": "purpose label for the section",
    "<SECTION CODE>": "content of the section",
    "SIG": "significance label for the section"
}}     
```                                                                                                         
                                                       
Provide your output as an array of aspect-purpose-significance dictionaries for each section. Format:
```json
{[
    {
        "ASP": "aspect label for the section",
        "PUR": "purpose label for the section",
        "ABS": "content of the abstract",                                                               
        "SIG": "significance label for the abstract section"
    },
    ...                                                    
]}
```

Do this for all the section. Don't missout on any section, even if it is empty.
""")