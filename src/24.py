import requests
import json

# Replace with your own credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Example API call: GET user details
response = requests.get(f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}")

# Parse the response JSON
user_details = json.loads(response.text)

# Extract and print user name and username
user_name = user_details['access_token']
username = user_details['oauth_token']

print(f"User Name: {username}")
print(f"Username: {user_name}")
