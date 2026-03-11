from app import client

db = client["circuit_court_db"]

if "circuit_court_db" in client.list_database_names() :
    print("circuit_court_db database exist")

if "customers" in db.list_collection_names() :
    print("Collection 'customers' exists")

else :
     customers = db["customers"]
     customers.insert_one({"last_name": "Dupont", "first_name": "Jean",
                     "age": 37, "city": "Paris", "street": "Rue du rond",
                     "street_number": 56, "postal_code": "7520",
                     "email": "jean.dupont@hotmail.com",
                     "phone_number": "+65 584 24 56 87"})

     print("Collection 'customers' created")

if "products" in db.list_collection_names() :
    print("Collection 'products' exists")

else :
    products = db["products"]
    products.insert_one({"grower": "Shop_1", "product_brand": "MilkMilk", "product_name": "Lait entier",
                         "description": "97% milk, 2% sugar, 1% water", "price": 2.99, "quantity": 48, "promo": None,
                         "date_added": "09/03/2026", "expiration_date": "15/03/2026"})

    print("Collection 'products' created")

if "orders" in db.list_collection_names() :
    print("Collection 'orders' exists")
else :
    orders = db["orders"]
    orders.insert_one({"order_date": "09/03/2026", "delivery_date": "13/03/2026",
                       "customer_order": "Jean Dupont", "product_buy": "Milk"})

    print("Collection 'orders' created")

products = db["products"]
products.insert_one({"grower": "Shop_2", "product_brand": "COCO", "product_name": "Cacao",
                         "description": "97% cacao, 2% sugar, 1% water", "price": 4.98, "quantity": 72, "promo": None,
                         "date_added": "10/03/2026", "expiration_date": "16/03/2026"})