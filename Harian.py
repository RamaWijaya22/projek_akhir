import tkinter as tk
from tkinter import messagebox
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.title("Lembar Kerja")
        self.geometry("300x200")

        self.date_var = tk.StringVar()
        self.income_var = tk.StringVar()
        self.expense_var = tk.StringVar()
        self.balance_var = tk.StringVar()

        date_label = tk.Label(self, text="Tanggal")
        date_label.pack()
        date_entry = tk.Entry(self, textvariable=self.date_var)
        date_entry.pack()

        income_label = tk.Label(self, text="Pemasukkan")
        income_label.pack()
        income_entry = tk.Entry(self, textvariable=self.income_var)
        income_entry.pack()

        expense_label = tk.Label(self, text="Pengeluaran")
        expense_label.pack()
        expense_entry = tk.Entry(self, textvariable=self.expense_var)
        expense_entry.pack()

        balance_label = tk.Label(self, text="Saldo")
        balance_label.pack()
        balance_entry = tk.Entry(self, textvariable=self.balance_var)
        balance_entry.pack()

        show_balance_button = tk.Button(self, text="Tampilkan Saldo", command=self.show_balance)
        show_balance_button.pack()

    def show_balance(self):
        date = self.date_var.get()
        income = int(self.income_var.get())
        expense = int(self.expense_var.get())

        if not os.path.exists(date):
            messagebox.showerror("Error", "Tanggal tidak valid atau data untuk tanggal tersebut tidak ada.")
            return

        with open(date, "r") as f:
            data = f.read().split("\n")
            for line in data:
                income_date, income_value, expense_value = line.split(",")
                if income_date == date:
                    balance = int(income_value) - int(expense_value)
                    self.balance_var.set(str(balance))
                    return

        messagebox.showerror("Error", "Tanggal tidak valid atau data untuk tanggal tersebut tidak ada.")

app = Application()
app.mainloop()