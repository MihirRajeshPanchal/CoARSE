from fastapi import APIRouter
from fastapi import UploadFile, File, HTTPException

from coarse.services.pdfparse import extract_sections_from_paper

router = APIRouter()

@router.post("/pdfparse")
async def pdf_parser_endpoint(file: UploadFile = File(...)):
    try:
        result = await extract_sections_from_paper(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the PDF: {str(e)}")