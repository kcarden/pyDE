import tkinter as tk
from tkinter import ttk
import os
import explorer
import editor
import wysiwyg

class PyDE(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("pyDE - Python Modular IDE")
        self.geometry("1200x800")  # Default window size
        self.create_gui()

    def create_gui(self):
        self.columnconfigure(0, weight=0)  # Left column (explorer) - Static width
        self.columnconfigure(1, weight=1)  # Middle column (editor) - Resizable
        self.columnconfigure(2, weight=1)  # Right column (wysiwyg) - Resizable
        self.rowconfigure(0, weight=1)  # Extend row to the bottom of the window

        # Initialize the panels
        self.explorer_panel = explorer.ExplorerPanel(self)
        self.editor_panel = editor.EditorPanel(self)
        self.wysiwyg_panel = wysiwyg.WYSIWYGPanel(self)

        # Add the panels to the main window
        self.explorer_panel.grid(row=0, column=0, sticky="ns")  # Static width (not resizable)
        self.editor_panel.grid(row=0, column=1, sticky="nsew")
        self.wysiwyg_panel.grid(row=0, column=2, sticky="nsew")

        # Add padding to the bottom of the window
        self.configure(padx=10, pady=10)

if __name__ == "__main__":
    app = PyDE()
    app.mainloop()
