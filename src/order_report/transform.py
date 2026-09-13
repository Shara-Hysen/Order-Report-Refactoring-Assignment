import pandas as pd


def clean_text_column(series: pd.Series) -> pd.Series:
    """Städar en textkolumn och ersätter saknade värden."""

    return (
        series
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )


def prepare_orders(data: pd.DataFrame) -> pd.DataFrame:
    """Städar orderdata och beräknar värden som används i rapporterna."""

    prepared = data.copy()

    prepared["region"] = clean_text_column(prepared["region"])
    prepared["product_category"] = clean_text_column(prepared["product_category"]
    )

    prepared["quantity"] = pd.to_numeric(
        prepared["quantity"], errors="coerce"
    ).fillna(1)

    prepared["unit_price"] = pd.to_numeric(
        prepared["unit_price"], errors="coerce"
    )
    prepared["unit_price"] = prepared["unit_price"].fillna(
        prepared["unit_price"].median()
    )

    prepared["discount"] = pd.to_numeric(
        prepared["discount"], errors="coerce"
    ).fillna(0)

    prepared["returned"] = (
        prepared["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )

    prepared["order_value"] = (
        prepared["quantity"] * prepared["unit_price"]
    )

    prepared["discounted_value"] = (
        prepared["order_value"] * (1 - prepared["discount"])
    )

    return prepared