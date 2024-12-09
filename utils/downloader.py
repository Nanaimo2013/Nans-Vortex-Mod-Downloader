import pyautogui
import logging
from utils.image_handler import find_and_click, wait_for_image_to_appear, wait_for_image_to_disappear

logger = logging.getLogger("main")

class ModDownloader:
    def __init__(self, regions=None):
        self.download_region = regions.get("download") if regions else None
        self.slow_download_region = regions.get("slow_download") if regions else None
        self.vortex_button = "assets/download_button.png"
        self.slow_button = "assets/slow_download_button.png"

    def process_mod(self):
        # Use download_region for the main download button
        if not find_and_click(self.vortex_button, region=self.download_region):
            logger.error("Could not find Vortex 'Download' button.")
            return False

        # Use slow_download_region for the slow download button
        if not find_and_click(self.slow_button, timeout=120, region=self.slow_download_region):
            logger.warning("Could not find 'Slow Download' button. Skipping mod.")
            return False

        # Wait for the download to complete
        if not wait_for_image_to_disappear(self.vortex_button, timeout=300, region=self.download_region):
            logger.error("'Download' button did not disappear in time.")
            return False

        if not wait_for_image_to_appear(self.vortex_button, region=self.download_region):
            logger.error("Could not find 'Download' button for the next mod.")
            return False

        logger.info("Mod processed successfully.")
        return True
