from fastapi import FastAPI, status, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
import schemas
import models
from database import engine, SessionLocal
from passlib.context import CryptContext

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

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/product', status_code=status.HTTP_201_CREATED, tags=['product'])
def create_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price, seller_id=request.seller_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.put('/product/{id}', tags=['product'])
def update_product(id: int, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    product.update(request.model_dump())
    db.commit()
    return 'updated'

@app.get('/product', response_model=list[schemas.DisplayProduct], tags=['product'])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/product/{id}', response_model=schemas.DisplayProduct, tags=['product'])
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    return product

@app.delete('/product/{id}', tags=['product'])
def delete_product(id: int, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.post('/seller', response_model=schemas.DisplaySeller, status_code=status.HTTP_201_CREATED, tags=['seller'])
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
