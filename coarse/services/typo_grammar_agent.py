from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import JsonOutputParser
from coarse.constants.typo_grammar import TYPO_GRAMMAR_PROMPT
from coarse.constants.coarse import llm
from coarse.models.errors import Errors

# Mapping section codes to full section labels
section_code_to_label = {
    "ABS": "Abstract",
    "INT": "Introduction",
    "RWK": "Related Works",
    "PDI": "Problem Definition/Idea",
    "DAT": "Data/Datasets",
    "MET": "Methodology",
    "EXP": "Experiments",
    "RES": "Results",
    "TNF": "Tables & Figures",
    "ANA": "Analysis",
    "FWK": "Future Work",
    "OAL": "Overall",
    "BIB": "Bibliography",
    "EXT": "External"
}

# Function to convert section codes in LangChain output to full section labels
def convert_section_codes(result_dict):
    for err_type in ["TYP", "GMR"]:
        for error in result_dict.get(err_type, []):
            code = error.get("SEC")
            if code in section_code_to_label:
                error["SEC"] = section_code_to_label[code]
    return result_dict

# Final async function
async def check_typo_grammar(paper_obj):
    chain = TYPO_GRAMMAR_PROMPT | llm | OutputFixingParser.from_llm(parser=JsonOutputParser(pydantic_object=Errors), llm=llm)
    
    errors = await chain.invoke({"paper_obj": paper_obj})
    
    print(errors)
    return errors