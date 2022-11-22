import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, "html.parser")
rows = soup.find('table', {'class': 'findSection'})
movielist = rows.findAll('tr')  # all tr

movie = movielist.findAll('td')  # td
movieName = movie[1].a.text  # td#a
link=movie[1].a['href']
print(link)

# ----Using Visible Text----------
movieNameVT = movie.find('a', string='Caterpillar Thriller')
linkVT=(movieNameVT['href'])
print(linkVT)

