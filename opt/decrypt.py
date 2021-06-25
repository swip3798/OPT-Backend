from . import server
import fitz
from typing import Dict

@server.command
def decrypt_pdf(data: Dict):
    doc = fitz.open(data["input_file"])
    type = doc.authenticate(data["password"])
    doc.save(data["output_file"], garbage = 3)
    doc.close()
    return {
        "output_file": data["output_file"]
    }