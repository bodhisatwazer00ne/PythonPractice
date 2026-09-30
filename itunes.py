#API Application Programming Interface 
#JSON JavaScript Object Notation

#The requests library in Python is used to send HTTP requests (like getting data from websites or APIs)

import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])
print(response.json())#json method of response object converts the JSON data into a Python dictionary/object
print(json.dumps(response.json(),indent=2)) #pretty print json data...indent=2 means 2 spaces for indentation 
#json.dumps() is used in Python to convert a Python object into a JSON-formatted string

o=response.json()
for result in o["results"]:
    print(result["trackName"])
