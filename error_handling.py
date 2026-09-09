import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("Application started")

    number = 10
    result = number / 0

    logging.info("Calculation completed")

except Exception as e:
    logging.error("An error occurred: %s", e)

finally:
    logging.info("Application finished")