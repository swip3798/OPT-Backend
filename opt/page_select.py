from . import server
import os
import fitz

@server.command
def select_pages(data):
    doc = fitz.open(data["input_file"])
    page_sequence = data["pages"]
    doc.select(page_sequence)
    doc.save(data["output_file"] + "_tmp", garbage = 3, )
    doc.close()
    os.rename(data["output_file"] + "_tmp", data["output_file"])
    return {
        "output_file": data["output_file"]
    }