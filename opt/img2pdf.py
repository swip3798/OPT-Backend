from . import server
import fitz

@server.command
def convert_img2pdf(data):
    doc = fitz.open()
    compress = data.get("compress", False)
    for img_filename in data["images"]:
        img = fitz.open(img_filename)
        rect = img[0].rect  # pic dimension
        pdfbytes = img.convert_to_pdf() # make a PDF stream
        img.close()
        imgPDF = fitz.open("pdf", pdfbytes)
        page = doc.new_page(width = rect.width, height = rect.height)
        page.show_pdf_page(rect, imgPDF, 0)
    doc.save(data["output_file"], garbage = 3, clean = True, deflate = compress)
    doc.close()
    return {
        "output_file": data["output_file"],
        "compressed": compress
    }