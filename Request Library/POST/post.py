#post request is used to submitting data from an html form and uploading files
#psost request allows larger amount of resources to be sent in a single request
# headers will pass the http request
# args will show the parameters
#the dictionary past through the post request is submitted to our server and shown in the form object within the response body


import requests

payload={"firstname":"John","lastname":"Smith"}#dictionary
r=requests.post("https://httpbin.org/post",data=payload)
#post will receive data from a form
# data will convert the payload dictioanry to send to our URL

print(r.url)#will reveal the full url
print(r.status_code)#http response code
print(r.text)#will return the response body which is decoded by the request library
# {
#   "args": {}, 1
#   "data": "",
#   "files": {},
#   "form": {
#     "firstname": "John",
#     "lastname": "Smith"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "29",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.0",
#     "X-Amzn-Trace-Id": "Root=1-62a6f83f-4d2a9aef7e765dbf1e72f5ad"
#   },
#   "json": null,
#   "origin": "103.170.172.202",
#   "url": "https://httpbin.org/post"
# }
#post method 2
response8 = requests.post ('https://httpbin.org/post',data ={'Name':'Niloy'})
print (response8.text )
# "form": {
#     "Name": "Niloy"
# },
#post method 3
response9 = requests.post ('https://httpbin.org/post',json ={'Name':'Niloy'})
print (response9.text )
# "json": {
#     "Name": "Niloy"
# }

