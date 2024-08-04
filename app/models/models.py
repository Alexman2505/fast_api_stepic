from pydantic import BaseModel, Field, EmailStr
from typing import Optional


# создаём модель данных, которая обычно расположена в файле models.py
class User(BaseModel):
    id: int
    name: str


class User_date(BaseModel):
    age: int
    name: str


class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr  # проверка формата почты
    age: Optional[int] = Field(None, gt=1)  # больше 1
    is_subscribed: bool = False
