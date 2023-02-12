# DONE В блоке if __name__ == '__main__' проверьте функциональность добавления продуктов в корзину
#  и отображения корзины пользователя.
from store import Store
from product import Product


if __name__ == "__main__":

    my_store = Store()
    print(my_store.store_name)
    for _ in range(2):
        my_store.add_random_product()
    ceylon_tea = Product("ceylon tea", 34)
    my_store.user.cart.add_product(ceylon_tea)
    my_store.cart_view()
    my_store.user.cart.del_product(ceylon_tea)
    my_store.cart_view()
