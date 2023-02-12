# DONE Создать класс User (в котором хранится информация о пользователе)
"""
+ в классе должны быть атрибуты (id, username, password)
+ id не должен передаваться как входной аргумент. При инициализации он должен сам определяться.
+ при инициализации пользователя должна создаваться корзина для этого пользователя,
    но изменить её извне не должно получаться, она доступна только для чтения (возвращения объекта корзины)
+ атрибут username можно задать при инициализации, но возможность его изменить должна отсутствовать
+ атрибут password должен храниться в хэш-значение пароля и должен быть закрытым. Хранение пароля в открытом виде
    запрещено
+ должны быть реализованы проверки при инициализации для атрибута username
+ реализуйте __str__ и __repr__ методы. Однако теперь реальный password не должен выводится на экран,
    вместо него поставим заглушку 'password1'.
"""
from id_counter import IdCounter
from passwd import Password
from cart import Cart
import re


class User(IdCounter):
    """
    Класс служит для создания пользователей.
    """
    def __init__(self, username: str, passwd: str, cart: Cart = Cart(None)):
        """
        Инициализация пользователя.
        :param username: Имя пользователя.
        :param passwd: Открытый пароль.
        """
        self.check_username(username)
        self.check_cart(cart)
        self.__passwd = Password(passwd)
        self._username = username
        self._user_id = self.__class__.increment_id_count()
        self._cart = cart

    def __repr__(self):
        return f"{self.__class__.__name__}({self._username}, password1)"

    def __str__(self):
        return f"Пользователь {self._username}"

    @property
    def user_id(self):
        return self._user_id

    @property
    def username(self):
        return self._username

    @property
    def passwd(self):
        return self.__passwd

    @property
    def cart(self):
        return self._cart

    @staticmethod
    def check_username(username: str) -> bool:
        """
        Проверка имени пользователя. Оно может содержать только буквы, цифры, пробелы, подчёркивания '_' и дефисы '-'.
        :param username: Имя пользователя.
        :return: bool
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if re.search(re.compile(r'[^\w\- ]'), username) is not None:
            raise ValueError("Имя пользователя может содержать только буквы, цифры, пробелы, "
                             "подчёркивания '_' и дефисы '-'")
        return True

    @staticmethod
    def check_cart(cart: Cart) -> bool:
        """
        Проверка корзины для пользователя.
        :param cart: Корзина.
        :return: bool
        """
        if not isinstance(cart, Cart):
            raise TypeError("Корзина должна принадлежать классу Cart")
        return True
