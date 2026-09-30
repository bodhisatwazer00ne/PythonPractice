#pip is a package manager for Python. It allows you to install and manage additional libraries and dependencies 
# that are not included in the standard Python library. 
# You can use pip to install packages from the Python Package 

import cowsay
import sys

if len(sys.argv) ==2:
    cowsay.cow("Hello, "+sys.argv[1])
    cowsay.trex("Hello, "+sys.argv[1])