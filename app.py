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
# tokens = xero.get_tokens(AUTH_CODE)
# print(tokens)
#
# # Refreshing tokens
# refreshed_tokens = xero.refresh_tokens(tokens['refresh_token'])
# print(refreshed_tokens)
# update_tokens(refreshed_tokens['access_token'], refreshed_tokens['refresh_token'])

with open('token.json', 'r') as f:
    data = json.load(f)
    refresh_token = data['REFRESH_TOKEN']
    access_token = data['ACCESS_TOKEN']


# Getting tenant_id
tenant_id = xero.get_tenant_id(access_token)
print(f"tenant_id: {tenant_id}")

new_contact = {
    "Name": "",
    "EmailAddress": "",
    "FirstName": "",
    "LastName": "",
    "DefaultCurrency": "RSA"
}

# Create the contact
created_contact = xero.create_contact(access_token, tenant_id, new_contact)
# print(created_contact)

contact_details = xero.get_contact_by_email(access_token, tenant_id, 'edward@slatelight.co.za')
print(contact_details)
