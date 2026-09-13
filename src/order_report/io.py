import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)


def load_orders(path: Path) -> pd.DataFrame:
    """Läser in orderdata från en CSV-fil."""

    if not path.exists():
        raise FileNotFoundError(f"Datafilen finns inte: {path}")

    data = pd.read_csv(path)

    logger.info("Läste in %d rader från %s", len(data), path)

    return data

def save_report(report: pd.DataFrame, path: Path) -> None:
    """Sparar en rapport som en CSV-fil."""

    path.parent.mkdir(parents=True, exist_ok=True)

    report.to_csv(path, index=False)

    logger.info("Sparade rapport till %s", path)