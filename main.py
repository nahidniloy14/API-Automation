import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content,'html.parser')
# this BeautifulSoup method will help us to retrive all the content using the response object
# data.content will render the data present in the url
# html.parser will parse the content in html standard

print(soup.prettify())
# pretify() is a bs4 syntax to print output

