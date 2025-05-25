import os
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data from {url}")

# Example usage: Fetch some sample data
data = fetch_data("https://api.example.com/data")
print(data)
