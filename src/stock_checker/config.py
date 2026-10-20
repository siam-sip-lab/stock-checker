"""Load settings from config.toml."""

import tomllib
from pathlib import Path

from stock_checker.checks import DEFAULT_THRESHOLD


def load_threshold(path: str | Path = "config.toml") -> int:
    """Return the threshold from the config file, or the default if there is none."""
    config_path = Path(path)
    if not config_path.exists():
        return DEFAULT_THRESHOLD
    with config_path.open("rb") as f:
        data = tomllib.load(f)
    return int(data.get("threshold", DEFAULT_THRESHOLD))


def load_warehouse_thresholds(path: str | Path = "config.toml") -> dict[str, int]:
    """Return {warehouse: threshold} for warehouses with their own setting."""
    config_path = Path(path)
    if not config_path.exists():
        return {}
    with config_path.open("rb") as f:
        data = tomllib.load(f)
    return {
        name: int(settings["threshold"])
        for name, settings in data.get("warehouses", {}).items()
        if "threshold" in settings
    }
