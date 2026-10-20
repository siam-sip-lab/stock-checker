# stock-checker

[![ci](https://github.com/siam-sip-lab/stock-checker/actions/workflows/ci.yml/badge.svg)](https://github.com/siam-sip-lab/stock-checker/actions/workflows/ci.yml)

CLI that checks stock levels from a CSV file and flags low stock.

## Quick start

Requires Python 3.12 or newer.

```bash
python -m venv .venv
source .venv/Scripts/activate      # Git Bash on Windows (macOS/Linux: .venv/bin/activate)
pip install -e ".[dev]"
python -m stock_checker data/sample_stock.csv
pytest
```

## How to contribute

Follow the org [contributing guide](https://github.com/siam-sip-lab/.github/blob/main/CONTRIBUTING.md).

## Owners

See [.github/CODEOWNERS](.github/CODEOWNERS).
