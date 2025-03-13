from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel): # This is the request body for POST /users
    name: str
    email: str
    age: int

class Product(BaseModel):
    name: str
    price: int
    discount: int
    discounted_price: float = 0

app = FastAPI()

@app.post('/users')
def create_user(user:User):
    return {'user data': user}

@app.post('/products')
def create_product(product: Product):
    product.discounted_price = product.price - \
        (product.price * product.discount)/100
    return product

@app.post('/purchase')
def purchase(user: User, product: Product):
    return {'user': user, 'product': product}
