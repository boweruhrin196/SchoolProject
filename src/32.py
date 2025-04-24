import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve data from {url}, status code: {response.status_code}")

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/'):
            print(href)
            # You can implement further logic here based on the data you retrieve

url = "https://example.com"
html_content = fetch_html(url)

parse_data(html_content)
