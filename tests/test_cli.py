from stock_checker import __version__
from stock_checker.__main__ import main


def test_lists_every_item(capsys):
    assert main(["data/sample_stock.csv"]) == 0
    out = capsys.readouterr().out
    assert "SS-001" in out
    assert "Roselle Juice 250ml" in out
    assert len(out.strip().splitlines()) == 8


def test_missing_file_gives_clear_error(capsys):
    assert main(["data/does_not_exist.csv"]) == 1
    assert "file not found" in capsys.readouterr().err


def test_version_is_set():
    assert __version__ == "0.0.0"
