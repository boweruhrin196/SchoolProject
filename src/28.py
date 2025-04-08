import requests

def main():
    url = "https://api.github.com/search/repositories"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()['items']
        for repo in repositories:
            print(repo['name'])
    else:
        print(f"Failed to get data. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
