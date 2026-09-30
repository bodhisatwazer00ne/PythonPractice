import sys

#sys.argv is used in Python to get command-line arguments — the values you pass when running a Python script from the terminal.

try:
    print("Hello , ",sys.argv[1]) #in command line python prog14.py Alice
except IndexError:
    print("python prog14.py <name>")

print(sys.argv[0]) #name of the script

#sys.exit() is used to exit from Python 


for arg in sys.argv[1:-2]: #splice the list to get all arguments except the first one (the script name) and the last two (if any)
    print("Hello ",arg)