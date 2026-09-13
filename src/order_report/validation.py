import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
}


def validate_orders(data: pd.DataFrame) -> None:
    """Kontrollerar att orderdatan innehåller nödvändiga kolumner och rader."""

    if data.empty:
        raise ValueError("Orderdatan är tom.")

    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Följande kolumner saknas: {missing}")