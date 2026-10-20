from stock_checker.reader import Item, load_inventory


def test_reads_all_rows():
    items = load_inventory("data/sample_stock.csv")
    assert len(items) == 8


def test_first_row_is_parsed():
    first = load_inventory("data/sample_stock.csv")[0]
    assert first == Item("SS-001", "Thai Iced Tea 250ml", "bangna", 48)
