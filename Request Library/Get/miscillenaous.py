#get request is used to render a list of data or filter a list of data based on query string
import requests
payload={"firstname":"John","lastname":"Smith"}
r=requests.get("https://httpbin.org/get",params=payload)
#httpbin.org---Base URL
#/get-----
#htttps://httpbin.org/get?firstname="John"
#firstname="John"----query string
#firstname----parameter name
#value-----John
print(r.url)#will reveal the full url #htttps://httpbin.org/get?firstname="John"
print(r.status_code)#http response code
print(r.content)#will turn the response body into bytes
# b'{\n  "args": {\n    "firstname": "John", \n    "lastname": "Smith"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.28.0", \n    "X-Amzn-Trace-Id": "Root=1-62a6e2b3-45e7388414745b3951b52efd"\n  }, \n  "origin": "103.170.172.202", \n  "url": "https://httpbin.org/get?firstname=John&lastname=Smith"\n}\n'
print(r.text)#will return the response body which is decoded by the request library
# {
#   "args": {
#     "firstname": "John",
#     "lastname": "Smith"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.0",
#     "X-Amzn-Trace-Id": "Root=1-62a6e357-56858a816f64650825595a21"
#   },
#   "origin": "103.170.172.202",
#   "url": "https://httpbin.org/get?firstname=John&lastname=Smith"
# }
# headers will pass the http request
# args will show the parameters
print(r.ok)#returns true if the request is successful


