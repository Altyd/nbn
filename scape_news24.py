import requests
from bs4 import BeautifulSoup

url = 'https://www.news24.com' # news24 website obviously
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='article-item--container')

for article in articles:
    title_elem = article.find('div', class_='article-item__title')
    if not title_elem:
        continue
    title = title_elem.text.strip()
    link_elem = article.find('a', class_='article-item--url')
    if not link_elem:
        break
    link = link_elem['href']
    print(title) #change this to save info to json file
    print(link) #change this to save info to json file

    #to do:
    #save data to json folder
