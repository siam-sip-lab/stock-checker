"""Low-stock summary for reorder planning."""

from pathlib import Path

from stock_checker.checks import DEFAULT_THRESHOLD, is_low
from stock_checker.reader import load_inventory


def low_stock_report(path: str | Path, threshold: int = DEFAULT_THRESHOLD) -> str:
    """Return a one-line summary and the SKUs that need reordering."""
    items = load_inventory(path)
    low = [item.sku for item in items if is_low(item, threshold)]
    return f"{len(low)} of {len(items)} items are LOW: {', '.join(low) or 'none'}"
