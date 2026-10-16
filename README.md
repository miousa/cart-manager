# Cart Manager

Консольное приложение для управления корзинами покупок. Позволяет создавать владельцев, корзины, добавлять товары и считать статистику.

---

## Possibilities

- __Создание владельцев__
- __Создание нескольких корзин для одного владельца__
- __Добавление товаров с ценой__
- __Подсчёт общей стоимости__
- __Переименование корзин__
- __Удаление корзин и владельцев__
- __Просмотр всех корзин__
- __Сохранение данных в JSON__

---

## Technologies

- **Python 3.12+**
- *standart library*: `json`, `time`
- **Git** для версионирования

---

## Downloads

```bash
git clone https://github.com/miousa/cart-manager.git
cd cart-manager
```

## Structures
```text
cart/
├── .gitignore
├── main.py
├── README.md
├── requirements
├── TODO.md
└── data/
| └── carts.json
├── models/
| ├── __init__.py
| ├── cart.py
| ├── manager.py
| └── item.py
├── storage/
| ├── __init__.py
| └── json_storage.py
├── utils/
| ├── __init__.py
| ├── decorators.py
| ├── helpers.py
| └── contexts.py
```




