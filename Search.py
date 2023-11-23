import tkinter as tk
from tkinter import filedialog as fd
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.title("Lembar Kerja")
        self.geometry("300x200")

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(self, textvariable=self.search_var)
        search_entry.pack()

        search_button = tk.Button(self, text="Cari File", command=self.search_files)
        search_button.pack()

    def search_files(self):
        search_string = self.search_var.get()
        files = []
        for root, dirs, filenames in os.walk('.'):
            for filename in filenames:
                if filename.startswith(search_string):
                    files.append(os.path.join(root, filename))
        
        files.sort()
        
        if files:
            fd.messagebox.showinfo("File Ditemukan", f"File yang sudah dibuat:\n\n{files}")
        else:
            fd.messagebox.showinfo("File Tidak Ditemukan", "Tidak ada file yang sudah dibuat.")

app = Application()
app.mainloop()