from . import server
import fitz

@server.command
def select_pages(data):
    doc = fitz.open(data["input_file"])
    page_sequence = data["pages"]
    doc.select(page_sequence)
    doc.save(data["output_file"], garbage = 3)
    doc.close()
    return {
        "output_file": data["output_file"]
    }