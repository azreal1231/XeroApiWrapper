ORDER_EXAMPLE = {
  "_id": "041af69ff5084aa5a77cb34db276bc42",
  "_rev": "5-57d344150bfbb586436fa053d59c560f",
  "collection": "orders",
  "status": "processing",
  "createdOn": "2023-07-31 19:21:11.569267+02:00",
  "createdBy": "self_order",
  "items": [
    {
      "name": "14kg Gas Refill",
      "price": 435.54,
      "vat": 0,
      "quantity": 2,
      "size": "",
      "meta_data": {
        "product_type": "refill"
      }
    }
  ],
  "addresses": [
    {
      "type": "shipping",
      "apartmentNumber": "",
      "buildingName": "",
      "address": "14 Armada road Rustivia Germiston",
      "postalCode": "1401",
      "country": "RSA",
      "city": "Rustivia",
      "province": "GP"
    },
    {
      "type": "billing",
      "apartmentNumber": "",
      "buildingName": "",
      "address": "14 Armada road Rustivia Germiston",
      "postalCode": "1401",
      "country": "RSA",
      "city": "Rustivia",
      "province": "GP"
    }
  ],
  "paymentMethod": {
    "type": "payfast",
    "ref_id": "596144"
  },
  "orderNumber": "596144",
  "customer": "19035efb-19d0-4a35-aa92-9a75248604dc",
  "cart_total": 871.08,
  "total": 871.08,
  "subTotal": 871.08,
  "vat": 130.662,
  "walletdoc_ref_id": "E7328CCF-1C2B-42DB-87FE-219B93293F85",
  "deliveryNotes": "",
  "meta_data": {
    "products": [],
    "tradeInProducts": [],
    "refillProducts": [
      {
        "_id": "66af5654c3de37fca90d8f290b0ea06e",
        "_rev": "26-ac4a4ba4252072948345b597b446a5b5",
        "collection": "products",
        "status": "draft",
        "createdOn": "2023-04-11T10:40:31.949Z",
        "createdBy": "Unknown",
        "name": "14kg Gas Refill",
        "code": "14KG-REF",
        "price": 435.54,
        "stock": 100,
        "description": "14kg gas refill",
        "cylinderType": "composite",
        "tags": [
          "gas refill"
        ],
        "category": [
          "refills"
        ],
        "img_name": "https://tcp-assets.ams3.cdn.digitaloceanspaces.com/products/56BEA779D277432D84A11A4F5C8C6484.png",
        "refill": 435.54,
        "deposit": 0,
        "size": "",
        "coming_soon": "false",
        "text": "",
        "unavailable": {
          "status": False,
          "reason": ""
        },
        "selected": False,
        "quantity": 2
      }
    ],
    "coupon": "",
    "subTotal": 871.08,
    "depositTotal": 0,
    "totalPrice": 871.08,
    "totalDiscount": 0,
    "cartItemsTotal": 2,
    "connectAppliance": False,
    "connectApplianceCost": 50,
    "customer_details": {
      "doc_id": "19035efb-19d0-4a35-aa92-9a75248604dc",
      "fullname": "Kenleigh Forbes",
      "contact_number": "0829051702",
      "contact_email": "kenleigh.forbes@absa.co.za"
    },
    "payfast_resp": {
      "payment_status": "COMPLETE",
      "signature": "9136014aa2834ba6a469007826aa9d96",
      "amount_gross": "871.08",
      "date": "2023-07-31 17:25:49.872865"
    },
    "create_order_drip_resp": True,
    "create_order_ship_day_resp": "{\n  \"success\": true,\n  \"response\": \"Order inserted with id 13619579\",\n  \"orderId\": 13619579\n}",
    "create_order_email_resp": {
      "request_id": "4fc8c072-2fc7-11ee-89ef-f23c9216bf70",
      "data": {
        "succeeded": 1,
        "failed": 0,
        "failures": [],
        "email_id": "1qQWec-9EVfkg-1q"
      }
    }
  },
  "client": {
    "fullname": "Kenleigh Forbes",
    "doc_id": "19035efb-19d0-4a35-aa92-9a75248604dc"
  },
  "credit": {
    "used": True,
    "total": 0,
    "records": []
  },
  "coupon": {
    "used": False,
    "total": 0,
    "code": "",
    "couponType": "",
    "doc_id": ""
  },
  "promo_code": {
    "used": False,
    "total": 0,
    "code": "",
    "doc_id": "",
    "associated_user": {
      "email": "",
      "doc_id": ""
    }
  },
  "affiliate": {
    "used": False,
    "code": "",
    "doc_id": "",
    "total": 0,
    "commission": 0
  },
  "business_details": {
    "used": False,
    "name": "",
    "vat_number": ""
  },
  "ENV": "PROD",
  "platform": "desktop"
}
