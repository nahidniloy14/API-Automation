import requests

response6 = requests.get ('https://httpbin.org/delay/3',timeout=10) #3 seconds delay with 10 seconds timeout
print(response6)
