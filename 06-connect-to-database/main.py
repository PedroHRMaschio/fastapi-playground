from fastapi import FastAPI
from .import schemas
from .import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.post('/product')
def create_product(request: schemas.Product):
    return request
