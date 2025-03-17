from fastapi import APIRouter, Depends, status, HTTPException
import database, models, schemas
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "81d259e9e4368a05d048aeae4766929319b55245375109e0b91720df1cbd2270"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(tags=['Login'])

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post('/auth')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    seller = db.query(models.Seller).filter(models.Seller.email == request.email).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials")
    if not pwd_context.verify(request.password, seller.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials")
    access_token = generate_token(
        data={'sub': seller.username}
    )
    return {"access_token":access_token, "token_type":"bearer"}
