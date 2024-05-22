import tkinter as tk
from tkinter import ttk
import json
import os

class GeigerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Geiger")
        
        # Set the data file path to be in the same directory as the script
        self.data_file = os.path.join(os.path.dirname(__file__), 'data.json')
        self.items = self.load_data()
        
        self.create_widgets()
        self.update_total()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        else:
            return {
                "Black Crystal": 0, "Black Stuff": 0, "Blue Crystal": 0, "Blue Stuff": 0, 
                "D Battery": 0, "Geiger Charger": 0, "Green Crystal": 0, "Green Stuff": 0, 
                "Nerd Hair": 0, "Nuclear Fuel": 0, "Orange Stuff": 0, "Purple Stuff": 0, 
                "Red Crystal": 0, "Red Stuff": 0, "Star Fuel": 0, "White Crystal": 0, 
                "White Stuff": 0, "Glowstick": 0, "Radioactive Chemical": 0, "": 0
            }
    
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.items, file)
    
    def create_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        row = 0
        for item, value in self.items.items():
            tk.Label(self.root, text=f"{item} =").grid(row=row, column=0, sticky=tk.W)
            tk.Label(self.root, textvariable=tk.StringVar(value=str(value))).grid(row=row, column=1)
            tk.Button(self.root, text="-", command=lambda i=item: self.update_value(i, -1)).grid(row=row, column=2)
            tk.Button(self.root, text="+", command=lambda i=item: self.update_value(i, 1)).grid(row=row, column=3)
            row += 1
        
        self.total_label = tk.Label(self.root, text="Total = 0")
        self.total_label.grid(row=row, columnspan=4, pady=10)
        
        self.dark_mode_var = tk.IntVar()
        self.dark_mode_check = tk.Checkbutton(self.root, text="Dark Mode", variable=self.dark_mode_var, command=self.toggle_dark_mode)
        self.dark_mode_check.grid(row=row+1, columnspan=4)
    
    def update_value(self, item, change):
        self.items[item] += change
        self.create_widgets()
        self.update_total()
    
    def update_total(self):
        total = sum(self.items.values())
        self.total_label.config(text=f"Total = {total}")
    
    def toggle_dark_mode(self):
        if self.dark_mode_var.get():
            self.root.config(bg="black")
            for widget in self.root.winfo_children():
                widget.config(bg="black", fg="white")
        else:
            self.root.config(bg="white")
            for widget in self.root.winfo_children():
                widget.config(bg="white", fg="black")
    
    def on_closing(self):
        self.save_data()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GeigerApp(root)
    root.mainloop()