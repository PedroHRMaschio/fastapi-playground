from fastapi import FastAPI

app = FastAPI()

@app.get('/products')
def products(id, price): # This way the query parameters are mandatory
    return {'product': id, 'price': price}

@app.get('/products/v2')
def products(id: int = 1, price: int = 0): # This way the query parameters are not mandatory and have a default value
    return {'product': id, 'price': price}
