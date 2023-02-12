# DONE Создать класс Cart (корзина в котором хранится информация о списке товаров)
"""
+ должны быть методы добавления и удаления товара из корзины
"""
# from user import User
from product import Product


class Cart:
    """
    Корзина. Здесь хранится информация о списке товаров.
    """
    def __init__(self, product_list: list = None):
        # self.check_user(user)
        # self._user = user
        self.product_list = product_list

    def __repr__(self):
        return f"{self.__class__.__name__}({self.product_list})"

    def __str__(self):
        return f'Корзина содержит: ' \
               f'{", ".join([product.product_name for product in self.product_list])}'

    # @property
    # def user(self):
    #     return self._user

    # @staticmethod
    # def check_user(user: User) -> bool:
    #     if not isinstance(user, User):
    #         raise TypeError("Пользователь должен принадлежать классу User")
    #     return True

    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, new_product_list: list):
        if new_product_list is None:
            self._product_list = []
        else:
            for product in new_product_list:
                if not isinstance(product, Product):
                    raise TypeError("Корзина должна содержать продукты")
            self._product_list = new_product_list

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Добавить можно только объект класса Product")
        self.product_list.append(product)

    def del_product(self, product: Product) -> None:
        if product not in self.product_list:
            print(f"Невозможно удалить - в корзине нет {product.product_name}")
        else:
            self.product_list.remove(product)
