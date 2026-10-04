import math as m
import time

from utils import numeric_check


def time_count(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        print(f"\n{'*' * 20}\n-Ищу корзину...")
        time.sleep(1)
        print(f"-Обновляю данные...\n{'*' * 20}")
        print("Ответ:\n")

        result = func(*args, **kwargs)

        end = time.time()
        print(f"(Время ожидания: {end - start:.2f} секунд)")

        return result

    return wrapper


class CartManager:
    def __init__(self):
        self.carts = {}

    def add_owner(self, owner: str) -> None:
        if owner not in self.carts:
            self.carts[owner] = {}
        else:
            print("Такой владелец уже есть!")

    def create_cart(self, owner: str, name: str) -> None:
        if name not in self.carts[owner]:
            self.carts[owner][name] = Cart(owner)
        else:
            print("Такая корзина уже есть!\n")

    def get_cart(self, owner: str, name: str):  # IS NONE (CHECK)
        if (owner not in self.carts) or (name not in self.carts[owner]):
            return None

        return self.carts[owner][name]

    def remove_owner(self, owner: str) -> bool:
        print("\nУдаление...")
        time.sleep(2)
        if owner in self.carts:
            del self.carts[owner]
            return True
        return False

    def remove_cart(self, owner: str, name: str) -> bool:
        print("\nУдаление...")
        time.sleep(2)
        if owner in self.carts and name in self.carts[owner]:
            del self.carts[owner][name]
            return True
        return False

    def rename_cart(self, owner: str, old: str, new: str) -> bool:  # BOOL CHECK
        print("Переименовываю...")
        time.sleep(1)
        status = True

        if (owner not in self.carts) or (old not in self.carts[owner]):
            status = False
        else:
            self.carts[owner][new] = self.carts[owner].pop(old)
        return status

    def show_all(self) -> None:
        for owner, carts in self.carts.items():
            print(f"\n=== {owner} ===")
            for i, name in enumerate(carts, start=1):
                print(f"{i}. {name}\n")


class Cart:
    def __init__(self, owner: str):
        self.owner = owner
        self.items = []

    @time_count
    def add_item(self, name: str, price: int) -> None:
        time.sleep(0.5)
        print("Добавляю предмет в корзину...")
        time.sleep(2)
        self.items.append({"name": name, "price": price})
        print("Успешно!")

    def get_total(self) -> int:
        total = 0
        if self.items:
            for items in self.items:
                total += items["price"]
        else:
            print("В корзине пусто!")

        return total

    def get_average(self, total: int) -> float:
        return total / len(self.items)

    def show_items(self) -> None:
        if not self.items:
            time.sleep(0.5)
            print("В корзине пусто!")
        else:
            print(f"{'-*' * 4} CART {'-*' * 4}\n")
            for i, items in enumerate(self.items, start=1):
                time.sleep(2)
                print(f"{i}. {items['name']} - {items['price']}")

    @time_count
    def count_items(self) -> int:
        if not self.items:
            time.sleep(0.5)
            print("В корзине пусто!")
            return 0
        else:
            return len(self.items)


def input_owner() -> str:
    return input("\nВладелец: ").strip()


def input_name() -> str:
    return input("Название корзины: ").strip()


# def print_menu_for_bank():
#     print(f"{'-' * 40}\n{'-' * 17} MENU {'-' * 17}\n{'-' * 40}\n")
#     print(f"{' ' * 4}1. Создать корзину в OZON")
#     print(f"{' ' * 4}2. Создать корзину в WILDBERRIS")
#     print(f"{' ' * 4}3. Создать корзину в ALIEXPRESS")
#     print(f"\n{'-' * 40}\n{'-' * 40}\n")


def print_menu() -> None:
    print(f"{'-' * 40}")
    print(f"{'-' * 17} MENU {'-' * 17}")
    print(f"{'-' * 40}\n")
    print(f"{' ' * 4}1. Создать владельца")
    print(f"{' ' * 4}2. Создать корзину")
    print(f"{' ' * 4}3. Показать все корзины")
    print(f"{' ' * 4}4. Добавить товар в корзину")
    print(f"{' ' * 4}5. Удалить корзину")
    print(f"{' ' * 4}6. Переименовать корзину")
    print(f"{' ' * 4}7. Статистика")
    print(f"{' ' * 4}0. Выход")
    print(f"\n{'-' * 40}\n")


def main():
    manager = CartManager()

    while True:
        print_menu()
        choice = numeric_check("Выбери действие: ")

        if choice == 1:
            print("\n=== Создание владельца ===\n")
            print("(Пример: Владелец - Илья)")
            while True:
                owner = input_owner()

                if not owner:
                    print("Имя владельца не может быть пустым!")
                    continue
                else:
                    manager.add_owner(owner)
                    print(f"\nВладелец {owner} был создан!")
                    break
        elif choice == 3:
            manager.show_all()


if __name__ == "__main__":
    main()
