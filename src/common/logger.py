import logging
import os
import datetime

LOGDIR = "logs"
os.makedirs(LOGDIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOGDIR, f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
