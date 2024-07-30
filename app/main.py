import uvicorn
from fastapi import FastAPI
from models.models import User, User_date


app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}


@app.get('/custom')
def read_custom_message():
    return {'message': 'Custom message'}


@app.get('/users', response_model=User)
async def get_users():
    return User(**{"name": "Johnа Doss", "id": 1})


@app.post('/user')
async def user_post(user_data: User_date):
    return {
        'name': user_data.name,
        'age': user_data.age,
        'is_adult': user_data.age >= 18,
    }


# Пример пользовательских данных (для демонстрационных целей)
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}


# Конечная точка для получения информации о пользователе по ID
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}
