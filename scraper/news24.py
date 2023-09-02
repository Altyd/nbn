import requests
from bs4 import BeautifulSoup
import json

# scrape the article links and titles from the website
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

# save the article links and titles to a JSON file
with open('articles.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# load the article links and titles from the JSON file
with open('articles.json') as f:
    data = json.load(f)

# extract the article content for each article and save it to a new JSON file
articles_with_titles = []
for article in data:
    url = article['link']
    response = requests.get(url)
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', class_='article__title').text.strip()
        article_content = soup.find('div', class_='article__body NewsArticle').get_text().strip()
        articles_with_titles.append({
            'title': title,
            'content': article_content
        })
    except AttributeError:
        print(f"Could not extract title or content for article: {article['title']}")
with open('articles_with_titles.json', 'w') as f:
    json.dump(articles_with_titles, f, indent=4)
