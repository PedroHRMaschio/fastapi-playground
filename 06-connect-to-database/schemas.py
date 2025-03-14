from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: int

class DisplayProduct(BaseModel): # Use this class to return the product hidding the price
    name: str
    description: str
    class Config:
        orm_mode = True
