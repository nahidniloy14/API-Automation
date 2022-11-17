#http://216.10.245.166/Library/GetBook.php?AuthorName=somename---Query Parameter
#http://216.10.245.166/Library/GetBook.php/AuthorName=somename---Form Parameter
import requests
import json
from payload import *
from Utilities.resources import *
from Utilities.configuration import *
#ADD BOOK

#Pre PMO Execution
# response=requests.get("http://216.10.245.166/Library/GetBook.php",
#              params={'AuthorName':'Rahul Shetty2'},) #params take the parameter as dictionary

#------------------------------------PMO EXECUTION STARTED------------------------------------------------------------
#Step 1
# config=configparser.ConfigParser() #this config variable can now drive all our ini files
# config.read("CodePractice/Libray API/Utilities/properties.ini")#copy the path of the ini file
# response=requests.get(config["API"]["endpoint"]+"/Library/GetBook.php",
#              params={'AuthorName':'Rahul Shetty2'},)
#Step 2
# config=getConfig()
# response=requests.get(config["API"]["endpoint"]+"/Library/GetBook.php",
#              params={'AuthorName':'Rahul Shetty2'},)
#step 3
# response=requests.get(getConfig()["API"]["endpoint"]+"/Library/GetBook.php", #directly getConfig() method is called
#              params={'AuthorName':'Rahul Shetty2'},)
#step 4

# response=requests.get(getConfig()["API"]["endpoint"]+ApiResources.addBook,
#              params={'AuthorName':'Rahul Shetty2'},)

#step 5
# url=getConfig()["API"]["endpoint"]+ApiResources.addBook
# response=requests.get(url,params={'AuthorName':'Rahul Shetty2'},)

#step 6
url=getConfig()["API"]["endpoint"]+ApiResources.addBook
dictionary =params={'AuthorName':'Rahul Shetty2'}

response=requests.get(url,dictionary,)
print(response.text)
j=json.loads(response.text)#JSON method#loads method parse json string and it returns dictionary
print(j[2])
j=response.json()
print(j[1])
print(response.status_code)#200
print(response.headers)#{'Date': 'Mon, 20 Jun 2022 14:22:02 GMT', 'Server': 'Apache', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST',
print(response.headers['Date'])#Mon, 20 Jun 2022 14:22:02 GMT
assert (response.headers['Server']) == 'Apache'



#find books named----Rest API Using HashMap
response2=requests.get("url",params={'AuthorName':'Rahul Shetty'},)
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
response3= requests.post(url,json={
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
response4= requests.post('url',json=payload())

#Delete Book
url2="getConfig()+ApiResources.deleteBook"
deleteBook=requests.post(url2,json={"ID":bookID})

assert deleteBook.status_code == 200
print(deleteBook)
#{msg: book is successfully deleted”}
print(deleteBook['msg'])

#book is successfully deleted
assert deleteBook['msg'] == 'book is successfully deleted'


