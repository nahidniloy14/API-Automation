#We can access the cookies in the server using a python dictionary
#To send our own cookies we can send our own parameters
import json

import requests
#get request and basic funcionalities
response=requests.get("https://docs.python.org/3/")

print ( response.cookies )#retuens the raw binary data












