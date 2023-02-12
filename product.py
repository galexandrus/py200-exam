# DONE Создать класс Product (в котором хранится информация о продукте)
"""
+ в классе должны быть атрибуты (id, name, price, rating)
+ id не должен передаваться как входной аргумент. При инициализации он должен сам определяться.
+ id и name не должны иметь возможность измениться извне
+ price, rating могут меняться извне (можно сделать как свойствами, так и обычными методами, на ваше усмотрение)
+ для тех атрибутов, которым это необходимо, проведите проверку корректности значений при инициализации, если проверка
    не пройдена вызываем raise ValueError
+ для атрибутов, необходимо провести проверку типов, если проверка не пройдена вызываем raise TypeError
    среди открытых методов не должно быть методов, которые явно позволяют изменять атрибуты (т.е. если у вас есть
    защищенный атрибут и вы не хотите, чтобы пользователь его менял, то сделайте защищенный метод,
    который будете вызывать вы как разработчик)
+ реализуйте __str__ и __repr__ методы. В __str__ вывести строку вида {id}_{name}
"""
# DONE Выберите для себя направление своего магазина - выбран чайный магазин
# DONE Создайте генераторы для создания продуктов.
"""
+ Постарайтесь чтобы генератор выдавал хотя бы приближенные значения с реальностью. Можете использовать как сторонние
    библиотеки, так и просто брать случайное значение из сформированного вами списка.
+ Значения цены и рейтинга округлите до 2-ух знаков.
"""
from id_counter import IdCounter
from typing import Union
import re
import faker
import random


class Product(IdCounter):
    """
    Класс служит для создания товаров.
    """
    def __init__(self, product_name: str, price: Union[int, float], rating: Union[int, float] = 0):
        """
        Генератор товаров. 
        :param product_name: Наименование товара. 
        :param price: Цена товара. 
        :param rating: Рейтинг товара. По умолчанию равен 0.
        """
        self.check_product_name(product_name)
        self._product_name = product_name
        self.price = price
        self.rating = rating
        self._product_id = self.__class__.increment_id_count()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.product_name}, {self.price}, {self.rating})"

    def __str__(self):
        return f"{self.product_id}_{self.product_name}"

    @property
    def product_id(self):
        return self._product_id

    @property
    def product_name(self):
        return self._product_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: Union[int, float]) -> None:
        """
        Устанавливает цену на товар.
        :param new_price: Цена.
        :return: None
        """
        if not (isinstance(new_price, int) or isinstance(new_price, float)):
            raise TypeError("Цена товара должна быть int или float")
        self._price = round(new_price, 2)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating: Union[int, float]) -> None:
        """
        Устанавливает рейтинг товара.
        :param new_rating: Рейтинг. Число от 0 до 10.
        :return: None
        """
        if not (isinstance(new_rating, int) or isinstance(new_rating, float)):
            raise TypeError("Рейтинг должен быть int или float")
        if 0 < new_rating > 10:
            raise ValueError("Значение должно быть от 0 до 10")
        if isinstance(new_rating, int):
            new_rating = float(new_rating)
        self._rating = round(new_rating, 2)

    @staticmethod
    def check_product_name(product_name: str) -> bool:
        """
        Проверка наименования товара. Оно может содержать только буквы, цифры, пробелы, подчёркивания '_' и дефисы '-'.
        :param product_name: Наименование товара.
        :return: bool
        """
        if not isinstance(product_name, str):
            raise TypeError("Наименование продукта должно быть типа str")
        if re.search(re.compile(r'[^\w\- ]'), product_name) is not None:
            raise ValueError("Наименование товара может содержать только буквы, цифры, пробелы, "
                             "подчёркивания '_' и дефисы '-'")
        return True

    @classmethod
    def product_gen(cls):

        fake_obj = faker.Faker("en")

        berries = [
            "cherry",
            "grapes",
            "raspberry",
            "strawberry",
            'watermelon',
            "cranberry",
            "gooseberry"
        ]

        fruits = [
            "apple",
            "apricot",
            "banana",
            "coconut",
            "lemon",
            "lime",
            "orange",
            "pear",
            "peach",
            "plum",
            "grapefruit"
        ]

        colour = fake_obj.safe_color_name()
        berry = berries[random.randrange(0, len(berries))]
        fruit = fruits[random.randrange(0, len(fruits))]
        if random.randrange(0, 2) == 0:
            name = colour + " " + berry + " tea"
        else:
            name = colour + " " + fruit + " tea"
        price = random.randrange(10000, 1000001) / 100
        rating = random.randrange(0, 1001) / 100
        yield cls(name, price, rating)
