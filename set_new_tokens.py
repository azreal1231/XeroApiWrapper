from xero_wrapper import XeroAPI
import json
from settings import AUTH_CODE, DEFAULT_SETTINGS


def update_tokens(_access_token, _refresh_token):
    # Define the path to the token.json file
    token_file_path = 'token.json'

    # Read the existing tokens from token.json
    try:
        with open(token_file_path, 'r') as f:
            token_data = json.load(f)
    except FileNotFoundError:
        token_data = {}  # Initialize as an empty dictionary if the file is not found

    # Update the tokens
    token_data['ACCESS_TOKEN'] = _access_token
    token_data['REFRESH_TOKEN'] = _refresh_token

    # Write the updated tokens back to token.json
    with open(token_file_path, 'w') as f:
        json.dump(token_data, f, indent=4)


# Example usage
xero = XeroAPI(DEFAULT_SETTINGS['CLIENT_ID'], DEFAULT_SETTINGS['CLIENT_SECRET'])

# # Getting tokens
tokens = xero.get_tokens(AUTH_CODE)
print(tokens)

update_tokens(tokens['access_token'], tokens['refresh_token'])
