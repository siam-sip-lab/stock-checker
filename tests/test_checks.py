import pytest

from stock_checker.checks import DEFAULT_THRESHOLD, is_low
from stock_checker.reader import Item


def item(quantity: int) -> Item:
    return Item("SS-999", "Test Drink", "bangna", quantity)


@pytest.mark.parametrize(
    ("quantity", "expected"),
    [(9, True), (10, False), (11, False)],
    ids=["below", "equal", "above"],
)
def test_is_low_against_default_threshold(quantity, expected):
    assert is_low(item(quantity)) is expected


def test_default_threshold_is_10():
    assert DEFAULT_THRESHOLD == 10


def test_custom_threshold():
    assert is_low(item(15), threshold=20) is True
