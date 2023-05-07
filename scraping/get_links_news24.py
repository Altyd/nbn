from bs4 import BeautifulSoup
import requests
import json

# load JSON data from file
with open('articles.json') as f:
    data = json.load(f)

# create a list to store the articles with their titles
articles_with_titles = []

# loop through each article
for article in data:
    # extract the article title and content from the HTML code
    url = article['link']
    response = requests.get(url)
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', class_='article__title').text.strip()
        article_content = soup.find('div', class_='article__body NewsArticle').get_text().strip()

        # append the article with its title to the list
        articles_with_titles.append({
            'title': title,
            'content': article_content
        })
        
    except AttributeError:
        print(f"Could not extract title or content for article: {article['title']}")

# write the list of articles with their titles to a JSON file
with open('articles_with_titles.json', 'w') as f:
    json.dump(articles_with_titles, f, indent=4)
