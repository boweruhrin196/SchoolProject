import requests
from bs4 import BeautifulSoup

def fetch_html_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching the page: {e}")
        return None

def parse_html(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    
    # Example for a simple search query
    input_text = "Python programming"
    results = soup.find_all(text=input_text)
    
    if results:
        print(f"Found {len(results)} matches for '{input_text}':")
        for result in results:
            print(result.text)

url = "https://www.example.com/search?q=python+programming"
html_data = fetch_html_data(url)
parse_html(html_data)
