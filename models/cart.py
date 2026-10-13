from utils import log_calls, validate_item


class Cart:
    def __init__(self, owner: str, name: str):
        self.owner = owner
        self.name = name
        self.items = []

    """Дейтсвия с корзиной: удаление/добавление/печать предметов - их стоимости"""

    @validate_item
    @log_calls
    def add_item(self, item_name: str, price: int) -> None:
        """Добавляет товар в корзину (Имя - цена)"""
        self.items.append({"name": item_name, "price": price})

    @log_calls
    def delete_item(self, item_name: str) -> bool:
        """Удаляет товар из корзины"""
        for i, item in enumerate(self.items):
            if item["name"] == item_name:
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
                print(f"{i}. {item['name']} - {item['price']}")
        return True

    """Статистика корзины: средняя стоимость предмета/количество предмотов/общая стоимость"""

    def get_total(self) -> int:
        """Возвращает общую стоимость всех товаров в корзине"""
        return sum(item["price"] for item in self.items)

    def get_average(self) -> float:
        """Считает и возвращает среднюю стоимость товара"""
        if not self.items:
            return 0.0
        return self.get_total() / len(self.items)

    def count_items(self) -> int:
        """Возвращает количество предметов в корзине"""
        if not self.items:
            return 0
        else:
            return len(self.items)

    """Методы для преобразования из обьекта класса в словарь, а из словаря обратно в обьекты класса, с полным сохранением и без потери результата, нужны для работы с функциям для сохранение в *.json"""

    def to_dict(self) -> dict:
        """Возвращает данные обьекта превращая их в словарь (Конвертер обьекта в словарь)"""
        return {"owner": self.owner, "name": self.name, "items": self.items}

    @classmethod
    def from_dict(cls, data: dict) -> "Cart":
        """Метод применимый для класса. Собирает данные json словаря обратно в обьект"""
        cart = cls(data["owner"], data["name"])
        cart.items = data["items"]
        return cart
