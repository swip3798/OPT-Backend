import fitz
import sys

doc = fitz.open(sys.argv[1])
pages = sys.argv[2:-1]
pages = [int(i) for i in pages]

doc.select(pages)
doc.save(sys.argv[-1], 2)
doc.close()