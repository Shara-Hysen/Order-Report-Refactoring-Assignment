import logging

from .config import ReportConfig
from .io import load_orders, save_report
from .reports import (
    create_overview,
    create_returns_by_category,
    create_sales_summary,
)
from .transform import prepare_orders
from .validation import validate_orders


logger = logging.getLogger(__name__)


def run_pipeline(config: ReportConfig) -> None:
    """Kör hela flödet för att skapa orderrapporter."""

    logger.info("Startar orderrapport")

    data = load_orders(config.input_path)

    validate_orders(data)

    prepared_data = prepare_orders(data)

    overview = create_overview(prepared_data)

    sales_by_category = create_sales_summary(
        prepared_data,
        "product_category",
    )

    sales_by_region = create_sales_summary(
        prepared_data,
        "region",
    )

    returns_by_category = create_returns_by_category(
        prepared_data
    )

    save_report(
        overview,
        config.output_folder / "overview.csv",
    )

    save_report(
        sales_by_category,
        config.output_folder / "sales_by_category.csv",
    )

    save_report(
        sales_by_region,
        config.output_folder / "sales_by_region.csv",
    )

    save_report(
        returns_by_category,
        config.output_folder / "returns_by_category.csv",
    )

    logger.info("Klart")