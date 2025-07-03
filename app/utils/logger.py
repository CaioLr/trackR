import logging
import sys

def setup_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s [%(name)s] [%(asctime)s]: %(message)s',
        handlers=[
            logging.FileHandler(filename="file.log", mode='w',encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ]
    )