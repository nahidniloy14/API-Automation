#We can access the cookies in the server using a python dictionary
#To send our own cookies we can send our own parameters
import json

import requests
#get request and basic funcionalities
# response=requests.get("https://docs.python.org/3/")
#
# # print(response.text)
# # print(response.status_code)
# # print ( response.cookies )#retuens the raw binary data
# # print(response.content)
# # print(response.text)#will decode the binary data to html format
# # print(response.headers)
# # print(response.headers['Content-Length'])
#print(dir(response))#It will show the attribute and method we can use
# ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

# print(response.ok)#returns true if the request is successful
# response2 = requests.get ("https://en.wikipedia.org")
# #takes us to the main page
# # https://en.wikipedia.org/wiki/Main_Page
# #http 301 redirect takes us to the orginal url where our informations are stored
# print(response2.url)
# print(response2.history)#gives the redirect history
# #[<Response [301]>]
#
# response3 = requests.get ("https://jsonplaceholder.typicode.com/users")
# j=response3.json() #retrive JSON
# print(j[0])

#post request
#checked authentication using url- http://httpbin.org/#/Auth/get_basic_auth__user___passwd_
#post technique 1
# payload = {'username':'nahidniloy14','password':'1414'}
# response4 = requests.post ('https://httpbin.org/post',data = payload)
# login = response4.json ( )
# print(login['form'])
#
# response5 =requests.get('http://httpbin.org/basic-auth/nahidniloy14/1414', auth =('nahidniloy14','1414'))
# print(response5)
# #will retuen the status code

#post technique 2
response8 = requests.post ('https://httpbin.org/post',data ={'Name':'Niloy'})
print (response8.text )
# "form": {
#     "Name": "Niloy"
# },
#post technique 3
response9 = requests.post ('https://httpbin.org/post',json ={'Name':'Niloy'})
print (response9.text )
# "json": {
#     "Name": "Niloy"
# }

#post technique 4
data = {'username':'nahidniloy14'}
res = requests.post ('https://httpbin.org/post',data=json.dumps(data))
print ( res.text )


#
# response6 = requests.get ('https://httpbin.org/delay/3',timeout=10) #3 seconds delay with 10 seconds timeout
# print(response6)
#
import json
courses = '{"name": "RahulShetty","languages": [ "Java", "Python"]}'
#the courses is a string and it is holding our JSON variable

#Loads method parse json string and it returns dictionary
#json.loads(courses)
dictionary_courses=json.loads(courses)
print(type(dictionary_courses))
# type will tell us the data type which we passed inside it
#output: <class 'dict'>
print(dictionary_courses)
#output: {'name': 'RahulShetty', 'languages': ['Java', 'Python']}
# 'name' and 'languages' are key and 'RahulShetty' 'Java' 'Python' is the value
# 'RahulShetty' is a string and ['Java', 'Python'] is a list
print(dictionary_courses['name'])
#output: RahulShetty
list_languages=dictionary_courses['languages']
print(list_languages)
#output: ['Java', 'Python']
print(list_languages[0])
#output: Java

