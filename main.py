import tkinter as tk
from tkinter import ttk
import os
import explorer
import editor
import wysiwyg

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WYSIWYG Markdown Editor")
        self.geometry("1200x800")  # Default window size
        self.create_gui()

    def create_gui(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Initialize the panels
        self.explorer_panel = explorer.ExplorerPanel(self)
        self.editor_panel = editor.EditorPanel(self)
        self.wysiwyg_panel = wysiwyg.WYSIWYGPanel(self)

        # Add the panels to the main window
        self.explorer_panel.grid(row=0, column=0, sticky="nsew")
        self.editor_panel.grid(row=0, column=1, sticky="nsew")
        self.wysiwyg_panel.grid(row=0, column=2, sticky="nsew")

        # Make the columns resizable
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
