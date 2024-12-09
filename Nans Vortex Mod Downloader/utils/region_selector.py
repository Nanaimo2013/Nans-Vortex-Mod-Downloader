import tkinter as tk
from tkinter import ttk, messagebox
import logging
import json

logger = logging.getLogger("setup")

class RegionSelectorGUI:
    def __init__(self, regions):
        self.regions = regions
        self.selected_regions = {}
        
        self.root = tk.Tk()
        self.root.title("Nans Vortex Mod Downloader - Region Selector")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        selection_frame = ttk.LabelFrame(self.root, text="Select Regions")
        selection_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.selection_labels = {}
        self.coordinate_labels = {}
        
        for region in self.regions:
            # Create frame for each region
            region_frame = ttk.Frame(selection_frame)
            region_frame.pack(fill="x", padx=5, pady=5)

            # Button
            button = ttk.Button(region_frame, text=f"Select {region}", 
                              command=lambda r=region: self.select_region(r))
            button.pack(anchor="w", padx=5, pady=2)

            # Status Label
            self.selection_labels[region] = ttk.Label(region_frame, 
                                                    text=f"{region}: Not Selected")
            self.selection_labels[region].pack(anchor="w", padx=5, pady=2)

            # Coordinates Label
            self.selection_labels[region] = ttk.Label(region_frame, 
                                                     text="Coordinates: None")
            self.selection_labels[region].pack(anchor="w", padx=5, pady=2)

        # Confirm button at the bottom
        self.confirm_button = ttk.Button(self.root, text="Confirm Selections", 
                                       command=self.confirm_selections, 
                                       state="disabled")
        self.confirm_button.pack(pady=10)

    def save_to_config(self):
        """Save selections to config.json"""
        with open("config.json", "w") as config_file:
            json.dump({"regions": self.selected_regions}, config_file, indent=4)
        logger.info("Selections saved to config.json")

    def update_labels(self, region_name, coords):
        """Update GUI labels with selection information"""
        if region_name in self.selection_labels:
            self.selection_labels[region_name].config(
                text=f"Coordinates: left={coords['left']}, top={coords['top']}, "
                     f"width={coords['width']}, height={coords['height']}")

    def select_region(self, region_name):
        """Handle region selection"""
        selector = ScreenRegionSelector(self.root, region_name, self)
        selector.select_region()

    def check_all_selected(self):
        """Check if all regions are selected and enable confirm button"""
        if len(self.selected_regions) == len(self.regions):
            self.confirm_button.config(state="normal")
        else:
            self.confirm_button.config(state="disabled")

    def confirm_selections(self):
        """Handle confirmation of selections"""
        if len(self.selected_regions) != len(self.regions):
            messagebox.showerror("Error", "Please select all regions before confirming.")
            return
        self.save_to_config()
        self.root.quit()

    def run(self):
        self.root.mainloop()

class ScreenRegionSelector:
    def __init__(self, parent, region_name, gui):
        self.parent = parent
        self.region_name = region_name
        self.gui = gui
        self.selected_region = None
        self.start_x = None
        self.start_y = None
        self.rect = None

    def select_region(self):
        self.selection_window = tk.Toplevel(self.parent)
        self.selection_window.attributes("-fullscreen", True)
        self.selection_window.attributes("-alpha", 0.3)
        self.selection_window.attributes("-topmost", True)
        self.selection_window.config(cursor="cross")

        self.canvas = tk.Canvas(self.selection_window, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.selection_window.bind("<Escape>", self.cancel_selection)

        logger.info(f"Please select the region for '{self.region_name}' by clicking and dragging the mouse.")
        self.selection_window.mainloop()

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, 
            outline='red', width=2)

    def on_move_press(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        left = min(self.start_x, end_x)
        top = min(self.start_y, end_y)
        width = abs(end_x - self.start_x)
        height = abs(end_y - self.start_y)
        self.selected_region = {
            "left": int(left),
            "top": int(top),
            "width": int(width),
            "height": int(height)
        }
        logger.info(f"Region selected for '{self.region_name}': {self.selected_region}")
        self.gui.selected_regions[self.region_name] = self.selected_region
        self.gui.update_labels(self.region_name, self.selected_region)
        self.gui.check_all_selected()
        self.selection_window.destroy()

    def cancel_selection(self, event):
        logger.warning(f"Selection for '{self.region_name}' was cancelled.")
        self.selected_region = None
        self.selection_window.destroy()