#JSON decoder allows us to parse the JSON response into python objects
#JSON stands for javascript object notation
#JSON is a easy adn light format between the server and a client
import requests
data = {'firstName':'John'}
r = requests.post ('https://httpbin.org/post',json = data)
print ( r.text )
# {
#   "args": {}, 
#   "data": "{\"firstName\": \"John\"}",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "21",
#     "Content-Type": "application/json",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.0",
#     "X-Amzn-Trace-Id": "Root=1-62a8a352-3d3a09065f28dbc341c4e007"
#   },
#   "json": {
#     "firstName": "John"
#   },
#   "origin": "103.170.172.202",
#   "url": "https://httpbin.org/post"
# }
