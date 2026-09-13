import pandas as pd

from order_report.transform import prepare_orders


def test_prepare_orders_cleans_and_calculates_values() -> None:
    # Arrange
    data = pd.DataFrame(
        {
            "region": [" west "],
            "product_category": [" electronics "],
            "quantity": ["2"],
            "unit_price": ["100"],
            "discount": ["0.1"],
            "returned": ["YES"],
        }
    )

    # Act
    result = prepare_orders(data)

    # Assert
    assert result.loc[0, "region"] == "West"
    assert result.loc[0, "product_category"] == "Electronics"
    assert result.loc[0, "quantity"] == 2
    assert result.loc[0, "unit_price"] == 100
    assert result.loc[0, "discount"] == 0.1
    assert result.loc[0, "returned"] == True
    assert result.loc[0, "order_value"] == 200
    assert result.loc[0, "discounted_value"] == 180

def test_prepare_orders_does_not_modify_input() -> None:
    # Arrange
    data = pd.DataFrame(
        {
            "region": [" west "],
            "product_category": [" books "],
            "quantity": ["2"],
            "unit_price": ["100"],
            "discount": ["0.1"],
            "returned": ["yes"],
        }
    )

    original = data.copy(deep=True)

    # Act
    prepare_orders(data)

    # Assert
    pd.testing.assert_frame_equal(data, original)


def test_prepare_orders_handles_invalid_numeric_values() -> None:
    # Arrange
    data = pd.DataFrame(
        {
            "region": ["West", "East", "North", "South"],
            "product_category": ["Books", "Books", "Books", "Books"],
            "quantity": ["fel", "2", "3", "4"],
            "unit_price": ["fel", "100", "200", "900"],
            "discount": ["fel", "0.1", "0.2", "0.3"],
            "returned": ["no", "yes", "no", "yes"],
        }
    )

    # Act
    result = prepare_orders(data)

    # Assert
    assert result.loc[0, "quantity"] == 1
    assert result.loc[0, "unit_price"] == 200
    assert result.loc[0, "discount"] == 0