import requests
from SQL.IntegrateDatabaseUsingAPI.payloadDB import *
from Utilities.configuration import getConfig
from Utilities.resources import *
query ="select * from apidevelop.books"

#ADD BOOK
url=getConfig()["API"]["endpoint"]+ApiResources.addBook
headers={"Content-Type":"application/json"}
addBook_response=requests.post(url,json=buildPayloadFromDB(query),headers=headers)
print(addBook_response.json())
json_response=addBook_response.json()
bookID=json_response["ID"]
print(bookID)
#Delete Book
url2=getConfig()["API"]["endpoint"]+ApiResources.deleteBook
deleteBook_response=requests.post(url2,json={"ID":bookID})

json_response2=deleteBook_response.json()
print(json_response2["msg"]

