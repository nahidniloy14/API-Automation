import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find?q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content,'html.parser')
# this BeautifulSoup method will help us to retrive all the content using the response object
# data.content will render the data present in the url
# html.parser will parse the content in html standard

print(soup.prettify())
# pretify() is a bs4 syntax to print output

moviesTable = soup.find('table', {'class': 'findList'})
print(moviesTable.prettify())
# soup.find(tagname,attribute)
# soup.find will print single result or the first row

rows = moviesTable.findAll('tr')
# finaall will print all the results available with the tag name

documentaryMovies=[] #is used inside the loop
for i in rows:
    rowdata = i.findAll('td')
    print(rowdata[1].a.text)
    # tag a is unique
    # .text will extract text
    nextUrl=rowdata[1].a['href']
    #it will extract the href attribute value
    nextUrlData=requests.get("https://www.imdb.com"+nextUrl)

    soup2=BeautifulSoup(nextUrlData.content,'html.parser')
    # put the if condition if you see non-type error
    if soup2.find('div',{'class':'ipc-metadata-list-item__content-container'}):
        genre=soup2.find('div',{'class':'ipc-metadata-list-item__content-container'})
        print(genre.a.text)
    # ---------------print all documentary movies-------------
        if genre.a.text=="documentary":
            print(rowdata[1].a.text)#shows movie name
            print(genre.a.text)#shows the genre
            #see the results in a list
            documentaryMovies.append(rowdata[1].a.text)

print(documentaryMovies)# print result in a list


