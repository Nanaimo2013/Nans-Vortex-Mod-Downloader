# Nans Vortex Mod Downloader

[![Latest Release](https://img.shields.io/github/v/release/Nanaimo2013/Nans-Vortex-Mod-Downloader?style=for-the-badge&color=blue&label=Latest%20Release)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/releases)
[![Version](https://img.shields.io/github/v/tag/Nanaimo2013/Nans-Vortex-Mod-Downloader?label=Version&style=for-the-badge&color=orange)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/releases/latest)
[![GitHub license](https://img.shields.io/github/license/Nanaimo2013/Nans-Vortex-Mod-Downloader?style=for-the-badge&color=blue)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Nanaimo2013/Nans-Vortex-Mod-Downloader?style=for-the-badge&color=red)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/issues)
[![GitHub stars](https://img.shields.io/github/stars/Nanaimo2013/Nans-Vortex-Mod-Downloader?style=for-the-badge&color=yellow)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/stargazers)
[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/Nanaimo2013/Nans-Vortex-Mod-Downloader/total?style=for-the-badge&color=blue)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/releases)
[![Contributors](https://img.shields.io/github/contributors/Nanaimo2013/Nans-Vortex-Mod-Downloader?style=for-the-badge&color=orange)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/graphs/contributors)
[![Code Size](https://img.shields.io/github/languages/code-size/Nanaimo2013/Nans-Vortex-Mod-Downloader?style=for-the-badge&color=blue)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen?style=for-the-badge&logo=github)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader)
[![Maintained](https://img.shields.io/maintenance/yes/2024?style=for-the-badge&color=green)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Nanaimo2013/Nans-Vortex-Mod-Downloader/ci.yml?style=for-the-badge&color=brightgreen)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/actions)
[![Forks](https://img.shields.io/github/forks/Nanaimo2013/Nans-Vortex-Mod-Downloader?style=for-the-badge&color=lightgray)](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/network/members)

## Overview

**Nans Vortex Mod Downloader** is an automated tool developed by **NansStudios** to streamline the process of downloading mods using Vortex. It leverages `pyautogui` for GUI automation, allowing users to specify screen regions by selecting and dragging boxes on your screen for efficient image recognition. This tool is currently optimized for **Windows** environments.

## Features

- **Automated Downloading**: Processes multiple mods sequentially with ease.
- **Customizable Regions**: Select and drag boxes on your screen to define specific areas for image searching, enhancing speed and accuracy.
- **Logging**: Comprehensive logs with color-coded outputs for easy monitoring.
- **Windows Support**: Optimized to work seamlessly on Windows operating systems.

## Requirements

- **Operating System**: Windows 10 or higher
- **Python**: 3.7 or higher
- **Libraries**:
  - [pyautogui](https://pyautogui.readthedocs.io/)
  - [colorama](https://pypi.org/project/colorama/)
  - [Pillow](https://pypi.org/project/Pillow/)
  - [tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)

Refer to `requirements.txt` for the complete list of dependencies.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader.git
    cd Nans-Vortex-Mod-Downloader
    ```

2. **Install Dependencies**

    Ensure you have `pip` installed. Then run:

    ```bash
    pip install -r requirements.txt
    ```

## Setup

Before running the downloader, you need to configure the screen regions where the "Download" and "Slow Download" buttons appear by selecting and dragging boxes on your screen.

1. **Run Setup Script**

    ```bash
    python Setup.py
    ```

2. **Select and Review Regions**

    The setup script will launch a user-friendly GUI where you can:

    - **Select Regions**: Click the **Select Region** button to choose the area for either the "Download" or "Slow Download" button by dragging a box on your screen.
    - **Review Selections**: The current selections for each button are displayed at the top of the setup window. You can see the coordinates and dimensions of each selected region.
    - **Redo Selections**: If a region is incorrect, you can select it again by clicking the **Select Region** button for that specific button.
    - **Confirm Selections**: Once all regions are correctly selected, click the **Confirm Selections** button at the top-right corner to save your configurations.

    **Tip**: Ensure that the selected regions accurately encompass the respective buttons to improve detection accuracy.

3. **Verify `config.json`**

    After setup and confirmation, your `config.json` will be automatically updated with the selected regions. It will look similar to:

    ```json:Nans Vortex Mod Downloader/config.json
    {
        "regions": {
            "download": {
                "left": 784,
                "top": 220,
                "width": 486,
                "height": 344
            },
            "slow_download": {
                "left": 771,
                "top": 189,
                "width": 589,
                "height": 365
            }
        }
    }
    ```

## Usage

1. **Start the Downloader**

    ```bash
    python Main.py
    ```

2. **Monitor Logs**

    The script will log its actions in the console with colored messages indicating the status of each operation.

## Customization

- **Adjusting the Number of Mods**

    In `Main.py`, you can adjust the range in the for-loop to process more or fewer mods:

    ```python
    for mod_number in range(240):  # Adjust the number as needed
    ```

- **Changing Confidence Level**

    The image search confidence is set to `0.8` by default. You can adjust this in `image_handler.py` if needed:

    ```python
    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8, region=region)
    ```

## Troubleshooting

- **Images Not Found**

    - Ensure that the screenshots (`download_button.png`, `slow_download_button.png`) are clear and match the on-screen buttons.
    - Verify that the regions specified in `config.json` correctly encompass the buttons.
    - Increase the `confidence` level if necessary.

- **Permission Issues**

    - On some operating systems, you might need to grant accessibility permissions to Python or your terminal.

- **Windows-Specific Issues**

    - Ensure that all dependencies are installed correctly.
    - Run the terminal or command prompt with administrative privileges if you encounter permission errors.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

    Click the [Fork](https://github.com/Nanaimo2013/Nans-Vortex-Mod-Downloader/fork) button at the top right of the repository page.

2. **Create a New Branch**

    ```bash
    git checkout -b feature/YourFeatureName
    ```

3. **Commit Your Changes**

    ```bash
    git commit -m "Add some feature"
    ```

4. **Push to the Branch**

    ```bash
    git push origin feature/YourFeatureName
    ```

5. **Open a Pull Request**

    Navigate to the original repository and click the "Compare & pull request" button.

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Colorama](https://pypi.org/project/colorama/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Developed and maintained by Nans Studio.
- Thanks to all the contributors and users who support this project.

## Contact

For any questions or suggestions, feel free to reach out:

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github)](https://github.com/Nanaimo2013)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Nanaimo_2013)

---

*Nans Vortex Mod Downloader - Streamlining your modding experience.*
