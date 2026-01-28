from pydantic import BaseModel

class DocumentRequest(BaseModel):
    title: str
    author: str
    pages: int