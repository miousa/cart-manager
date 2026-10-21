from functools import wraps
from time import perf_counter, sleep
from typing import Callable

design = "-" * 30 + "[LOG]" + "-" * 31 + '\n'
last = "-" * 66


def log_calls(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):        
        print(f"{design}\nВызов функции: {func.__name__}c arg={args} kw={kwargs}")

        print(f"Обьяснение функции: {func.__doc__}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} вернул {result}\n{last}")
        return result

    return wrapper


def time_counter(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        result = func(*args, **kwargs)

        end = perf_counter()
        print(f"[TIME] {func.__name__} выполнилась за {end - start:.4f} сек.")
        return result

    return wrapper


def validate_item(func: Callable):
    @wraps(func)
    def wrapper(self, item_name, price):
        if price > 0:

            if not item_name.replace(" ", ""):
                print("Имя не может быть пустым")
                return
            result = func(self, item_name, price)

            print(f"Товар {item_name} добавлен.")
            return result
        else:
            print("Цена товара не может быть 0 или отрицательной")
            return

    return wrapper


def retry(max_attempts: int, delay: float):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Попытка {attempt}/{max_attempts} упала: {e}")
                    if attempt == max_attempts:
                        raise
                    sleep(delay)

        return inner

    return wrapper
