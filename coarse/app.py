from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from coarse.api import healthcheck, pdfparse

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

@app.get("/")
def root():
    return {"message": "Welcome to ArgumentPeer API!"}