from stock_checker.report import low_stock_report


def test_report_lists_low_items():
    report = low_stock_report("data/sample_stock.csv")
    assert report == "3 of 8 items are LOW: SS-002, SS-004, SS-007"


def test_report_with_no_low_items():
    assert low_stock_report("data/sample_stock.csv", threshold=0) == (
        "0 of 8 items are LOW: none"
    )
