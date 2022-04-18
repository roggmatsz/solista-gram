"""Library containing methods used to access account media."""

import requests

_BASE_URL = 'https://graph.instagram.com'

def get_media_meta(access_token):
    """Gets user media metadata."""
    ENDPOINT = '/me/media?'
    media_meta_params = {
        'fields': 'id,caption',
        'access_token': access_token
    }

    response = requests.get(_BASE_URL + ENDPOINT, params=media_meta_params)
    if response.status_code != 200:
        print(response.text)
    else:
        return response.json()

def get_media_contents(media_id, access_token):
    """Gets pictures from user profile."""
    media_params = {
        'fields': 'id,media_type,media_url,username,timestamp',
        'access_token': access_token
    }

    media_response = requests.get(f'{_BASE_URL}/{media_id}', params=media_params)
    if media_response.status_code != 200:
        print(media_response.text)
    else:
        return media_response.json()
        