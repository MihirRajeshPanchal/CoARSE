from fastapi import APIRouter
from fastapi import UploadFile, File, HTTPException

from coarse.services.typo_grammar_agent import check_typo_grammar
from coarse.models.paperobj import PaperObj

router = APIRouter()

@router.post("/typogrammar")
async def typo_grammar(paper_obj: PaperObj):
    try:
        result = await check_typo_grammar(paper_obj)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the PDF: {str(e)}")