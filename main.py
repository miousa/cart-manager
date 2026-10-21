from app_utils import (
    DATA_FILE,
    Timer,
    numeric_check,
    print_menu,
)

from menu import (
    handle_add_owner,
    handle_create_cart,
    handle_delete_cart,
    handle_open_cart,
    handle_show_all,
    handle_show_stats,
)

from models import CartManager

from storage import JsonStorage


def manager_menu() -> None:
    with Timer():
        storage = JsonStorage(DATA_FILE)
        manager = CartManager.from_dict(storage.load())

    actions = {
        1: handle_add_owner,
        2: handle_create_cart,
        3: handle_delete_cart,
        4: handle_open_cart,
        5: handle_show_all,
        6: handle_show_stats,
    }

    while True:
        print_menu()
        choice = numeric_check("Выбери действие: ")

        if choice == 0:
            break

        action = actions.get(choice)
        if action is None:
            print("Такого пункта нет, попробуй ещё раз.")
            continue

        action(manager)


def main():
    manager_menu()


if __name__ == "__main__":
    main()
