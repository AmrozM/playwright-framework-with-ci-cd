# utils/logger.py

import logging

def get_logger(name ="framework"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))

        logger.addHandler(console)
    return logger