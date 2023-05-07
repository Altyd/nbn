import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.news24.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='article-item--container')

data = []

for article in articles:
    title_elem = article.find('div', class_='article-item__title')
    if not title_elem:
        continue
    title = title_elem.text.strip()
    link_elem = article.find('a', class_='article-item--url')
    if not link_elem:
        break
    link = link_elem['href']
    article_data = {'title': title, 'link': "https://www.news24.com/" + link}
    data.append(article_data)

with open('articles.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
