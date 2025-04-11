import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}")

# Example usage
url = "https://api.github.com/search/repositories"
data = fetch_data(url)

if data:
    print("Repository found!")
    for repo in data["items"]:
        print(f"- {repo['name']}")
