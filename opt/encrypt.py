from . import server
import fitz
from typing import Dict
import os

@server.command
def encrypt_pdf(data: Dict):
    doc = fitz.open(data["input_file"])
    owner_pw = data.get("owner_pw")
    user_pw = data["user_pw"]
    doc.save(data["output_file"] + "_tmp", garbage = 3, encryption = fitz.PDF_ENCRYPT_AES_256, owner_pw = owner_pw, user_pw = user_pw)
    doc.close()
    try:
        os.remove(data["output_file"])
    except:
        pass
    os.rename(data["output_file"] + "_tmp", data["output_file"])
    return {
        "output_file": data["output_file"]
    }