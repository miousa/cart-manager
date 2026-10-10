from .cart import Cart


class CartManager:
    def __init__(self):
        self.carts = {}

    def add_owner(self, owner: str) -> bool:
        if owner not in self.carts:
            self.carts[owner] = {}
            return True
        return False

    def create_cart(self, owner: str, name: str) -> bool:
        if owner not in self.carts:
            print(
                f"\nОшибка: Владелец '{owner}' не найден. Сначала создайте владельца!"
            )
            return False
        if name not in self.carts[owner]:
            self.carts[owner][name] = Cart(owner, name)
            return True
        return False

    def delete_cart(self, owner: str, name: str) -> bool:
        try:
            # Пытаемся удалить корзину
            del self.carts[owner][name]
            return True
        except KeyError:
            # Ловим ошибку, если владельца или корзины нет
            print(f"\nОшибка: Владелец '{owner}' или корзина '{name}' не найдены.")
            return False

    def work_owner(self, owner: str, name: str) -> None | Cart:
        if owner in self.carts and name in self.carts[owner]:
            return self.carts[owner][name]
        return None

    def show_all(self) -> bool:
        if not self.carts:
            return False
        for owner, carts in self.carts.items():
            print(f"\n=== {owner} ===")
            if not carts:
                print("Нет корзин.")
            else:
                for i, name in enumerate(carts, start=1):
                    print(f"  {i}. {name}")

        return True

    def to_dict(self) -> dict:
        data = {}
        for owner, carts in self.carts.items():
            data.setdefault(owner, {})
            for name, cart in carts.items():
                data[owner][name] = cart.to_dict()

        return data

    @classmethod
    def from_dict(cls, data: dict) -> "CartManager":
        manager = cls()

        for owner, carts in data.items():
            manager.add_owner(owner)
            for name, cart_data in carts.items():
                manager.create_cart(owner, name)
                cart = manager.work_owner(owner, name)
                for product in cart_data["items"]:
                    cart.add_item(product["name"], product["price"])

        return manager
