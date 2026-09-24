from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai_core.gemini_generator import GeminiDocumentGenerator


router = APIRouter()

# Initialize Gemini generator
try:
    gemini_generator = GeminiDocumentGenerator()
except Exception as e:
    gemini_generator = None
    gemini_error = str(e)


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    effective_date: str


@router.get("/")
def home():
    return {
        "message": "LegalEase API is running"
    }


@router.post("/generate")
def generate_document(request: DocumentRequest):

    if gemini_generator is None:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini initialization failed: {gemini_error}"
        )

    try:

        document_content = (
            gemini_generator.generate_document(
                document_type=request.document_type,
                parties=request.parties,
                terms=request.terms,
                effective_date=request.effective_date,
            )
        )

        return {
            "document_type": request.document_type,
            "parties": request.parties,
            "terms": request.terms,
            "effective_date": request.effective_date,
            "content": document_content,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Document generation failed: {str(e)}"
        )