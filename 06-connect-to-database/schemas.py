from pydantic import BaseModel
from typing import Optional

class Seller(BaseModel):
    username: str
    email: str
    password: str

class DisplaySeller(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        orm_mode = True

class Product(BaseModel):
    name: str
    description: str
    price: int
    seller_id: int

class DisplayProduct(BaseModel): # Use this class to return the product hidding the price
    name: str
    description: str
    seller: DisplaySeller
    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
