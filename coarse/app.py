from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from coarse.api import healthcheck, pdfparse, typogrammar

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(healthcheck.router)
app.include_router(pdfparse.router)
app.include_router(typogrammar.router)

@app.get("/")
def root():
    """
    Handles the root endpoint and returns a welcome message for the ArgumentPeer API.
    
    Returns:
        A JSON object containing a welcome message.
    """
    return {"message": "Welcome to ArgumentPeer API!"}