from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel): # This is the request body for POST /users
    name: str
    email: str
    age: int

app = FastAPI()

@app.post('/users')
def create_user(user:User):
    return {'user data': user}
