from stock_checker import __version__
from stock_checker.__main__ import main


def test_main_runs_with_sample_file(capsys):
    assert main(["data/sample_stock.csv"]) == 0
    assert "data/sample_stock.csv" in capsys.readouterr().out


def test_version_is_set():
    assert __version__ == "0.0.0"
