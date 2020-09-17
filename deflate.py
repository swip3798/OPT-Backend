import fitz
import sys

doc = fitz.open(sys.argv[1])
doc.save("deflate.pdf", 3, clean = True, deflate = True)
doc.close()