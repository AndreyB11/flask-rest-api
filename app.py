from flask import Flask, request


app = Flask(__name__)


stores = [
    {
        "name": "Store 1",
        "items": [
            {
                "name": "Boots",
                "price": 15.5,
            }
        ]
    }
]


@app.get('/stores')
def get_stores():
    return {"stores": stores}


@app.get('/stores/<string:name>')
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 200

    return {"message": "Store not found"}, 404


@app.post('/stores')
def create_store():
    body = request.get_json()
    new_store = {"name": body["name"], "items": []}

    stores.append(new_store)
    return new_store, 201


@app.post('/stores/<string:name>/items')
def create_item(name):
    body = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": body["name"], "price": body["price"]}
            store["items"].append(new_item)
            return new_item, 201

    return {"message": "Store not found"}, 404
