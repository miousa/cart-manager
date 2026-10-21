class Storage:
    def save(self, data: dict) -> None:
        raise NotImplementedError("save() должен быть реализован.")

    def load(self) -> dict:
        raise NotImplementedError("load() должен быть реализован.")
