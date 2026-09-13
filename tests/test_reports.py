import pandas as pd

from order_report.reports import (
    create_overview,
    create_returns_by_category,
    create_sales_summary,
)


def test_create_overview_calculates_values() -> None:
    # Arrange
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 2],
            "discounted_value": [100.0, 150.0, 50.0],
            "returned": [False, True, False],
        }
    )

    # Act
    result = create_overview(data)

    # Assert
    expected = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                300.0,
                2,
                1,
            ],
        }
    )

    pd.testing.assert_frame_equal(result, expected)


def test_create_sales_summary_calculates_values() -> None:
    # Arrange
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "region": ["West", "West", "East"],
            "discounted_value": [100.0, 50.0, 200.0],
            "returned": [True, False, True],
        }
    )

    # Act
    result = create_sales_summary(data, "region")

    # Assert
    expected = pd.DataFrame(
        {
            "region": ["East", "West"],
            "order_count": [1, 2],
            "total_sales": [200.0, 150.0],
            "returns": [1, 1],
            "return_rate": [1.0, 0.5],
        }
    )

    pd.testing.assert_frame_equal(result, expected)

def test_create_returns_by_category_calculates_return_rate() -> None:
    # Arrange
    data = pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "product_category": ["Books", "Books", "Electronics", "Electronics"],
            "returned": [True, False, True, True],
        }
    )

    # Act
    result = create_returns_by_category(data)

    # Assert
    expected = pd.DataFrame(
        {
            "product_category": ["Electronics", "Books"],
            "order_count": [2, 2],
            "returns": [2, 1],
            "return_rate": [1.0, 0.5],
        }
    )

    pd.testing.assert_frame_equal(result, expected)