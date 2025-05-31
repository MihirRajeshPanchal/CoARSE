from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import JsonOutputParser
from fastapi import UploadFile
import os
from coarse.constants.typo_grammar import TYPO_GRAMMAR_PROMPT
from coarse.constants.coarse import llm
from coarse.models.errors import Errors

async def check_typo_grammar(paper_obj):
    """
    Performs typo and grammar checking on the provided paper object using a language model.
    
    Args:
        paper_obj: The paper or text object to be checked for typos and grammatical errors.
    
    Returns:
        An Errors object containing the detected typos and grammar issues.
    """
    chain = TYPO_GRAMMAR_PROMPT | llm | OutputFixingParser.from_llm(parser=JsonOutputParser(pydantic_object=Errors), llm=llm)
    
    errors = await chain.invoke({"paper_obj": paper_obj})
    
    print(errors)
    return errors