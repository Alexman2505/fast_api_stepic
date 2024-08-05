from app.models.models import (
    User,
    User_date,
    Feedback,
    UserCreate,
    Product,
    User_cookie,
)
from datetime import datetime
from fastapi import FastAPI, HTTPException, Cookie, Response, Form, Response
from typing import Dict, List, Annotated
from uuid import uuid4


app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"message": "Hello, World!"}


@app.get("/custom")
async def read_custom_message():
    return {"message": "Custom message2"}


@app.get("/users", response_model=User)
async def get_users():
    return User(**{"name": "Johnа Doss", "id": 1})


@app.post("/user")
async def user_post(user_data: User_date):
    return {
        "name": user_data.name,
        "age": user_data.age,
        "is_adult": user_data.age >= 18,
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


@app.post("/create_user", response_model=UserCreate)
async def create_user(user: UserCreate):
    return user


sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99,
}
sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99,
}
sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99,
}
sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99,
}
sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99,
}
sample_products = [
    sample_product_1,
    sample_product_2,
    sample_product_3,
    sample_product_4,
    sample_product_5,
]


# урок 3.1. обработка параметров пути в http запросах
@app.get('/products/search')
async def search(keyword: str, category: str = None, limit: int = 10):
    '''принимает различные параметры запроса и
    возвращает список, в который добавлены результаты поиска
    '''
    result = list(
        filter(
            lambda item: keyword.lower() in item['name'].lower(),
            sample_products,
        )
    )
    if category:
        result = list(
            filter(lambda item: item["category"] == category, result)
        )
    return result[:limit]


# урок 3.1. обработка параметров пути в http запросах
@app.get("/product/{product_id}", response_model=Product)
async def get_product_info_by_id(product_id: int):
    '''принимает только параметр пути и возвращает элемент списка,
    в котором опредленному ключу соответствует значение из поиска
    '''
    for prod in sample_products:
        if product_id == prod["product_id"]:
            return prod
    raise HTTPException(status_code=404, detail="Product not found")


# урок 3.2 куки
@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}


@app.get("/")
async def root(response: Response):
    now = datetime.now().strftime(
        "%d/%m/%Y, %H:%M:%S"
    )  # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    return {"message": f"куки установлены {now}"}


# урок 3.2 куки
user_db_cookie = [
    {'username': 'JohnD', 'password': 'qwer1234', 'session_token': ''}
]


@app.post('/login')
async def login_user(
    response: Response, username: str = Form(), password: str = Form()
):
    for user in user_db_cookie:
        if user['username'] == username and user['password'] == password:
            user['session_token'] = str(uuid4())
            response.set_cookie(
                key='session_token', value=user['session_token'], httponly=True
            )
            return {'message': 'Cookie was set.'}
    return {'message': 'Wrong username or password.'}


@app.get('/user')
async def user_login_via_cookie(
    session_token: Annotated[str | None, Cookie()] = None
):
    for user in user_db_cookie:
        if session_token and session_token == user['session_token']:
            return {'username': user['username'], 'password': user['password']}
    return {'message': 'Unauthorized'}
