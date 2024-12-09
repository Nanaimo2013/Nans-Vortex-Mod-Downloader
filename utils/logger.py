import logging
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class ColorLogFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA,
    }
    RESET = Style.RESET_ALL

    def format(self, record):
        color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f"{color}{message}{self.RESET}"

def setup_logger(name):
    """Set up a logger with colorized output."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(ColorLogFormatter("%(asctime)s [%(levelname)s] %(message)s"))
    if not logger.handlers:
        logger.addHandler(handler)
    return logger