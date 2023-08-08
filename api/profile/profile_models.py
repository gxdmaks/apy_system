from pydantic import BaseModel
from datetime import datetime


# Модель входных данных
class UserDent(BaseModel):
    profile_photo: str
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    reg_date: datetime
    password: str

# Модель для карты пользователя
class CardDent(BaseModel):
    card_number: int
    cardholder: str
    exp_date: int
    card_balanse: float
    card_name: str


