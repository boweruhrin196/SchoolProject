import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to load the webpage. Status code: {response.status_code}")
    except Exception as e:
        print(e)

url = "https://www.example.com"
html_content = fetch_html(url)
soup = BeautifulSoup(html_content, 'html.parser')
