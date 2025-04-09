import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve {url}")

url = "https://example.com"
html_content = fetch_webpage(url)
soup = BeautifulSoup(html_content, 'html.parser')
