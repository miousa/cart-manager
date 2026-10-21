class ItemError(Exception):
    pass


class InvalidPriceError(ItemError):
    pass


class EmptyNameError(ItemError):
    pass
