from fastapi import APIRouter
import schemas

router = APIRouter(tags=['Login'])

@router.post('/auth')
def login(request: schemas.Login):
    return request


