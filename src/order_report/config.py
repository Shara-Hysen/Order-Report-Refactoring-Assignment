from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ReportConfig:
    """Sökvägar som behövs för att skapa orderrapporterna."""

    input_path: Path = Path("data/orders.csv")
    output_folder: Path = Path("output")

