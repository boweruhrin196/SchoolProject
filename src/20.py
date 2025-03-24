import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('h1').text
print(title)

links = soup.find_all('a')
for link in links:
    print(link['href'])
