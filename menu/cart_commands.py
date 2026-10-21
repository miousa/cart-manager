from typing import TYPE_CHECKING

from app_utils import numeric_check, print_cart_menu, save

from models import Cart, ItemError

if TYPE_CHECKING:
    from models import CartManager


def handle_add_item(cart: Cart, manager: CartManager) -> None:
    item = input("Введите имя товара (для добавления): ").strip()
    price = numeric_check("Введите его цену: ")

    try:
        cart.add_item(item, price)
        save(manager)
    except ItemError as e:
        print(f"\nОшибка добавления: {e}")
        return

    print(f"\nТовар {item} был успешно добавлен!")


def handle_delete_item(cart: Cart, manager: CartManager) -> None:
    item = input("Введите имя товара (для удаления): ").strip()
    if cart.delete_item(item):
        print(f"\nПредмет {item} был удален!")
        save(manager)
    else:
        print(f"Товар {item} не найден.")


def handle_show_items(cart: Cart) -> None:
    if not cart.show_items():
        print("Корзина пуста.")


def cart_menu(cart: Cart, manager: CartManager) -> None:
    actions = {
        1: handle_add_item,
        2: handle_delete_item,
        3: handle_show_items,
    }

    while True:
        print_cart_menu(cart.name)
        choice = numeric_check("Выбери действие: ")

        if choice == 0:
            print("Выход в главное меню.\n")
            break

        action = actions.get(choice)
        if action is None:
            print("Такого пункта нет, попробуй ещё раз.")
            continue

        action(cart, manager)
