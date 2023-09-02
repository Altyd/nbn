# NBN | South Africa Non Biased News
**School Project**

Changing South Africa One Step At A Time

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Usage](#usage)
- [Project Plan](#project-plan)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)

## Introduction
Welcome to the NBN (Non Biased News) project repository! This is a school project aimed at creating a platform to scrape news articles from a popular news website, process them, and present unbiased news stories to users.

## Project Overview
The project consists of multiple components that work together to achieve the goal of providing unbiased news content. Here's an overview of the key components:

### news24.py
This Python script scrapes article links and titles from the News24 website. It uses the `requests` library to fetch the website content and `BeautifulSoup` for HTML parsing. The extracted data is saved to a JSON file.

### articles.json
This JSON file stores the scraped article links and titles in a structured format.

### Loading Article Data
The script loads the article links and titles from the JSON file and prepares to extract the article content.

### Extracting Article Content
The script visits each article link, extracts the article's title and content, and stores it in the `articles_with_titles.json` file. It handles cases where title or content extraction fails.

### plan.txt
This text file outlines the project plan in chronological order. It lists the steps involved, from scraping news sources to making news stories ready for upload.

## Usage
To run the `news24.py` script and scrape news articles from the News24 website, follow these steps:

1. Make sure you have Python installed on your system.
2. Install the required libraries by running: `pip install requests beautifulsoup4`.
3. Run the `news24.py` script using the command: `python news24.py`.

## Project Plan
The project plan outlined in `plan.txt` includes the following steps:

1. **Scrape News Sources:** Implement code to scrape news articles from the News24 website using web scraping techniques.

2. **Save News Stories To Database:** Save the scraped article links and titles to a JSON file (`articles.json`).

3. **Check if News Story Has Been Used Before:** Implement a mechanism to prevent duplicate news stories from being processed.

4. **Unbias News Story:** Develop strategies to present news content in an unbiased manner, ensuring objectivity and fairness.

5. **Ready for Upload:** Prepare the processed news stories for upload to the platform, making them accessible to users.

## Contributing
Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to submit pull requests or open issues.

## Disclaimer
This project is developed as a school project and may not accurately reflect real-world news standards. The goal is to provide a learning experience in web scraping, data processing, and unbiased content presentation.

## License
This project is licensed under the [MIT License](LICENSE).
