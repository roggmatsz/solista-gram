"""Collection of functions used to get access to IG's API."""

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

def get_browser_auth(client_id, redirect_uri, scope=None):
    """Temporary method used to get auth code from user."""

    AUTH_URL = 'https://api.instagram.com/oauth/authorize'
    scope_param = 'user_profile,user_media' if scope == None else scope

    browser_url = f'{AUTH_URL}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope_param}'
    webbrowser.open(browser_url, new=1)

    authorization_code = input('Enter authorization code:\n')
    if len(authorization_code) == 0:
        print('Error: No authorization code received.')
        return authorization_code

    return str.strip(authorization_code)

def get_access_token(client_id, client_secret, redirect_uri, auth_code):
    """Returns a short-lived access token given an auth code."""

    TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'code': auth_code
    }

    response = requests.post(TOKEN_URL, params=params)
    if response.status_code != 200:
        print(response.text)
        return ''

    return response.json()
