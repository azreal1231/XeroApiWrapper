from xml.etree import ElementTree
import requests
import json


class XeroAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = 'https://identity.xero.com/connect/token'
        self.invoice_url = "https://api.xero.com/api.xro/2.0/Invoices"
        self.connection_url = "https://api.xero.com/connections"

    def get_tokens(self, authorization_code, redirect_uri='https://slatelight.co.za'):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',}
        data = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': redirect_uri,
        }
        response = requests.post(self.token_url, headers=headers, data=data, auth=(self.client_id, self.client_secret))
        if response.status_code == 200:
            tmp_tokens = json.loads(response.text)
            return {'access_token': tmp_tokens['access_token'], 'refresh_token': tmp_tokens['refresh_token']}
        else:
            print(f"Failed to get tokens, status code: {response.status_code}, message: {response.text}")
            return {}

    def refresh_tokens(self, _refresh_token):
        headers = {'Content-Type': 'application/x-www-form-urlencoded',}
        data = {'grant_type': 'refresh_token', 'refresh_token': _refresh_token,}
        response = requests.post(self.token_url, headers=headers, data=data, auth=(self.client_id, self.client_secret))
        if response.status_code == 200:
            tmp_tokens = json.loads(response.text)
            return {'access_token': tmp_tokens['access_token'], 'refresh_token': tmp_tokens['refresh_token']}
        else:
            print(f"Failed to refresh tokens, status code: {response.status_code}, message: {response.text}")
            return {}

    def get_tenant_id(self, _access_token):
        headers = {'Authorization': f'Bearer {_access_token}', 'Content-Type': 'application/json'}
        response = requests.get(self.connection_url, headers=headers)
        if response.status_code == 200:
            connections = json.loads(response.text)
            if connections:
                return connections[0]['tenantId']
            else:
                print("No connections found.")
                return None
        else:
            print(f"Failed to retrieve tenant ID, status code: {response.status_code}, message: {response.text}")
            return None

    def create_contact(self, _access_token, _tenant_id, contact_data):
        contacts_url = "https://api.xero.com/api.xro/2.0/Contacts"
        headers = {
            'Authorization': f'Bearer {_access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Xero-tenant-id': _tenant_id,
        }

        response = requests.post(contacts_url, headers=headers, json={'Contacts': [contact_data]})

        if response.status_code == 200:
            if response.headers.get('Content-Type') == 'application/json; charset=utf-8':
                resp = json.loads(response.text)
                return resp
            elif response.headers.get('Content-Type') == 'application/xml':
                tree = ElementTree.fromstring(response.content)
                # ... (parse XML to get the data you want)
                return tree
        else:
            print(f"Failed to create contact, status code: {response.status_code}, message: {response.text}")
            return None

    def get_contact_by_email(self, _access_token, _tenant_id, _email):
        contacts_url = "https://api.xero.com/api.xro/2.0/Contacts"
        headers = {
            'Authorization': f'Bearer {_access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Xero-tenant-id': _tenant_id,
        }

        # Fetch all contacts
        response = requests.get(contacts_url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve contacts, status code: {response.status_code}, message: {response.text}")
            return None

        contacts_data = json.loads(response.text)
        contacts = contacts_data.get('Contacts', [])

        # Find contact by email
        for contact in contacts:
            if 'EmailAddress' in contact and contact['EmailAddress'] == _email:
                return contact

        return None