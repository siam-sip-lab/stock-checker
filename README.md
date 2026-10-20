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

## Usage

```bash
python -m stock_checker <csv_path> [--threshold N] [--config PATH] [--format text|json]
```

| Option | Meaning | Default |
| --- | --- | --- |
| `--threshold N` | mark items below N as LOW; overrides every value in the config file | from `config.toml` |
| `--config PATH` | config file to read | `config.toml` |
| `--format text\|json` | output format | `text` |

Per-warehouse thresholds go in `config.toml` under `[warehouses.<name>]`.

### Example output

Text (default):

```text
SS-001   Thai Iced Tea 250ml            bangna            48
SS-002   Lemongrass Soda 330ml          bangna             7  LOW
```

JSON (`--format json`), one object per item:

```json
{
  "sku": "SS-002",
  "name": "Lemongrass Soda 330ml",
  "warehouse": "bangna",
  "quantity": 7,
  "low": true
}
```

## How to contribute

Follow the org [contributing guide](https://github.com/siam-sip-lab/.github/blob/main/CONTRIBUTING.md).

## Owners

See [.github/CODEOWNERS](.github/CODEOWNERS).
