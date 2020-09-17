import fitz
import sys

main_doc = fitz.open(sys.argv[1])
insert_doc_names = sys.argv[2:-1]
insert_docs = [fitz.open(i) for i in insert_doc_names]

for i in insert_docs:
    main_doc.insertPDF(i)
main_doc.save(sys.argv[-1], 2)
main_doc.close()