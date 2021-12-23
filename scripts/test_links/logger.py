import logging
from datetime import datetime
from pathlib import Path

SUFFIX_TIMESTAMP = datetime.now().strftime("_%Y%m%d_%H%M")

SOURCES_DIR = Path(__file__).parent.resolve()
LOGS_DIR = SOURCES_DIR / "logs"
LOGS_FILE = LOGS_DIR / "test_links"


def get_logger(name: str = __name__):
    if name == "__main__":
        name = "main"

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    fmt = "%(asctime)s | %(name)s |  %(levelname)s: %(message)s"
    formatter = logging.Formatter(fmt)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_file = f"{LOGS_FILE}{SUFFIX_TIMESTAMP}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
