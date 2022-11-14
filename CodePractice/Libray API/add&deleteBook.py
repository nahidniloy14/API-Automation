#http://216.10.245.166/Library/GetBook.php?AuthorName=somename---Query Parameter
#http://216.10.245.166/Library/GetBook.php/AuthorName=somename---Form Parameter
import json

import requests

from payoad import payload

response=requests.get("http://216.10.245.166/Library/GetBook.php",
             params={'AuthorName':'Rahul Shetty2'},) #params take the parameter as dictionary
print(response.text)
#JSON method
j=json.loads(response.text)#loads method parse json string and it returns dictionary
print(j[2])
#request library
j=response.json()
print(j[1])
print(response.status_code)#200

print(response.headers)#{'Date': 'Mon, 20 Jun 2022 14:22:02 GMT', 'Server': 'Apache', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST',
print(response.headers['Date'])#Mon, 20 Jun 2022 14:22:02 GMT
assert (response.headers['Server']) == 'Apache'
#find books named----Rest API Using HashMap
response2=requests.get("http://216.10.245.166/Library/GetBook.php",
             params={'AuthorName':'Rahul Shetty'},)
j2=response2.json()
#print(j2)
for books in j2:
    if books['book_name'] == "Rest API Using HashMap":
        print(books)
        break
    #{'book_name': 'Rest API Using HashMap', 'isbn': 'fdfsf', 'aisle': '89456'}

#assertion
expectedBook= {
        "book_name": "Rest API Using HashMap",
        "isbn": "fdfsf",
        "aisle": "89456"
    }
print(expectedBook)
assert books == expectedBook
# post/add a book
response3= requests.post('http://216.10.245.166/Library/Addbook.php',json={
{
"name":"Learn Appium Automation with Java",
"isbn":"bcd",
"aisle":"227",
"author":"John foe"
}

},headers=#headers not mendatory
{"Connection":'keep-alive'}
)

j3=response3.josn()
print(j3)
#{'Msg':'"Successfilly Added','BookID':"124511"}
bookID=j3['BookID']
#another method to post
response4= requests.post('http://216.10.245.166/Library/Addbook.php',json=payload())


#Delete Book
deleteBook=requests.post("http://216.10.245.166/Library/DeleteBook.php",json={
    "ID":bookID

})
assert deleteBook.status_code == 200
print(deleteBook)
#{msg: book is successfully deleted”}
print(deleteBook['msg'])
#book is successfully deleted
assert deleteBook['msg'] == 'book is successfully deleted'


