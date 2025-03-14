from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Set


class User(BaseModel): # This is the request body for POST /users
    name: str
    email: str
    age: int

class Image(BaseModel):
    url: HttpUrl
    name: str

class Product(BaseModel):
    name: str
    price: int = Field(tittle='Price of the item', # This is an addition to the docs
                       description='This would be the price',
                       gt=0) # This means that it must be greater than 0
    discount: int
    discounted_price: float = 0
    image: Image
    tags: List[str] = [] # Here I have a list that only accepts strings.
    tags_unique: Set[str] = [] # Here I have a list that only accepts unique strings.

    class Config: # This is an addition to the docs
        schema_extra = {
            'example': {
                'name': 'Phone',
                'price': 200,
                'discount': 20,
                'discounted_price': 180,
                'image': {
                    'url': 'http://example.com/phone.jpg',
                    'name': 'phone'
                },
                'tags': ['smart', 'android'],
                'tags_unique': ['smart', 'android']
            }
        }

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
