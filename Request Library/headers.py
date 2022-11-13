#when a request is made to the sever the response object contains headers which pass additional information within the request
import requests
headers= {'content - type':'multipart / form - data'} #when a form or file is uploaded to the server using a post request
r = requests.post ('https://httpbin.org/post',headers=headers)
print ( r.headers )
#{'Date': 'Tue, 14 Jun 2022 15:25:52 GMT', 'Content-Type': 'text/html', 'Content-Length': '173', 'Connection': 'keep-alive'}
print ( r.request.headers )
# {'Date': 'Tue, 14 Jun 2022 15:26:17 GMT', 'Content-Type': 'text/html', 'Content-Length': '173', 'Connection': 'keep-alive'}
# {'User-Agent': 'python-requests/2.28.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content - type': 'multipart / form - data', 'Content-Length': '0'}
print ( r.headers['content-type'])
# text/html
