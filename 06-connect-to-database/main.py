from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
import schemas
import models
from database import engine, SessionLocal
from database import get_db
from routers import product, seller

app = FastAPI(
    title='Product API',
    description='A simple product API',
    version='0.0.1',
    terms_of_service='http://example.com/terms/',
    contact={
        'name': 'Pedro Henrique Maschio',
        'url': 'https://github.com/PedroHRMaschio',
        'email': 'demo@gmail.com'
    },
    license_info={
        'name': 'XYZ',
        'url': 'https://example.com/license/'
    }
)
app.include_router(product.router)
app.include_router(seller.router)
models.Base.metadata.create_all(bind=engine)
