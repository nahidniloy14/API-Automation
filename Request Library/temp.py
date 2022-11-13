#We can access the cookies in the server using a python dictionary
#To send our own cookies we can send our own parameters
import json

import requests
#get request and basic funcionalities
response=requests.get("https://docs.python.org/3/")


print ( response.cookies )#retuens the raw binary data


print(response.ok)#returns true if the request is successful



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
# response8 = requests.post ('https://httpbin.org/post',data ={'Name':'Niloy'})
# print (response8.text )
# "form": {
#     "Name": "Niloy"
# },
#post technique 3
# response9 = requests.post ('https://httpbin.org/post',json ={'Name':'Niloy'})
# print (response9.text )
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
