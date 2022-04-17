import json
import webbrowser
import requests

def get_long_token(short_token, client_secret):
    """Converts a short access token into a long access token."""

    LONG_TOKEN_URL = 'https://graph.instagram.com/access_token'
    long_token_params = {
        'grant_type': 'ig_exchange_token',
        'client_secret': client_secret,
        'access_token': short_token
    }
    print('Converting short to long access token')
    long_token_response = requests.get(LONG_TOKEN_URL, params=long_token_params)

    if long_token_response.status_code != 200:
        print(long_token_response.text)
        return
    
    return long_token_response.json()

def get_secrets():
    with open('secrets.json', 'r', encoding='utf-8') as secrets_file:
        parsed_secrets = json.load(secrets_file)
    return parsed_secrets

def update_secrets(key, value):
    with open('secrets.json', 'r+', encoding='utf-8') as secrets_file:
        parsed_json = json.load(secrets_file)
        parsed_json.update({ key: value })
        secrets_file.seek(0)
        json.dump(parsed_json, secrets_file, indent=4)

    return parsed_json

AUTH_URL = 'https://api.instagram.com/oauth/authorize'
TOKEN_URL = 'https://api.instagram.com/oauth/access_token'

secret = get_secrets()['secret']
client_id = get_secrets()['client_id']
redirect_uri = get_secrets()['redirect_uri']
account = get_secrets()['real_account']

if 'long_token' not in get_secrets():
    print(f'Requesting new access token for @{account}')
    auth_url = f'{AUTH_URL}?client_id={client_id}&redirect_uri={redirect_uri}&scope=user_profile,user_media&response_type=code'
    webbrowser.open(auth_url, new=1)
    authorization_code = input('Enter code in URL')

    params = {
        'client_id': '1024729738207116',
        'client_secret': secret,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'code': authorization_code
    }
    token_response = requests.post(TOKEN_URL, data=params)
    if token_response.status_code != 200:
        print(token_response.text)
    else:
        access_token = token_response.json()['access_token']
        user_id = token_response.json()['user_id']
        print(f'Access Token: {access_token}')
        print(f'User ID: {user_id}')
        update_secrets('access_token', access_token)
        update_secrets('user_id', user_id)
        print('Saved access token and user id.')
else:
    print(f'Access Token: {get_secrets()["access_token"]}')
    print(f'User ID: {get_secrets()["user_id"]}')
    response = get_long_token(get_secrets()['access_token'], secret)
    update_secrets('long_token', response)
    print(response['access_token'])
    print('Token Type:' + response['token_type'])
