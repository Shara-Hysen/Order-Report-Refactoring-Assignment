from order_report import ReportConfig, run_pipeline
from order_report.logging_config import configure_logging


def main() -> None:
    configure_logging()
    run_pipeline(ReportConfig())


if __name__ == "__main__":
    main()