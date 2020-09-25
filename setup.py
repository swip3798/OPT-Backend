import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "pytz", "unittest", "html", "http", "numpy", "pydoc_data", "email", "logging", "PIL"],
    "include_files": [
        ["TPL/cx_Freeze"]*2,
        ["TPL/MuPDF"]*2,
        ["TPL/PyMuPDF"]*2,
        ["TPL/Python"]*2,
        "LICENSE"
    ]
}

setup(  name = "OPT-Backend",
        version = "0.3.0",
        description = "PDF manipulation backend of OPT using PyMuPDF!",
        options = {"build_exe": build_exe_options},
        executables = [
            Executable("renderimages.py", base=None), 
            Executable("renderthumbnails.py", base=None),
            Executable("mergedoc.py", base=None),
            Executable("pageselect.py", base=None),
            Executable("deflate.py", base=None),
            Executable("docinfo.py", base=None),
            Executable("getdir.py", base=None),
        ])