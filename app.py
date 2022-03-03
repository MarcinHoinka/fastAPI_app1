from typing import Optional
import logging

from fastapi import FastAPI, Path, Response, status
from pydantic import BaseModel

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO, datefmt='%m/%d/%Y %H:%M:%S')


class User(BaseModel):
    firstname: str
    lastname: Optional[str] = None
    id: int


testapp = FastAPI()


@testapp.get("/")
def root():
    return {"message": "Hell no World!"}


# if you need returned JSONResponse - FastAPI uses it by default, set: return user
@testapp.post("/users/", status_code=201)
def create_user(user: User, response: Response):
    logging.info(f'Created user: {user}')
    response.status_code = status.HTTP_201_CREATED
    return response


# hardcoded user for API test purposes
@testapp.get("/users/{user_id}")
def read_user(user_id):
    user = User(firstname="John", lastname="Dope", id=user_id)
    logging.info(f'Read user: {user}')
    return user

# update body https://fastapi.tiangolo.com/tutorial/body-updates/#partial-updates-with-patch
