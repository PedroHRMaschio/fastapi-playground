from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
import schemas
import models
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/product', status_code=status.HTTP_201_CREATED)
def create_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put('/product/{id}')
def update_product(id: int, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    product.update(request.model_dump())
    db.commit()
    return 'updated'

@app.get('/product')
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/product/{id}', response_model=schemas.DisplayProduct)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    return product

@app.delete('/product/{id}')
def delete_product(id: int, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.post('/seller')
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    new_seller = models.Seller(username=request.username, email=request.email, password=request.password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
