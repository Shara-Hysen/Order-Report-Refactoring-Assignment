import pandas as pd
import pytest

from order_report.validation import REQUIRED_COLUMNS, validate_orders


def test_empty_data_raises_value_error() -> None:
    # Arrange
    data = pd.DataFrame(columns=list(REQUIRED_COLUMNS))

    # Act + Assert
    with pytest.raises(ValueError, match="Orderdatan är tom"):
        validate_orders(data)


def test_missing_required_column_raises_value_error() -> None:
    # Arrange
    data = pd.DataFrame(
        {
            "order_id": [1],
            "order_date": ["2026-01-01"],
            "customer_id": [101],
            "region": ["West"],
            "product_category": ["Electronics"],
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.1],
        }
    )

    # Act + Assert
    with pytest.raises(ValueError, match="returned"):
        validate_orders(data)
