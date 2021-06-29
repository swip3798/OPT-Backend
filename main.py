# Needed in order to run this with pythonw.exe
import sys
if sys.stdout == None:
	sys.stdout = open('log.txt', 'w')
	sys.stderr = open('err.txt', 'w')
from opt import server

server.execute(port = 43512, server = "tornado")