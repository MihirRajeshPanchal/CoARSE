from fastapi import APIRouter
from fastapi import UploadFile, File, HTTPException

from coarse.services.typo_grammar_agent import check_typo_grammar
from coarse.models.paperobj import PaperObj
from coarse.models.sections_map import SectionMap
from coarse.models.errors import Errors

router = APIRouter()

@router.post("/typogrammar", response_model=Errors)
async def typo_grammar(paper_obj: SectionMap):
    """
    Handles POST requests to check a paper for typos and grammar issues.
    
    Accepts a PaperObj payload, performs typo and grammar checking, and returns the result. Raises an HTTP 500 error if processing fails.
    """
    try:
        result = await check_typo_grammar(paper_obj.root)
        return result  # no .dict() here
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the PDF: {str(e)}")
