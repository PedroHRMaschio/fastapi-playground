from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.params import Depends
import schemas
import models
from database import get_db

router = APIRouter()

@router.post('/product', status_code=status.HTTP_201_CREATED, tags=['product'])
def create_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price, seller_id=request.seller_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.put('/product/{id}', tags=['product'])
def update_product(id: int, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    product.update(request.model_dump())
    db.commit()
    return 'updated'

@router.get('/product', response_model=list[schemas.DisplayProduct], tags=['product'])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.get('/product/{id}', response_model=schemas.DisplayProduct, tags=['product'])
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    return product

@router.delete('/product/{id}', tags=['product'])
def delete_product(id: int, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'
