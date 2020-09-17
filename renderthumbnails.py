import fitz
import sys

doc = fitz.open(sys.argv[1])
if len(sys.argv) > 2:
    directory = sys.argv[2]
else:
    directory = "./"

for page in doc:  # iterate through the pages
    pix = page.getPixmap(alpha = False)  # render page to an image
    pix.shrink(2)
    pix.writePNG(directory + "%i.png" % page.number)   # store image as a PNG

