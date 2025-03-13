from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'Hello world!'


# id here is an id parameter
@app.get('/users/{id}')
def users(id: int):
    return f'This is a user page for user {id}'


@app.get('/profiles/{username}')
def profile(username: str):
    return {f'This is a profile page for user : {username}'}


@app.get('/movies')
def movies():
    return { 'movie list': ['Movie A', 'Movie B', 'Movie C'] }
