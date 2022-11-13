import requests
response2 = requests.get ("https://en.wikipedia.org")
#takes us to the main page
# https://en.wikipedia.org/wiki/Main_Page
#http 301 redirect takes us to the orginal url where our informations are stored
print(response2.url)
print(response2.history)#gives the redirect history
#[<Response [301]>]
##3