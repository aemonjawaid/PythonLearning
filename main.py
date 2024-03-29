from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.33
            }
        ]
    }
]


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.get("/store/<string:name>")
def get_store_by_name(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:store_name>/items")
def get_store_items(store_name):
    for store in stores:
        if store["name"] == store_name:
            return store["items"]
    return {"message": "Store not found"}, 404


@app.post("/store")
def create_new_store():
    request_data = request.get_json()
    for store in stores:
        if store["name"] == request_data["name"]:
            return {"message": "Store name already exists"}, 404
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:store_name>/item")
def create_new_store_item(store_name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == store_name:
            store["items"].append(request_data)
            return request_data, 201
    return {"message": "Store not found"}, 404


if __name__ == '__main__':
    app.run()
