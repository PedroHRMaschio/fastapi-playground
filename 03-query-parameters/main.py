from fastapi import FastAPI

app = FastAPI()

@app.get('/products')
def products(id, price):
    return {'product': id, 'price': price}
