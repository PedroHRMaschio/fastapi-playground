from fastapi import FastAPI
from pydantic import BaseModel, Field

class User(BaseModel): # This is the request body for POST /users
    name: str
    email: str
    age: int

class Product(BaseModel):
    name: str
    price: int = Field(tittle='Price of the item', # This is an addition on docs
                       description='This would be the price',
                       gt=0) # This means that it must be greater than 0
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
