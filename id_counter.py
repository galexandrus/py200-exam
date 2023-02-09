# DONE Создать класс IdCounter (в котором хранятся генератор значений id (обычный инкремент на 1))
"""
в нем должен быть реализован простой интерфейс хранения значения и получения нового значения
"""


class IdCounter:
    id_count = 0

    @classmethod
    def increment_id_count(cls):
        cls.id_count += 1
