"""Central konfiguration av paketets loggning."""

import logging


LOGGER_NAME = "order_report"


def configure_logging() -> None:
    """Konfigurerar loggning för order_report."""

    package_logger = logging.getLogger(LOGGER_NAME)

    if package_logger.handlers:
        return

    package_logger.setLevel(logging.INFO)
    package_logger.propagate = False

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    package_logger.addHandler(console_handler)