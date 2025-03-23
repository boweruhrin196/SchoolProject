import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Perform parsing and processing here

# Example usage
url = "https://www.example.com"
html_content = fetch_html(url)
parse_html(html_content)
