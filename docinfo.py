import fitz
import sys

doc = fitz.open(sys.argv[1])
print(doc.pageCount)