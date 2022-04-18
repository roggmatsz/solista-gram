"""Main or entry point for solista-gram."""

import json
import authentication as auth
import media_access as media

def get_secrets():
    """Gets contents of secrets.json file."""
    with open('secrets.json', 'r', encoding='utf-8') as secrets_file:
        parsed_secrets = json.load(secrets_file)
    return parsed_secrets

def update_secrets(key, value):
    """Updates values or creates new values in secrets.json file."""
    with open('secrets.json', 'r+', encoding='utf-8') as secrets_file:
        parsed_json = json.load(secrets_file)
        parsed_json.update({ key: value })
        secrets_file.seek(0)
        json.dump(parsed_json, secrets_file, indent=4)

    return parsed_json

secret = get_secrets()['secret']
client_id = get_secrets()['client_id']
redirect_uri = get_secrets()['redirect_uri']
account = get_secrets()['real_account']

if 'long_token' not in get_secrets():
    print('Requesting new access token.')
    auth_code = auth.get_browser_auth(client_id, redirect_uri)
    (user_id, access_token) = auth.get_access_token(client_id, secret, redirect_uri, auth_code)

    update_secrets('access_token', access_token)
    update_secrets('user_id', user_id)
    print('Saved access token and user id.')

    print('Converting to long access token')
    long_token = auth.get_long_token(access_token, secret)
    update_secrets('long_token', long_token)
else:
    print(f'Access Token: {get_secrets()["access_token"]}')
    print(f'User ID: {get_secrets()["user_id"]}')
    print(media.get_media_meta(get_secrets()['long_token']['access_token']))
    print(media.get_media_contents('18019372519365816', get_secrets()['long_token']['access_token']))

if __name__ == '__main__':
    # unit testing suite goes here
    print('This runs when file is executed as python file.py')
    