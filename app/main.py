from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from app.models.models import User
import uvicorn


app = FastAPI()
security = HTTPBasic()
USER_DATA = [
    User(**{"username": "JohnD", "password": "qwer1234"}),
    User(**{"username": "KateL", "password": "tyui5678"}),
]


def get_user_from_db(username: str) -> User | None:
    for user in USER_DATA:
        if user.username == username:
            return user
    return None


@app.post('/login')
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={'WWW-Authenticate': 'Basic'},
        )

    return {'message': 'You got my secret, welcome'}
