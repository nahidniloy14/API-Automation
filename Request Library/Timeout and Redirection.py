import requests
response2 = requests.get ("https://en.wikipedia.org")
#takes us to the main page
# https://en.wikipedia.org/wiki/Main_Page
#http 301 redirect takes us to the orginal url where our informations are stored
print(response2.url)
print(response2.history)#gives the redirect history #[<Response [301]>]
print(response2.status_code)#200
#[<Response [301]>]
response3 = requests.get ("https://en.wikipedia.org",allow_redirects=False)
print(response3.url)#https://en.wikipedia.org/
print(response3.history)#gives the redirect history
print(response3.status_code)#301 #[]

response3 = requests.get ("https://en.wikipedia.org",timeout=2)
#to wait 2s and grab the response

