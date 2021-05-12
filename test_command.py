import os
import json

def call_command_server(command, data):
    data_raw = json.dumps(data).replace('"', '\\"')
    os.system('.\Scripts\python.exe main.py {} "{}"'.format(command, data_raw))

if __name__ == "__main__":
    # call_command_server("merge_files", {"input_files": ["example1.pdf", "example2.pdf"], "output_file": "merge.pdf"})
    # call_command_server("render_doc_thumbnail", {"input_file": "example1.pdf"})
    # call_command_server("render_page_thumbnails", {"input_file": "C:\\Users\\d070527\\Documents\\Private\\Programming\\Python\\OPT-Backend-Rework\\example2.pdf"})
    # call_command_server("select_pages", {"input_file": "C:\\Users\\d070527\\Documents\\Private\\Programming\\Python\\OPT-Backend-Rework\\example2.pdf", "pages": [1,4,7], "output_file": "select.pdf"})
    
    # call_command_server("compress_pdf", {"input_file": "example2.pdf", "output_file": "compress.pdf"})
    # call_command_server("get_docinfo", {"input_file": "example2.pdf"})
    # call_command_server("encrypt_pdf", {"input_file": "example2.pdf", "user_pw": "hello", "owner_pw": "test", "output_file": "encrypt.pdf"})
    # call_command_server("decrypt_pdf", {"input_file": "encrypt.pdf", "password": "hello", "output_file": "decrypt.pdf"})
    call_command_server("convert_img2pdf", {"images": ["img1.jpeg", "img2.jpg"], "output_file": "img.pdf"})

