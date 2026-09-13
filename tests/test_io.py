from pathlib import Path

import pytest
import pandas as pd

from order_report.io import load_orders, save_report


def test_load_orders_raises_when_file_is_missing(tmp_path: Path) -> None:
    # Arrange
    missing_file = tmp_path / "missing.csv"

    # Act + Assert
    with pytest.raises(FileNotFoundError, match="Datafilen finns inte"):
        load_orders(missing_file)


def test_load_orders_reads_csv_file(tmp_path: Path) -> None:
    # Arrange
    file_path = tmp_path / "orders.csv"

    expected = pd.DataFrame(
        {
            "order_id": [1, 2],
            "region": ["West", "East"],
        }
    )

    expected.to_csv(file_path, index=False)

    # Act
    result = load_orders(file_path)

    # Assert
    pd.testing.assert_frame_equal(result, expected)

def test_save_report_creates_folder_and_file(tmp_path: Path) -> None:
    # Arrange
    report = pd.DataFrame(
        {
            "metric": ["total_sales"],
            "value": [500],
        }
    )

    file_path = tmp_path / "output" / "report.csv"

    # Act
    save_report(report, file_path)

    # Assert
    assert file_path.exists()