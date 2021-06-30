from . import server
import fitz
from typing import Dict
import os

@server.command
def decrypt_pdf(data: Dict):
    doc = fitz.open(data["input_file"])
    type = doc.authenticate(data["password"])
    doc.save(data["output_file"] + "_tmp", garbage = 3)
    doc.close()
    try:
        os.remove(data["output_file"])
    except:
        pass
    os.rename(data["output_file"] + "_tmp", data["output_file"])
    return {
        "output_file": data["output_file"]
    }