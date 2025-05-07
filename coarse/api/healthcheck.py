
from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck_endpoint():
    return {"status": "ok"}