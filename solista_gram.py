import json
import requests
import webbrowser

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
## this opens browser successfully. Can't access URL so I can do an input command
