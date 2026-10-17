from typing import TYPE_CHECKING
from storage import save_data
from .decorators import log_calls

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
        'cart1': __object__.Cart(class) -> [__obj__.Item(class), __obj__.Item(class), ...],
        'cart2': __object__.Cart(class) -> [__obj__.Item(class), __obj__.Item(class), ...]
    },
    'owner2': {
        'cart1': __object__.Cart(class) -> [__obj__.Item(class), __obj__.Item(class), ...],
       'cart2': __object__.Cart(class) -> [__obj__.Item(class), __obj__.Item(class), ...]
    }
}
"""


@log_calls
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
            # Далее считаем общее количество продуктов с помощью __len__ у класса Cart
            total_products += len(cart)
            # Cчитаем общую стоимость всех предметов
            total_price += cart.total

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
        f"\n{'-' * 30 + name.upper() + '-' * 30}\n"
        f"\n{' ' * 4}1. Добавить товар в корзину\n"
        f"{' ' * 4}2. Удалить товар с корзины\n"
        f"{' ' * 4}3. Показать все товары\n"
        f"{' ' * 4}0. Выход в главное меню\n"
        f"\n{'-' * (60 + len(name))}\n"
    )
    print(menu_text)


# Печать 2-ого меню
def print_menu() -> None:
    menu_text = (
        f"\n{'-' * 30 + 'MENU' + '-' * 30}\n"
        f"\n{' ' * 4}1. Создать владельца\n"
        f"{' ' * 4}2. Создать корзину\n"
        f"{' ' * 4}3. Удалить корзину\n"
        f"{' ' * 4}4. Войти в корзину\n"
        f"{' ' * 4}5. Показать всех владельцев\n"
        f"{' ' * 4}6. Статистика\n"
        f"{' ' * 4}0. Выход\n"
        f"\n{'-' * 64}\n"
    )
    print(menu_text)
