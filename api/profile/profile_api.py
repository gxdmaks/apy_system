from fastapi import Body
from main import app
from .profile_models import UserDent

# Регистрация пользователя
@app.post('/api/register-user')
async def user_registration(user_data: UserDent):
    print(user_data)
    # После регистрации выдать айди пользователя
    return {'status': 1, 'message': 'Registration complete'}


# Вход в аккаунт
@app.post('/api/login-user')
async def user_login(phone_number: int = Body(), password: str = Body()):
    print(phone_number, password)
    checker = None
    # если данные верны отпровляем user_id и данные пользователя
    return {'status': 1, 'message': 'Logged in'}