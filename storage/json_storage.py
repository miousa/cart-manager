from json import JSONDecodeError, dump, load
from pathlib import Path

from .base import Storage


class JsonStorage(Storage):
    def __init__(self, path: str | Path):
        self.path = path

    def save(self, data: dict) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            dump(data, f, ensure_ascii=False, indent=2)

    def load(self) -> dict:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return load(f)
        except FileNotFoundError:
            return {}
        except JSONDecodeError:
            print("Файл поврежден и будет перезаписан.")
            return {}
