from . import server
import fitz

@server.command
def compress_pdf(data):
    doc = fitz.open(data["input_file"])
    doc.save(data["output_file"], garbage = 4, clean = True, deflate = True)
    doc.close()
    return {
        "output_file": data["output_file"]
    }