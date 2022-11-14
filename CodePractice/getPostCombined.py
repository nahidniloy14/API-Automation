#post request
#checked authentication using url- http://httpbin.org/#/Auth/get_basic_auth__user___passwd_
import requests

payload = {'username':'nahidniloy14','password':'1414'}
response4 = requests.post ('https://httpbin.org/post',data = payload)
login = response4.json ( )
print(login['form'])

response5 =requests.get('http://httpbin.org/basic-auth/nahidniloy14/1414', auth =('nahidniloy14','1414'))
print(response5)
