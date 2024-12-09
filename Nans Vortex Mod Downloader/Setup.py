import json
import logging
import os
from utils.logger import setup_logger
from utils.region_selector import RegionSelectorGUI

logger = setup_logger("setup")

def main():
    logger.info("=== Setting Up Configuration ===")
    
    # Define the regions to be selected
    regions_to_select = ["Download Button", "Slow Download Button"]
    
    # Initialize the Region Selector GUI
    selector_gui = RegionSelectorGUI(regions_to_select)
    selected_regions = selector_gui.run()
    
    if not selected_regions:
        logger.critical("No regions were selected. Exiting setup.")
        exit(1)
    
    # Save configuration to config.json only after confirmation
    with open("config.json", "w") as config_file:
        json.dump({"regions": selected_regions}, config_file, indent=4)
    
    logger.info("Configuration saved successfully.")
    logger.info("Setup completed successfully.")

if __name__ == "__main__":
    main()