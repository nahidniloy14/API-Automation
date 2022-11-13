import requests

url="https://httpbin.org/post"
#post will receive data from a form
csvfile=[
    ('copy1',('Postman.csv',open('Postman.csv','rb'),'csv')),
    ('copy2',('Postman.csv',open('Postman.csv', 'rb'), 'csv'))
]

#to open multiple files we have to use the lsit of tuples
#(identifier,(filename,openfunction(filename,filemode),filetype)
# open function has two parameter file name and file mode
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# .........................................................................................
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
r= requests.post(url,files=csvfile)
print(r.status_code)
print(r.url)#will reveal the full url
print(r.status_code)#http response code
print(r.text)#will return the response body which is decoded by the request library
# {
#   "args": {},
#   "data": "",
#   "files": {
#     "file": "Name,Salary,Age\r\nNiloy,1100,24\r\nNahid,1101,25\r\nHassan,1102,26\r\n"
#   },
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "210",
#     "Content-Type": "multipart/form-data; boundary=4b30a5a2e82f767d637cd3a3a68c3da5",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.28.0",
#     "X-Amzn-Trace-Id": "Root=1-62a74a8d-70cac8d70803002b0522dca9"
#   },
#   "json": null,
#   "origin": "103.170.172.202",
#   "url": "https://httpbin.org/post"
# }

# headers will pass the http request
# args will show the parameters
#the dictionary past through the post request is submitted to our server and shown in the form object within the response body

