import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    # Send an HTTP request to the specified URL
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data from the HTML using Beautiful Soup
        data = soup.find_all('div', class_='example-class')  # Replace 'example-class' with your actual CSS selector
        
        return data
    
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

url = "https://www.example.com"
data = scrape_data(url)
print(data)

