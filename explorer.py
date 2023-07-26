import tkinter as tk
from tkinter import ttk
import os

class ExplorerPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.tree = ttk.Treeview(self)
        self.tree.heading("#0", text="File Explorer")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.load_initial_directory()

    def load_initial_directory(self):
        initial_dir = os.getcwd()
        self.load_directory(initial_dir)

    def load_directory(self, directory):
        self.tree.delete(*self.tree.get_children())
        self.parent.title(f"WYSIWYG Markdown Editor - {directory}")
        try:
            files = os.listdir(directory)
            for file in files:
                self.tree.insert("", "end", text=file, values=(os.path.join(directory, file)))
        except OSError:
            print(f"Error loading directory: {directory}")

if __name__ == "__main__":
    root = tk.Tk()
    explorer_panel = ExplorerPanel(root)
    explorer_panel.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
