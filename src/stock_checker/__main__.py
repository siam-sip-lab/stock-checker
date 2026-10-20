"""Entry point: python -m stock_checker <csv_path> [--threshold N]"""

import argparse
import sys

from stock_checker import __version__
from stock_checker.checks import is_low
from stock_checker.config import load_threshold
from stock_checker.reader import read_stock


def non_negative_int(value: str) -> int:
    number = int(value)
    if number < 0:
        raise argparse.ArgumentTypeError("must be 0 or greater")
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stock_checker",
        description="Check stock levels from a CSV file.",
    )
    parser.add_argument("csv_path", help="path to the stock CSV file")
    parser.add_argument(
        "--threshold",
        type=non_negative_int,
        default=None,
        help="mark items below this quantity as LOW (overrides the config file)",
    )
    parser.add_argument(
        "--config",
        default="config.toml",
        help="path to the config file (default: config.toml)",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        items = read_stock(args.csv_path)
    except FileNotFoundError:
        print(f"error: file not found: {args.csv_path}", file=sys.stderr)
        return 1

    threshold = (
        args.threshold if args.threshold is not None else load_threshold(args.config)
    )
    for item in items:
        flag = "LOW" if is_low(item, threshold) else ""
        line = f"{item.sku:<8} {item.name:<30} {item.warehouse:<14} {item.quantity:>5}  {flag}"
        print(line.rstrip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
