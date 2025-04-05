import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve HTML from {url}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching the HTML: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Example: Extracting specific text based on attributes (id, class, etc.)
    title_text = soup.find('title').text
    author_name = soup.find('p', {'class': 'author'}).text
    
    return title_text, author_name

url = "https://example.com"
html_content = fetch_html(url)
if html_content:
    title, author = parse_html(html_content)
    print(f"Title: {title}")
    print(f"Author: {author}")
