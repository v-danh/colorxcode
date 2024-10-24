import logging
from logging import Logger
from colorama import init, Fore

init(autoreset=True)

SUCCESS_COLOR = Fore.GREEN
INFO_COLOR    = Fore.CYAN
WARNING_COLOR = Fore.YELLOW
ERROR_COLOR   = Fore.RED
RESET         = Fore.RESET

LOG_FMT = '(%(filename)s:%(lineno)d) | <%(levelname)s> %(message)s'
# DATE_FMT = '%d/%m/%Y %H:%M:%S'

class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Center the levelname to 9 characters
        record.levelname = f"{record.levelname.center(6)}"
        return super().format(record)

def setup_logging() -> Logger:
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter(LOG_FMT))

    logger = logging.getLogger("ColorLib")
    logger.setLevel(logging.DEBUG)  # hoặc logging.INFO tùy vào mức bạn muốn
    logger.propagate = False
    logger.addHandler(handler)

    return logger