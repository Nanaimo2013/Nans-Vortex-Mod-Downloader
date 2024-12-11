import logging
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define color codes for different log levels
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Fore.WHITE)
        message = super().format(record)
        return f"{log_color}{message}{Style.RESET_ALL}"

# Set up logging
def setup_logger(name):
    """Set up a logger with colorized output."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = ColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    return logger

# Define error codes
error_codes = {
    404: "Download button not found.",
    405: "Slow download button not found.",
    408: "Download button did not disappear in time.",
    409: "Failed to click on the download button.",
    410: "Error while waiting for image to appear.",
    411: "Error while waiting for image to disappear.",
    412: "Configuration file not found.",
    413: "Invalid configuration settings.",
    414: "Image recognition failed.",
    415: "Unexpected error occurred.",
    416: "Network connection failed.",
    417: "Timeout while waiting for response.",
    418: "Image not matching expected pattern.",
    419: "User cancelled the operation.",
    420: "Insufficient permissions to access resources.",
    421: "File not found in the specified path.",
    422: "Error reading from the configuration file.",
    423: "Error writing to the log file.",
    424: "Image processing error.",
    425: "Invalid region specified.",
    426: "Failed to initialize GUI.",
    427: "Threading error occurred.",
    428: "Unexpected response from the server.",
    429: "Failed to load required libraries.",
    430: "Error during setup process.",
    431: "Invalid input provided by the user.",
    432: "Error during cleanup process.",
    433: "Failed to save user settings.",
    434: "Error during image capture.",
    435: "Failed to start the application.",
    436: "Error during mod processing.",
    437: "Failed to retrieve mod information.",
    438: "Error during logging setup.",
    439: "Failed to update application.",
    440: "Error during dependency installation.",
    441: "Debugging information logged.",
    442: "Critical failure in the application.",
    443: "Invalid operation attempted.",
    444: "Resource not available."
}

def log_error(code):
    """Log an error with the corresponding error code."""
    message = error_codes.get(code, "Unknown error code.")
    logger = logging.getLogger("main")
    logger.error(f"{code}: {message}")
