# DONE Создать класс Password (который ответственен за выдачу хэш-значения пароля и проверке пароля с его хэш значением)
"""
реализовать методы get и check
get - выдаёт хэш-значение. Можно возпользоваться модулем hashlib. Как пример и для упрощения предлагаю воспользоваться
данным выражением hashlib.sha256(password.encode()).hexdigest(), которое вернёт хэш-значение по переданной строке
password.
Однако вы сами вольны выбирать каким методом и как возвращать хэш-значение.
Для передаваемого пароля перед получением хэш-значения должны быть произведены проверки, что пароль строкового типа
и пароль соответствует минимальным правилам (проверить можно как при помощи re, так и обычных строковых методов) пароля:
Длина не менее 8 символов
В пароле есть как цифры так и буквы
check - проверяет соотносится ли передаваемый пароль с его хэш-значением
"""
import hashlib
import re


class Password:
    def __init__(self, passwd: str):
        self.__check_plain_passwd(passwd)
        self.__hashed_passwd = self.__hashed_passwd_gen(passwd)
        # self.check_hashed_passwd(passwd, self.__hashed_passwd)

    @staticmethod
    def __check_plain_passwd(passwd: str) -> None:
        if len(passwd) < 8:
            raise(ValueError("Пароль должен содержать не менее 8 символов"))
        any_digit = re.compile(r'[0-9]')
        any_letter = re.compile(r'[a-zA-Z]')
        if re.search(any_digit, passwd) is None:
            raise ValueError("Пароль должен содержать буквы и цифры")
        elif re.search(any_letter, passwd) is None:
            raise ValueError("Пароль должен содержать буквы и цифры")

    @staticmethod
    def __hashed_passwd_gen(passwd: str) -> str:
        return hashlib.sha256(passwd.encode()).hexdigest()

    def check_hashed_passwd(self, passwd: str, hashed_passwd: str):
        if self.__hashed_passwd_gen(passwd) != hashed_passwd:
            raise ValueError(f'Пароль {passwd} НЕ соответствует хэш-значению {hashed_passwd}')
        # print("Пароль соответствует хэш-значению")

    @property
    def hashed_passwd(self) -> str:
        return self.__hashed_passwd
