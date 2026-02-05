from docx import Document

def read_docx(file_path: str) -> dict:
    document = Document(file_path)

    paragraphs = [p.text for p in document.paragraphs if p.text.strip()]

    return {
        "raw_text": "\n".join(paragraphs),
        "paragraphs": paragraphs
    }
