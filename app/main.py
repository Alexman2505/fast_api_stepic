import uvicorn
from typing import Dict, List
from fastapi import FastAPI
from models.models import User, User_date, Feedback, UserCreate


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
async def read_user(user_id: int):
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}


feedback_db: List[Dict[str, str]] = []


# Конечная точка для получения фидбека
@app.post("/feedback")
async def read_feedback(user_feedback: Feedback):
    # тут добавили юзера в фейковую БД
    feedback_db.append(
        {"name": user_feedback.name, "message": user_feedback.message}
    )
    print(feedback_db)
    return {"message": f"Feedback received. Thank you {user_feedback.name}!"}


@app.post('/create_user', response_model=UserCreate)
async def create_user(user: UserCreate):
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
