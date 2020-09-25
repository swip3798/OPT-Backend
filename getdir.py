# For debugging purposes

import os
import sys

try:
    print(os.path.realpath(__file__))
except:
    pass

try:
    print(sys.argv[0])
except:
    pass

try:
    print(os.path.realpath(sys.argv[0]))
except:
    pass