from typing import TYPE_CHECKING

from app_utils import autosave, save, stats_cart

from .cart_commands import cart_menu

if TYPE_CHECKING:
    from models import CartManager


def handle_add_owner(manager: CartManager) -> None:
    with autosave(manager):
        owner = input("\nИмя владельца: ").strip()
        if not owner.replace(" ", ""):
            print("Имя владельца не может быть пустым")
            return

        if manager.add_owner(owner):
            print(f"Владелец {owner} был создан!\n")
        else:
            print("Такой владелец уже есть")
            print("Возвращаюсь в меню...\n")


def handle_create_cart(manager: CartManager) -> None:
    with autosave(manager):
        owner = input("\nИмя владельца: ").strip()
        name_cart = input("Имя корзины: ").strip()
        flag = manager.create_cart(owner, name_cart)

        if flag:
            print(
                f"Корзина '{name_cart}' для владельца "
                f"'{owner}' была создана!\n"
            )
            save(manager)
        elif flag is False:
            print(
                f"Корзина '{name_cart}' для владельца "
                f"'{owner}' уже существует!\n"
            )


def handle_delete_cart(manager: CartManager) -> None:
    with autosave(manager):
        if not manager.show_all():
            print("Нет корзин для удаления")
            return

        owner = input("\nИмя владельца: ").strip()
        name_cart = input("Имя корзины (для удаления): ").strip()

        if manager.delete_cart(owner, name_cart):
            print(f"Корзина {name_cart} была удалена!\n")


def handle_open_cart(manager: CartManager) -> None:
    manager.show_all()
    owner = input("\nИмя владельца: ").strip()
    name_cart = input("Имя корзины: ").strip()

    cart = manager.work_owner(owner, name_cart)

    if cart is None:
        print("Попробуйте еще раз!")
        return

    cart_menu(cart, manager)


def handle_show_all(manager: CartManager) -> None:
    manager.show_all()


def handle_show_stats(manager: CartManager) -> None:
    owners = stats_cart(manager.carts)
    print("\nСтатистика:")
    for name_stat, value in owners.items():
        print(f"{name_stat} - {value}")