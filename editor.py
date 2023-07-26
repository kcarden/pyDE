import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import filedialog
import os

class EditorPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.text_editor = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Courier New", 12))
        self.text_editor.pack(fill=tk.BOTH, expand=True)
        self.setup_menu()

    def setup_menu(self):
        menubar = tk.Menu(self)
        self.parent.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        menubar.add_cascade(label="File", menu=file_menu)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, file.read())
            self.parent.title(f"WYSIWYG Markdown Editor - {os.path.basename(file_path)}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Markdown Files", "*.md"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_editor.get(1.0, tk.END))
            self.parent.title(f"WYSIWYG Markdown Editor - {os.path.basename(file_path)}")

    def save_file_as(self):
        self.save_file()

if __name__ == "__main__":
    root = tk.Tk()
    editor_panel = EditorPanel(root)
    editor_panel.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
