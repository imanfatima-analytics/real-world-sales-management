import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")

logging.info("Loading sales data")

logging.warning("This is a warning message")

logging.error("This is an error message")

logging.info("Application finished")