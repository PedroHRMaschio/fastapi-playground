from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello world!'

@app.get('/movies')
def movies():
    return { 'movie list': ['Movie A', 'Movie B', 'Movie C'] }
