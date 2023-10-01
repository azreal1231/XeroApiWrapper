from settings import DEFAULT_SETTINGS
client_id = DEFAULT_SETTINGS['CLIENT_ID']
redirect_url = DEFAULT_SETTINGS['REDIRECT_URI']
base_url = 'https://login.xero.com/identity/connect/authorize'
url_params = f'?response_type=code&client_id={client_id}&redirect_uri={redirect_url}&scope=offline_access%20accounting.transactions%20accounting.contacts'
link = base_url+url_params
print(link)
