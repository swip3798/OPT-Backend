import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"excludes": ["tkinter", "pytz", "unittest", "html", "http", "numpy", "pydoc_data", "email", "logging", "PIL"]}

setup(  name = "PDF Toolkit",
        version = "0.1",
        description = "PDF Toolkit using PyMuPDF!",
        options = {"build_exe": build_exe_options},
        executables = [
            Executable("renderimages.py", base=None), 
            Executable("renderthumbnails.py", base=None),
            Executable("mergedoc.py", base=None),
            Executable("pageselect.py", base=None),
            Executable("deflate.py", base=None),
            Executable("docinfo.py", base=None),
        ])