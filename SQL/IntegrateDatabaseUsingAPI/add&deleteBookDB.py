import requests
from SQL.IntegrateDatabaseUsingAPI.payloadDB import *
from SQL.IntegrateDatabaseUsingAPI.resourceDB import *
query ='select * from apidevelop.books '

#ADD BOOK
url=getConfig()["API"]["endpoint"]+ApiResources.addBook
addBook_response=requests.post(url,json=buildPayloadFromDB(query),)
print(addBook_response.json())
json_response=addBook_response.json()
bookID=json_response["ID"]

#Delete Book
url2=getConfig()["API"]["endpoint"]+ApiResources.deleteBook
deleteBook=requests.post(url2,json={"ID":bookID})


