from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi.params import Depends
import schemas
import models
from database import get_db
from passlib.context import CryptContext

router = APIRouter(
    tags=['Seller'],
    prefix='/seller'
)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.post('/', response_model=schemas.DisplaySeller, status_code=status.HTTP_201_CREATED)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
