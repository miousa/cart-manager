class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item({self.name!r}, {self.price!r})"

    def __str__(self):
        return f"{self.name} — {self.price} руб."

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))

    def to_dict(self) -> dict:
        """Возвращает данные обьекта превращая их в словарь (Конвертер обьекта в словарь)"""
        return {"name": self.name, "price": self.price}

    @classmethod
    def from_dict(cls, data: dict) -> "Item":
        """Метод применимый для класса. Собирает данные json словаря обратно в обьект"""
        item = cls(data["name"], data["price"])
        return item
