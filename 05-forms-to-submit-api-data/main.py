from fastapi import FastAPI, Form

app = FastAPI()

@app.post('/login')
def login(username: str = Form(...), password: str = Form(...)):
    return {'username': username}
# This way you can enter da data in the form and submit it to the API
# The data will be sent as a form data and not as a JSON
# This is useful when you are working with HTML forms
# You can check this on the docs by accessing the route /docs
