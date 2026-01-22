from models.user import User
from models.currency import Currency


class UserCurrency:
    def __init__(self, user: User, currency: Currency):
        self.user = user
        self.currency = currency

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value: User):
        if isinstance(value, User):
            self.__user = value
        else:
            raise ValueError('Ошибка при задании пользователя')

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value: Currency):
        if isinstance(value, Currency):
            self.__currency = value
        else:
            raise ValueError('Ошибка при задании валюты')
