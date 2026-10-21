from app_utils import log_calls

from .item import Item


class Cart:
    def __init__(self, owner: str, name: str):
        self.owner = owner
        self.name = name
        self.items = []

    """Дейтсвия с корзиной: удаление/добавление/печать"""

    @log_calls
    def add_item(self, item_name: str, price: int) -> None:
        """Добавляет товар в корзину (Имя - цена)"""
        self.items.append(Item(item_name, price))

    @log_calls
    def delete_item(self, item_name: str) -> bool:
        """Удаляет товар из корзины"""
        for i, item in enumerate(self.items):
            if item.name == item_name:
                del self.items[i]
                return True
        return False

    def show_items(self) -> bool:
        """Печатает все товары в корзине"""
        if not self.items:
            return False
        else:
            print("\nСодержимое:\n")
            for i, item in enumerate(self.items, start=1):
                print(f"{i}. {item.name} - {item._price}")
        return True

    """Магические методы"""

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item_name):
        return any(i.name == item_name for i in self.items)

    """Статистика корзины: средняя стоимость предмета/количество предмотов/общая стоимость"""

    @property
    def total(self) -> int:
        """Возвращает общую стоимость всех товаров в корзине"""
        return sum(item.price for item in self.items)

    @property
    def average(self) -> float:
        """Считает и возвращает среднюю стоимость товара"""
        if not self.items:
            return 0.0
        return self.total / len(self.items)

    """Методы для преобразования из обьекта класса в словарь, а из словаря обратно в обьекты класса, с полным сохранением и без потери результата, нужны для работы с функциям для сохранение в *.json"""

    def to_dict(self) -> dict:
        """Возвращает данные обьекта превращая их в словарь (Конвертер обьекта в словарь)"""
        data = {"owner": self.owner, "name": self.name, "items": []}
        for item in self.items:
            data["items"].append(item.to_dict())

        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Cart":
        """Метод применимый для класса. Собирает данные json словаря обратно в обьект"""
        cart = cls(data["owner"], data["name"])
        cart.items = [Item.from_dict(item) for item in data["items"]]
        return cart
