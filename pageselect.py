import fitz
import sys

doc = fitz.open(sys.argv[1])
pages = sys.argv[2:]
pages = [int(i) for i in pages]

doc.select(pages)
doc.save("reselect.pdf", 2)
doc.close()