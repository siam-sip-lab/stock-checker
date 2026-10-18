from stock_checker.reader import Item, read_stock


def test_reads_all_rows():
    items = read_stock("data/sample_stock.csv")
    assert len(items) == 8


def test_first_row_is_parsed():
    first = read_stock("data/sample_stock.csv")[0]
    assert first == Item("SS-001", "Thai Iced Tea 250ml", "bangna", 48)
