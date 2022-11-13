import requests

response3 = requests.get ("https://jsonplaceholder.typicode.com/users")
j=response3.json() #retrive JSON
print(j[0])
print(j[0]['name'])