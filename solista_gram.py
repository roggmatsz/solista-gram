import json
import requests

def get_secrets():
    with open('secrets.json', 'r') as secrets_file:
        parsed_secrets = json.load(secrets_file)
        
    return (parsed_secrets['secret'], parsed_secrets['client_id'])

print(get_secrets())
