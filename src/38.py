import requests
from bs4 import BeautifulSoup
import re

url = "https://www.example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

header = soup.find('head').find_all('title')
print(header[0].text)

data = soup.find('body').find_all('div', class_='some-class')
for item in data:
    print(item.text)
