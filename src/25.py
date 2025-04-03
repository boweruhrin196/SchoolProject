import requests
from bs4 import BeautifulSoup
import os

url = "https://www.example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    href = link['href']
    if href.startswith("/"):
        href = href[1:]
    file_name = f"{href}.txt"
    with open(file_name, "w") as f:
        f.write(link.get_text())
