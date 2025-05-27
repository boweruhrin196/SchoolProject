import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Get some data from a specific HTML element
data = soup.find('div', {'class': 'example-class'}).text.strip()
print(data)
