import logging
import time
import json
from utils.downloader import ModDownloader
from utils.logger import setup_logger

# Set up logging
logger = setup_logger("main")

def load_config():
    """Load configuration settings."""
    try:
        with open("config.json", "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logger.critical("Config file not found! Run Setup.py first.")
        exit(1)

def main():
    logger.info("=== Starting Nans Vortex Mod Downloader ===")

    config = load_config()
    regions = config.get("regions", {})
    downloader = ModDownloader(regions=regions)

    for mod_number in range(240):  # Adjust for your needs
        logger.info(f"Processing mod {mod_number + 1}...")
        success = downloader.process_mod()
        if not success:
            logger.warning(f"Failed to process mod {mod_number + 1}. Skipping.")
        else:
            logger.info(f"Successfully processed mod {mod_number + 1}.")
        time.sleep(1)  # Optional: Add a short delay between mods

if __name__ == "__main__":
    main()
