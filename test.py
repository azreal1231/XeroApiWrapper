from order_example import ORDER_EXAMPLE

items = []
for item in ORDER_EXAMPLE['meta_data']['products']:
    tmp = {
        "Description": item['name'],
        "Quantity": item['quantity'],
        "UnitAmount": item['price'],
        "AccountCode": item['code'],
    }
    items.append(tmp)

for item in ORDER_EXAMPLE['meta_data']['refillProducts']:
    tmp = {
        "Description": item['name'],
        "Quantity": item['quantity'],
        "UnitAmount": item['price'],
        "AccountCode": item['code'],
    }
    items.append(tmp)

payment_date = ORDER_EXAMPLE['meta_data']['payfast_resp']['date'][0: 16]
