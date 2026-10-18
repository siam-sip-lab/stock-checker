"""Entry point: python -m stock_checker <csv_path>"""

import argparse
import sys

from stock_checker import __version__
from stock_checker.reader import read_stock


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stock_checker",
        description="Check stock levels from a CSV file.",
    )
    parser.add_argument("csv_path", help="path to the stock CSV file")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        items = read_stock(args.csv_path)
    except FileNotFoundError:
        print(f"error: file not found: {args.csv_path}", file=sys.stderr)
        return 1

    for item in items:
        print(f"{item.sku:<8} {item.name:<30} {item.warehouse:<14} {item.quantity:>5}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
