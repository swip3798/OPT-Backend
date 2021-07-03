# Needed in order to run this with pythonw.exe
import sys
import os
if sys.stdout == None:
	sys.stdout = open(os.devnull, 'w')
	sys.stderr = open(os.devnull, 'w')
from opt import server

server.execute(port = 43512, server = "tornado")