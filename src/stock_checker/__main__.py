"""Entry point: python -m stock_checker <csv_path>"""

import argparse
import sys

from stock_checker import __version__


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
    print(f"stock_checker {__version__}: ready to read {args.csv_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
