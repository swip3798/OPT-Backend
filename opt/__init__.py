import EasyEmbed as EE

server = EE.HttpCommandServer(version="0.5.0")

from .merge import merge_files
from .thumbnails import render_doc_thumbnail, render_page_thumbnails
from .page_select import select_pages
from .encrypt import encrypt_pdf
from .deflate import compress_pdf
from .docinfo import get_docinfo
from .decrypt import decrypt_pdf
from .img2pdf import convert_img2pdf