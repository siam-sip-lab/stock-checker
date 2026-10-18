import pytest

from stock_checker import __version__
from stock_checker.__main__ import main


def lines_for(capsys, *argv: str) -> dict[str, str]:
    assert main(["data/sample_stock.csv", *argv]) == 0
    return {line.split()[0]: line for line in capsys.readouterr().out.splitlines()}


def test_lists_every_item(capsys):
    assert len(lines_for(capsys)) == 8


def test_marks_low_items_with_default_threshold(capsys):
    lines = lines_for(capsys)
    assert lines["SS-002"].endswith("LOW")      # 7  < 10
    assert not lines["SS-006"].endswith("LOW")  # 10 is not below 10


def test_threshold_option(capsys):
    lines = lines_for(capsys, "--threshold", "20")
    assert lines["SS-003"].endswith("LOW")      # 15 < 20


def test_missing_file_gives_clear_error(capsys):
    assert main(["data/does_not_exist.csv"]) == 1
    assert "file not found" in capsys.readouterr().err


def test_version_is_set():
    assert __version__ == "0.0.0"


def test_negative_threshold_is_rejected(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["data/sample_stock.csv", "--threshold", "-1"])
    assert exc.value.code == 2
    assert "must be 0 or greater" in capsys.readouterr().err
