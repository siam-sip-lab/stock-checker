from stock_checker.checks import DEFAULT_THRESHOLD
from stock_checker.config import load_threshold, load_warehouse_thresholds


def test_missing_file_uses_default(tmp_path):
    assert load_threshold(tmp_path / "nope.toml") == DEFAULT_THRESHOLD


def test_reads_threshold_from_file(tmp_path):
    config = tmp_path / "config.toml"
    config.write_text("threshold = 7\n", encoding="utf-8")
    assert load_threshold(config) == 7


def test_repo_config_matches_default():
    assert load_threshold("config.toml") == 10


def test_reads_warehouse_thresholds(tmp_path):
    config = tmp_path / "config.toml"
    config.write_text(
        "threshold = 10\n[warehouses.bangna]\nthreshold = 20\n", encoding="utf-8"
    )
    assert load_warehouse_thresholds(config) == {"bangna": 20}


def test_no_warehouses_section(tmp_path):
    config = tmp_path / "config.toml"
    config.write_text("threshold = 10\n", encoding="utf-8")
    assert load_warehouse_thresholds(config) == {}
