# TODO В блоке if __name__ == '__main__' проверьте функциональность добавления продуктов в корзину
#  и отображения корзины пользователя.

from passwd import Password


if __name__ == "__main__":

    super_passwd = Password("asdf1234")

    # while True:
    #     try:
    #         super_passwd = Password(str(input("Введите пароль: ")))
    #     except ValueError:
    #         print("Пароль должен содержать не менее 8 символов (буквы и цифры)")
    #         continue
    #     break

    print(super_passwd.hashed_passwd)
    print(super_passwd)
    print(super_passwd.check_hashed_passwd("hkhjk", super_passwd.hashed_passwd))
