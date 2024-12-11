import pyautogui
import logging
from utils.image_handler import find_and_click, wait_for_image_to_appear, wait_for_image_to_disappear
import time
import threading
import sys
from utils.logger import log_error

logger = logging.getLogger("main")

stop_loading = False  # Global variable to control the loading indicator

def loading_indicator():
    """Display a loading indicator in the console."""
    while not stop_loading:
        for status in ["Loading...", "Waiting...", "Still waiting..."]:
            sys.stdout.write(f'\r{status}   ')  # Overwrite the same line
            sys.stdout.flush()
            time.sleep(1)  # Update every second

def loading_indicator():
    """Display a loading indicator in the console."""
    while not stop_loading:
        for status in ["Loading...", "Waiting...", "Still waiting..."]:
            sys.stdout.write(f'\r{status}   ')  # Overwrite the same line
            sys.stdout.flush()
            time.sleep(1)  # Update every second

class ModDownloader:
    def __init__(self, regions=None):
        self.download_region = regions.get("Download Button") if regions else None
        self.vortex_button = "assets/download_button.png"

    def process_mod(self):
        global stop_loading
        stop_loading = False
        loader_thread = threading.Thread(target=loading_indicator)
        loader_thread.start()

        logger.info("Starting to process mod...")
        error_count = 0  # Count the number of errors encountered
        for attempt in range(3):  # Retry mechanism for finding the download button
            if find_and_click(self.vortex_button, region=self.download_region):
                logger.info("Found 'Download' button, proceeding to click...")
                break
            else:
                error_count += 1  # Increment error count
                if error_count == 1:  # Log only the first error
                    logger.error(f"Error finding '{self.vortex_button}': Attempt {attempt + 1}")
                elif error_count == 3:  # Log a summary after all attempts
                    logger.error(f"Failed to find '{self.vortex_button}' after {attempt + 1} attempts.")
                time.sleep(1)  # Wait before retrying
        else:
            stop_loading = True
            loader_thread.join()
            return False

        stop_loading = True
        loader_thread.join()
        logger.info("Waiting for the download to complete...")
        if not wait_for_image_to_disappear(self.vortex_button, timeout=300, region=self.download_region):
            logger.error(f"Download button did not disappear in time after {error_count} attempts.")
            return False

        for attempt in range(3):
            logger.info(f"Attempting to find 'Download' button again... (Attempt {attempt + 1})")
            if wait_for_image_to_appear(self.vortex_button, region=self.download_region):
                logger.info("Download button reappeared for the next mod.")
                return True
            time.sleep(1)

        logger.error(f"Could not find 'Download' button for the next mod after {error_count} attempts.")
        return False
