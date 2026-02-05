from pydantic import BaseModel

class DocxUploadResponse(BaseModel):
    filename: str
    raw_text: str
    paragraphs: list[str]