import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return None

url = "https://www.example.com"
soup = get_html(url)
print(soup.prettify())
