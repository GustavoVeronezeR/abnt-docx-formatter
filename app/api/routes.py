from fastapi import APIRouter
from models.schemas import DocumentRequest

router = APIRouter()

@router.post("/format")
def format_document(data: DocumentRequest):
    return{
        "status": "received",
        "title": data.title,
        "author": data.author,
        "pages": data.pages
    }