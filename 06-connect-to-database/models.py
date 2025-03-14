from sqlalchemy import Column, Integer, String
from database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)

class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
