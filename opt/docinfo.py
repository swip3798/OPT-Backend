from . import server
import fitz
from typing import Dict

@server.command
def get_docinfo(data: Dict):
    doc = fitz.open(data["input_file"])
    page_count = doc.page_count
    is_encrypted = doc.is_encrypted
    doc.close()
    return {
        "page_count": page_count,
        "is_encrypted": is_encrypted
    }