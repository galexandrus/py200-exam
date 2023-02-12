# DONE Создайте класс Store
"""
+ Реализуйте в нём аутентификацию (упростим задачу, чтобы не хранить список пользователей, под аутентификацией будем
    понимать создание пользователя) пользователя через консоль (логин и пароль будут вводиться через консоль)
+ Реализуйте метод, позволяющий пользователю добавить случайный продукт в корзину
+ Реализуйте метод, позволяющий пользователю просмотреть свою корзину
"""
from user import User
from product import Product


class Store:

    def __init__(self, store_name: str = "tea store", user: User = None):
        self.check_store_name(store_name)
        self._store_name = store_name
        user = self.user_auth(user)
        self._user = user

    @property
    def user(self):
        return self._user

    @property
    def store_name(self):
        return self._store_name

    def add_random_product(self):
        self.user.cart.add_product(next(Product.product_gen()))

    def cart_view(self):
        print("id   product_name    price   rating")
        for product in self.user.cart.product_list:
            id_ = product.product_id
            name = product.product_name
            price = product.price
            rating = product.rating
            print(id_, name, price, rating)

    def del_product(self, product: Product):
        self.user.cart.del_product(product)

    @staticmethod
    def user_auth(user: User):
        if user is None:
            while True:
                try:
                    username = str(input("Введите имя пользователя: "))
                    passwd = str(input("Введите пароль: "))
                    user = User(username, passwd)
                except TypeError:
                    print("Имя пользователя и пароль должны быть типа str")
                    continue
                except ValueError:
                    print("Имя пользователя и пароль могут содержать только буквы, цифры, пробелы, "
                          "подчёркивания '_' и дефисы '-', пароль не менее 8 символов")
                    continue
                break
        else:
            if not isinstance(user, User):
                raise TypeError("Пользователь должен принадлежать классу User")
        return user

    @staticmethod
    def check_store_name(store_name) -> bool:
        if not isinstance(store_name, str):
            raise TypeError("Наименование магазина должно быть типа str")
        return True
