from . import server
import fitz
import base64 as b64

@server.command
def render_doc_thumbnail(data):
    doc = fitz.open(data["input_file"])
    pix = doc[0].getPixmap(alpha = False)
    pix.shrink(2)
    data = pix.tobytes()
    return {
        "thumbnail": b64.b64encode(data).decode("ascii"),
        "format": "b64"
    }

@server.command
def render_page_thumbnails(data):
    doc = fitz.open(data["input_file"])
    thumbs = []
    for page in doc:
        pix = page.getPixmap(alpha = False)
        pix.shrink(2)
        data = pix.tobytes()
        thumbs.append(b64.b64encode(data).decode("ascii"))
    return {
        "thumbnails": thumbs,
        "format": "b64"
    }