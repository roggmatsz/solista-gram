import json
import webbrowser
import requests

def get_secrets():
    with open('secrets.json', 'r', encoding='utf-8') as secrets_file:
        parsed_secrets = json.load(secrets_file)
    return parsed_secrets

AUTH_URL = 'https://api.instagram.com/oauth/authorize'
TOKEN_URL = 'https://api.instagram.com/oauth/access_token'

secret = get_secrets()['secret']
client_id = get_secrets()['client_id']
redirect_uri = get_secrets()['redirect_uri']
account = get_secrets()['real_account']
auth_url = f'{AUTH_URL}?client_id={client_id}&redirect_uri={redirect_uri}&scope=user_profile,user_media&response_type=code'


# Stuck at the part where user needs to interact with browser to get token
# auth_response = requests.get(auth_url)
webbrowser.open(auth_url, new=1)
authorization_code = input('Enter code in URL')

# with open('secrets.json', 'r+', encoding='utf-8') as secrets_file:
#     parsed_json = json.load(secrets_file)
#     parsed_json.update({'auth_code': authorization_code})
#     secrets_file.seek(0)
#     json.dump(parsed_json, secrets_file, indent=4)

params = {
    'client_id': '1024729738207116',
    'client_secret': secret,
    'grant_type': 'authorization_code',
    'redirect_uri': redirect_uri,
    'code': authorization_code
}
token_response = requests.post(TOKEN_URL, data=params)
#token_response = requests.post(url)
if token_response.status_code != 200:
    print(token_response.text)
else:
    access_token = token_response.json()['access_token']
    user_id = token_response.json()['user_id']
    print(f'Access Token: {access_token}')
    print(f'User ID: {user_id}')

## this opens browser successfully. Can't access URL so I can do an input command
