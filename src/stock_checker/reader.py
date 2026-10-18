"""Read stock data from CSV."""

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Item:
    sku: str
    name: str
    warehouse: str
    quantity: int


def read_stock(path: str | Path) -> list[Item]:
    """Return every row of the stock CSV as an Item."""
    with Path(path).open(newline="", encoding="utf-8") as f:
        return [
            Item(
                sku=row["sku"],
                name=row["name"],
                warehouse=row["warehouse"],
                quantity=int(row["quantity"]),
            )
            for row in csv.DictReader(f)
        ]
