from . import server
import fitz

@server.command
def merge_files(data):
    files = data["input_files"]
    docs = [fitz.open(filename) for filename in files]
    first_doc = docs[0]
    for doc in docs[1:]:
        first_doc.insert_pdf(doc)
    first_doc.save(data["output_file"], garbage = 3)
    for doc in docs:
        doc.close()
    return {
        "output_file": data["output_file"]
    }