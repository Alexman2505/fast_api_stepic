import jwt  # тут используем библиотеку PyJWT


SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


USERS_DATA = [{"username": "admin", "password": "adminpass"}]


def create_jwt_token(data: dict):
    # кодируем токен, передавая в него наш словарь с тем, что мы хотим там разместить
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_user_from_token(token: str):
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )  # декодируем токен
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        pass
    except jwt.InvalidTokenError:
        pass


# Функция для получения пользовательских данных на основе имени пользователя
def get_user(username: str):
    for user in USERS_DATA:
        if user.get("username") == username:
            return user
    return None


# закодируем токен, внеся в него словарь с утверждением о пользователе
token = create_jwt_token({"sub": "admin"})

print(token)

# декодируем токен и излечем из него информацию о юзере, которую мы туда зашили
username = get_user_from_token(token)

print(username)  # посмотрим, что возвращается то, что ожидаем

# и теперь пойдем в нашу базу данных искать такого юзера по юзернейму
current_user = get_user(username)

print(current_user)  # удостоверимся, что нашелся тот, кто нужен
