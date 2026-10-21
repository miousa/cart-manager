# Cart Manager

Консольное приложение для управления корзинами покупок. Позволяет создавать владельцев, корзины, добавлять товары и считать статистику.

---

## Possibilities

- __CartManager__
    - __Создание владельцев__
    - __Создание нескольких корзин для одного владельца__
    - __Удаление корзин и владельцев__
    - __Просмотр всех корзин__
- __Cart__
    - __Добавление товаров с ценой__
    - __Удаление товаров__
    - __Просмотр всех товаров__
- __Statistcis (app_utils/helpers.py)__
    - __Количество владельцев__
    - __Количество корзин__
    - __Количество товаров__
    - __Подсчёт общей стоимости__
    - __Подсчет средней цены продукта__
- __Storage__
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
| ├── item.py
| └── exceptions.py
├── storage/
| ├── __init__.py
| ├── base.py
| └── json_storage.py
├── app_utils/
| ├── __init__.py
| ├── decorators.py
| ├── helpers.py
| ├── paths.py
| └── contexts.py
├── menu/
| ├── __init__.py
| ├── cart_commands.py
| └── manager_commands.py
```

## About the projects

*Проект был создан в качестве учебной цели: понять как работают обьекты в __python__, иерархия __моделей__, понятия строение архитектуры, модулейи и многово другого...*


