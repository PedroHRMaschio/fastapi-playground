from fastapi import FastAPI

app = FastAPI()


@app.get('/users/{username}')
def profile(username):
    return {f'This is a profile page for {username}'}


@app.get('/users/admin')
def admin():
    return {'This is admin page'}

# When you get the route admin you will receive the response:
# {"This is a profile page for admin"}
# And this is not what we want, we want to receive the message:
# {"This is admin page"}
# This happens because /users/admin is under /users/{username}
# You can fix this just changing the order of the requests
