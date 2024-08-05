from typing import Annotated
from pydantic import BaseModel, Field


class User(BaseModel):
    name: Annotated[str, Field(..., min_length=1)]
    age: Annotated[int, Field(..., ge=0)]


# Валидация данных
user = User(name="1", age=1)
print(user)
