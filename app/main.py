from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI()
security = HTTPBasic()


class User(BaseModel):
    username: str
    password: str


USER_DATA = [
    User(**{"username": "user1", "password": "pass1"}),
    User(**{"username": "user2", "password": "pass2"}),
]


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    return user


# симуляционный пример
def get_user_from_db(username: str):
    for user in USER_DATA:
        if user.username == username:
            return user
    return None


@app.get("/protected_resource/")
def get_protected_resource(user: User = Depends(authenticate_user)):
    return {
        "message": "You have access to the protected resource!",
        "user_info": user,
    }
