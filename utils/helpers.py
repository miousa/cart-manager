from typing import TYPE_CHECKING
from storage import save_data

if TYPE_CHECKING:
    from models import CartManager


def numeric_check(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введи число!")


def save(manager: CartManager) -> None:
    save_data(manager.to_dict())


# Визуализация наполнения массива carts
"""
carts = {
    'owner1': {
        'cart1': __object__.Cart(class) -> [{item: price}, {item: price}, ...],
        'cart2': __object__.Cart(class) -> [{item: price}, {item: price}, ...]
    },
    'owner2': {
        'cart1': __object__.Cart(class) -> [{item: price}, {item: price}, ...],
       'cart2': __object__.Cart(class) -> [{item: price}, {item: price}, ...]
    }
}
"""


def stats_cart(carts: dict) -> dict:
    total_carts = 0
    total_products = 0
    total_price = 0

    # Проходимся по списку из значений каждого владельца
    for owner_carts in carts.values():
        # Считаем кол-во всех корзин у всех владельцев
        total_carts += len(owner_carts)

        # Проходимся по списку обьектов классa Cart
        for cart in owner_carts.values():  # cart это экземпляр класса Cart
            # Далее считаем общее количество продуктов с помощью метода count_items() у класса Cart
            total_products += cart.count_items()
            # Таким же образом считаем общую стоимость всех предметов
            total_price += cart.get_total()

    # Считаем среднюю стоимость одного предмета и проверяем, чтобы был хотябы 1 предмет
    average = (
        total_price / total_products if total_products > 0 else 0
    )  # Защита от ZeroDivisionError

    # Возвращаем нашу статистику в dict
    return {
        "Владельцев": len(carts),
        "Корзин": total_carts,
        "Товаров": total_products,
        "Общая стоимость": total_price,
        "Средняя цена продукта": average,
    }


# Печать 1-го меню
def print_cart_menu(name: str) -> None:
    menu_text = (
        f"{'-' * 40}\n"
        f"{' ' * 12} {name.upper()}\n"
        f"{' ' * 4}1. Добавить товар в корзину\n"
        f"{' ' * 4}2. Удалить товар с корзины\n"
        f"{' ' * 4}3. Показать все товары\n"
        f"{' ' * 4}0. Выход в главное меню\n"
        f"{'-' * 40}\n"
    )
    print(menu_text)


# Печать 2-ого меню
def print_menu() -> None:
    menu_text = (
        f"{'-' * 40}\n"
        f"{'-' * 17} MENU {'-' * 17}\n"
        f"{' ' * 4}1. Создать владельца\n"
        f"{' ' * 4}2. Создать корзину\n"
        f"{' ' * 4}3. Удалить корзину\n"
        f"{' ' * 4}4. Войти в корзину\n"
        f"{' ' * 4}5. Показать всех владельцев\n"
        f"{' ' * 4}6. Статистика\n"
        f"{' ' * 4}0. Выход\n"
        f"\n{'-' * 40}\n"
    )
    print(menu_text)
