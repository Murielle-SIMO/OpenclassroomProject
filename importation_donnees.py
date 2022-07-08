import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#Voir le code html source
print(page.content)

titres = soup.find_all("a", class_="gem-c-document-list__item-title")

for title in titres:
    print (title.string)