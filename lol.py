import requests
from bs4 import BeautifulSoup as bs

#tableau final 
result = []

url="https://leagueoflegends.fandom.com/wiki/List_of_champions"
response = requests.get(url)
html = response.content

soup = bs(html, "html.parser")
#the parent page
page = soup.find(attrs={'class' : 'page__main'})

#******************************************Contents of the page in order of display**************************************#
#we are stocking all the values in the result list

#first h1 of page
result.append(page.h1.get_text().strip())
#p for skin
result.append(page.find(attrs={'class' : "dablink"}).get_text())
#p paragraph
result.append(page.p.get_text())
#contents table
result.append(page.find(attrs={'class' : 'toc'}).get_text())
#second h2 of page
result.append(page.find_all('h2', limit=2)[1].get_text().strip())

#avalable_champ table
table = page.find('table')
tr = table.find_all("tr")

for i in tr :
    card = []
    td = i.find_all('td')
    for y in td :
        card.append(y.get_text().strip())
    result.append(card)

#List of all champs table
table = page.find_all('table', limit=2)[1]
tr = table.find_all("tr")

for i in tr :
    card = []
    td = i.find_all('td')
    for y in td :
        card.append(y.get_text().strip())
    result.append(card)
    #print(card)

#first h3 of page
result.append(page.h3.get_text())
#first i of page
result.append(page.i.get_text())
#fifth ul of page
result.append(page.find_all('ul', limit=5)[-1].get_text().strip())
#third h2 of page
result.append(page.find_all('h2', limit=3)[-1].get_text().strip())
#scrapped champs list 
scrapped = page.find(attrs={'class' : 'columntemplate'})
for i in scrapped :
    result.append(i.get_text())
#section named 'Triva'
result.append(page.find_all('h2', limit=4)[-1].get_text().strip())
result.append(page.find_all('ul', limit=7)[-1].get_text().strip())
#section named 'Reference' table
result.append(page.find_all('h2', limit=5)[-1].get_text().strip())
result.append(page.find(attrs={'class' : 'references-small'}).get_text())
result.append(page.find(attrs={'class' : ['navbox-wrapper', 'va-collapsible-content', 'mw-collapsible', 'mw-made-collapsible']}).get_text())


#*****************************************Display of result array ***************************************#
for i in result :
    print(i)


