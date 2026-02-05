from fastapi import APIRouter, UploadFile, File
from app.services.docx_reader import read_docx
from app.core.config import UPLOAD_DIR
from app.models.schemas import DocxUploadResponse
import os

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "API ABNT DOCX Formatter está rodando"}


@router.post("/upload-docx", response_model=DocxUploadResponse)
async def upload_docx(file: UploadFile = File(...)):
    if not file.filename.endswith(".docx"):
        raise ValueError("Apenas arquivos .docx são permitidos")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    data = read_docx(file_path)

    return {
        "filename": file.filename,
        "raw_text": data["raw_text"],
        "paragraphs": data["paragraphs"]
    }
