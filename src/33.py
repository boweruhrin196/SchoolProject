import requests

url = "https://api.github.com/search/repositories"
params = {
    'q': 'Python',
    'sort': 'stars'
}

response = requests.get(url, params=params)
data = response.json()
repositories = data['items']

for repository in repositories:
    print(repository['full_name'])
