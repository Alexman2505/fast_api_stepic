from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt
import time

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Секретный ключ для подписи и верификации токенов JWT
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

# Пример информации из БД
USERS_DATA = [{"username": "admin", "password": "adminpass"}]


class User(BaseModel):
    username: str
    password: str


# Функция для создания JWT токена
def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)  # кодируем токен


# Функция получения User'а по токену
def check_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )  # декодируем токен
        if time.time() < payload.get("exp"):
            return payload
    except:
        return {"error": "the token is not valid"}


# Функция для получения пользовательских данных на основе имени пользователя
def get_user(username: str):
    for user in USERS_DATA:
        if user.get("username") == username:
            return user
    return None


@app.post("/login")
async def login(user_in: User):
    for user in USERS_DATA:
        if (
            user.get("username") == user_in.username
            and user.get("password") == user_in.password
        ):
            expiration_time = (
                time.time() + 30
            )  # время действия токкена 30 секунд с момента его создания
            return {
                "access_token": create_jwt_token(
                    {"sub": user_in.username, "exp": expiration_time}
                ),
                "token_type": "bearer",
            }
    return {"error": "Invalid credentials"}


@app.get("/protected_resource")
async def about_me(current_user: str = Depends(check_token)):
    user = get_user(current_user.get("sub"))
    if user:
        return {"message": "access is allowed"}
    return {"error": "access denied"}
