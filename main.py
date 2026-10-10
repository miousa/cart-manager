from utils import (
    print_cart_menu,
    print_menu,
    numeric_check,
    stats_cart,
    save,
)
from models import Cart, CartManager
from storage import load_data


def cart_menu(cart: Cart, manager: CartManager) -> None:
    while True:
        print_cart_menu(cart.name)
        choice = numeric_check("Выбери действие: ")

        if choice == 0:
            break

        elif choice == 1:
            item = input("Введите имя товара (для добавления): ").strip()
            price = numeric_check("Введите его цену: ")
            cart.add_item(item, price)
            print(f"Товар {item} добавлен.")
            save(manager)

        elif choice == 2:
            item = input("Введите имя товара (для удаления): ").strip()
            if cart.delete_item(item):
                print(f"\nПредмет {item} был удален!")
                save(manager)
            else:
                print(f"Товар {item} не найден.")

        elif choice == 3:
            if not cart.show_items():
                print("Корзина пуста.")

        else:
            print("Такого пункта нет, попробуй ещё раз.")


def manager_menu() -> None:
    manager = CartManager.from_dict(load_data())

    while True:
        print_menu()
        choice = numeric_check("Выбери действие: ")

        if choice == 0:
            break

        elif choice == 1:
            owner = input("Имя владельца: ").strip()
            if manager.add_owner(owner):
                print(f"Владелец {owner} был создан!\n")
                save(manager)

            else:
                print("Такой владелец уже есть")
                print("Возвращаюсь в меню...\n")
                continue

        elif choice == 2:
            owner = input("Имя владельца: ").strip()
            name_cart = input("Имя корзины (если нету создадится новая): ").strip()
            if manager.create_cart(owner, name_cart):
                print(f"Корзина '{name_cart}' для владельца '{owner}' была создана!\n")
                save(manager)
            else:
                print(f"Корзина '{name_cart}' для владельца '{owner}' уже имеется\n")

        elif choice == 3:
            if not manager.show_all():
                print("Нет корзин для удаления")
                continue
            owner = input("\nИмя владельца: ").strip()
            name_cart = input("Имя корзины (для удаления): ").strip()

            if manager.delete_cart(owner, name_cart):
                print(f"Корзина {name_cart} была удалена!\n")
                save(manager)

        elif choice == 4:
            manager.show_all()
            owner = input("Имя владельца: ").strip()
            name_cart = input("Имя корзины (для входа): ").strip()

            cart = manager.work_owner(owner, name_cart)

            if cart is None:
                print("Попробуйте еще раз!")
                continue
            cart_menu(cart, manager)

        elif choice == 5:
            manager.show_all()

        elif choice == 6:
            print("\nСтатистика:")
            owners = stats_cart(manager.carts)
            for name_stat, value in owners.items():
                print(f"{name_stat} - {value}")

        else:
            print("Такого пункта нет, попробуй ещё раз.")


def main():
    manager_menu()


if __name__ == "__main__":
    main()
