from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import router


app = FastAPI(
    title="LegalEase API",
    description="AI-powered legal document drafting API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.include_router(router)


@app.get("/", tags=["System"])
def root():
    return {
        "name": "LegalEase API",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "ok"
    }