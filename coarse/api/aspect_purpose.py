from fastapi import APIRouter
from fastapi import UploadFile, File, HTTPException

from coarse.services.aspect_purpose import aspect_purpose
from coarse.models.paperobj import PaperObj
from coarse.models.sections_map import SectionMap
from coarse.models.errors import Errors
from coarse.models.aspect_purpose import AspectPurposeOutput
import json
from pprint import pprint
router = APIRouter()

@router.post("/aspect_purpose", response_model=AspectPurposeOutput)
async def aspect_purpose_route(paper_obj: SectionMap):
    try:
        result = await aspect_purpose(paper_obj)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the PDF: {str(e)}")
