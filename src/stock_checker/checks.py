"""Stock level rules."""

from stock_checker.reader import Item

DEFAULT_THRESHOLD = 10


def is_low(item: Item, threshold: int = DEFAULT_THRESHOLD) -> bool:
    """An item is low when its quantity is strictly below the threshold."""
    return item.quantity < threshold
