from xero_wrapper import XeroAPI
import json
from settings import AUTH_CODE, DEFAULT_SETTINGS
from order_example import ORDER_EXAMPLE


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
    token_data['access_token'] = _access_token
    token_data['refresh_token'] = _refresh_token

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


with open('token.json', 'r') as f:
    data = json.load(f)
    refresh_token = data['refresh_token']
    access_token = data['access_token']
#
refreshed_tokens = xero.refresh_tokens(refresh_token)
print(refreshed_tokens)
update_tokens(refreshed_tokens['access_token'], refreshed_tokens['refresh_token'])
access_token = refreshed_tokens['access_token']
# Getting tenant_id
tenant_id = xero.get_tenant_id(access_token)
print(f"tenant_id: {tenant_id}")

# results = xero.get_invoices_by_email(access_token, tenant_id, 'edward@slatelight.co.za')
# print(results)
new_contact = {
    "Name": "edward",
    "EmailAddress": "jack4@slatelight.co.za",
    "FirstName": "jack",
    "LastName": "nicholls",
    "DefaultCurrency": "RSA"
}

# Create the contact
created_contact = xero.create_contact(access_token, tenant_id, new_contact)
new_contact = created_contact['Contacts'][0]

# accounts = xero.get_all_accounts(access_token, tenant_id)
# print(accounts)

contact_details = xero.get_contact_by_email(access_token, tenant_id, 'jack4@slatelight.co.za')
if contact_details is None:
    '''Create Contact'''
else:
    print(contact_details)

#
invoice_data = {
    "Type": "ACCREC",
    "Contact": {"ContactID": contact_details['ContactID']},
    "Date": "2023-09-29",
    "DueDate": "2023-10-29",
    'LineAmountType': 'Exclusive',
    "LineItems": [],
    "Status": "AUTHORISED"

}

items = []
# for item in ORDER_EXAMPLE['meta_data']['products']:
#     tmp = {
#         "Description": item['name'],
#         "Quantity": item['quantity'],
#         "UnitAmount": item['price'],
#         "TaxType": "OUTPUT",
#         "AccountCode": "200"
#     }
#     items.append(tmp)

for item in ORDER_EXAMPLE['meta_data']['refillProducts']:
    tmp = {
        "Description": item['name'],
        "Quantity": item['quantity'],
        "UnitAmount": item['price'],
        "TaxType": "OUTPUT",
        "AccountCode": "201"
    }
    items.append(tmp)

payment_date = ORDER_EXAMPLE['meta_data']['payfast_resp']['date'][0: 16]
invoice_data['LineItems'] = items
invoice_data['Date'] = payment_date
invoice_data['DueDate'] = payment_date

result = xero.create_invoice(access_token, tenant_id, invoice_data)
print(result)
credit_note_data = {
    'Type': 'ACCPAYCREDIT',  # Accounts payable credit note
    'Contact': {
        'Name': contact_details['Name'],
        "ContactID": contact_details['ContactID']
    },
    'LineItems': [
        {
            'Description': 'Credit for returned item',
            'Quantity': 1,
            'UnitAmount': 50.00,
            'AccountCode': '400'  # Appropriate account code
        }
    ],
    'Date': '2023-01-01',  # Date of the credit note
    'Status': 'AUTHORISED',  # Status of the credit note
    'LineAmountTypes': 'Exclusive',  # How line amounts are treated
    # Additional fields as needed
}

# resp = xero.create_credit_note(access_token, tenant_id, credit_note_data)
# print(resp)
# invoice = result['Invoices'][0]
# invoice_no = invoice['InvoiceNumber']
# print(f'invoice no: {invoice_no}')
