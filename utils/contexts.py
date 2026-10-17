from time import perf_counter
from contextlib import contextmanager
from .helpers import save

design_time = "-" * 30 + "[TIME]" + "-" * 30
design_log = "-" * 30 + "[LOG]" + "-" * 31
last = "-" * 66


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        print(f"\n{design_time}\nЗагружаю данные...\n{last}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        print(
            f"\n{design_time}\nБлок загрузки занял: {self.end - self.start:.4f}\n{last}"
        )
        return False


@contextmanager
def autosave(manager):
    try:
        print(f"\n{design_log}\nНачинаем работу.\n{last}")
        yield manager
    finally:
        save(manager)
        print(f"\n{design_log}\nФайл сохранен.\n{last}")
