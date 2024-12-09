import pyautogui
import logging
import time

logger = logging.getLogger("main")

def find_and_click(image_path, timeout=30, region=None):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8, region=(
                region['left'],
                region['top'],
                region['width'],
                region['height']
            ) if region else None)
            if location:
                pyautogui.click(location)
                logger.info(f"Clicked '{image_path}' at {location}.")
                return True
        except Exception as e:
            logger.error(f"Error finding '{image_path}': {e}")
        time.sleep(2)
    logger.warning(f"Could not find '{image_path}' within {timeout} seconds.")
    return False

def wait_for_image_to_appear(image_path, timeout=30, region=None):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8, region=(
                region['left'],
                region['top'],
                region['width'],
                region['height']
            ) if region else None)
            if location:
                logger.info(f"'{image_path}' appeared at {location}.")
                return True
        except Exception as e:
            logger.error(f"Error finding '{image_path}': {e}")
        time.sleep(2)
    logger.warning(f"'{image_path}' did not appear within {timeout} seconds.")
    return False

def wait_for_image_to_disappear(image_path, timeout=30, region=None):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8, region=(
                region['left'],
                region['top'],
                region['width'],
                region['height']
            ) if region else None)
            if not location:
                logger.info(f"'{image_path}' disappeared.")
                return True
        except Exception as e:
            logger.error(f"Error checking disappearance of '{image_path}': {e}")
        time.sleep(2)
    logger.warning(f"'{image_path}' did not disappear within {timeout} seconds.")
    return False