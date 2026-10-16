from time import perf_counter
from contextlib import contextmanager
from .helpers import save


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        print(f"[TIME] блок занял {self.end - self.start:.4f}")
        return False


@contextmanager
def autosave(manager):
    try:
        print("[LOG] Начинаем работу")
        yield manager
    finally:
        save(manager)
        print("[LOG] Файл сохранен")
