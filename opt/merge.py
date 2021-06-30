from . import server
import fitz
import os

@server.command
def merge_files(data):
    files = data["input_files"]
    docs = [fitz.open(filename) for filename in files]
    first_doc = docs[0]
    for doc in docs[1:]:
        first_doc.insert_pdf(doc)
    first_doc.save(data["output_file"] + "tmp", garbage = 3)
    for doc in docs:
        doc.close()
    try:
        os.remove(data["output_file"])
    except:
        pass
    os.rename(data["output_file"] + "_tmp", data["output_file"])
    return {
        "output_file": data["output_file"]
    }