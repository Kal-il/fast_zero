from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UsserPublic, UsserSchema, UserList

database = []

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/ola', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_page():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
"""


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UsserPublic)
def create_user(user: UsserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id

@app.get('/users', response_model=UserList)
def read_users():
    return{'users': database}