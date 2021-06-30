from . import server
import fitz
import os

@server.command
def compress_pdf(data):
    doc = fitz.open(data["input_file"])
    doc.save(data["output_file"] + "_tmp", garbage = 4, clean = True, deflate = True)
    doc.close()
    try:
        os.remove(data["output_file"])
    except:
        pass
    os.rename(data["output_file"] + "_tmp", data["output_file"])
    return {
        "output_file": data["output_file"]
    }