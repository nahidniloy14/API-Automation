#We can access the cookies in the server using a python dictionary
#To send our own cookies we can send our own parameters
import requests
res=requests.get("https://httpbin.org/cookies")
print ( res.cookies )
# <RequestsCookieJar[]>
# To create our own cookie
cookies = dict ( key1 ='value1')
res = requests.get ('https://httpbin.org/cookies',cookies = cookies )
print ( res.text )
# {
#   "cookies": {
#     "key1": "value1"
#   }
# }

url="http://rahulshettyacademy.com"
visitMonthCookie={"visit-month":"March"}

response=requests.get(url,cookies=visitMonthCookie)
print(response.status_code)


