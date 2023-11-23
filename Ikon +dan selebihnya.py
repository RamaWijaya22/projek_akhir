import tkinter as tk
from tkinter import filedialog, messagebox
import os
import datetime

class BudgeBuddy:
    def __init__(self, master):
        self.master = master
        self.master.title("BudgeBuddy")

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Transaksi Baru", command=self.new_transaction)
        self.file_menu.add_command(label="Folder Baru", command=self.new_folder)

        self.title = tk.Label(self.master, text="BudgeBuddy")
        self.title.pack()

        self.create_widgets()

    def create_widgets(self):
        self.date_entry = tk.Entry(self.master)
        self.date_entry.pack()

        self.time_entry = tk.Entry(self.master)
        self.time_entry.pack()

        self.category_var = tk.StringVar()
        self.category_var.set("Choose Category")
        self.category_menu = tk.OptionMenu(self.master, self.category_var, "Income", "Expense")
        self.category_menu.pack()

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack()

        self.save_button = tk.Button(self.master, text="Save", command=self.save_transaction)
        self.save_button.pack()

    def new_transaction(self):
        workbook = xlsxwriter.Workbook(self.workbook_path)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Date')
        worksheet.write('B1', 'Time')
        worksheet.write('C1', 'Category')
        worksheet.write('D1', 'Amount')
        workbook.close()

    def new_folder(self):
        os.makedirs(self.folder_path)

    def save_transaction(self):
        if not self.date_entry.get() or not self.time_entry.get() or not self.amount_entry.get():
            messagebox.showerror("Error", "Please fill in all the fields")
            return

        date = self.date_entry.get()
        time = self.time_entry.get()
        category = self.category_var.get()
        amount = self.amount_entry.get()

        workbook = xlsxwriter.Workbook(self.workbook_path)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Date')
        worksheet.write('B1', 'Time')
        worksheet.write('C1', 'Category')
        worksheet.write('D1', 'Amount')
        worksheet.write(f'A{int(datetime.datetime.now().strftime("%S")) + 2}', date)
        worksheet.write(f'B{int(datetime.datetime.now().strftime("%S")) + 2}', time)
        worksheet.write(f'C{int(datetime.datetime.now().strftime("%S")) + 2}', category)
        worksheet.write(f'D{int(datetime.datetime.now().strftime("%S")) + 2}', amount)
        workbook.close()

        messagebox.showinfo("Success", f"Transaction has been saved\n\nDate: {date}\nTime: {time}\nCategory: {category}\nAmount: {amount}")

if __name__ == "__main__":
    folder_path = "transactions"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    workbook_path =