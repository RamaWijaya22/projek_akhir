import tkinter as tk
from tkinter import ttk

def add_transaction():
    # Fungsi untuk menambahkan transaksi ke dalam aplikasi
    tanggal = tanggal_entry.get()
    opsi = opsi_var.get()
    kategori = kategori_entry.get()
    jumlah = jumlah_entry.get()

    # Validasi input (Anda mungkin ingin menambahkan validasi lebih lanjut)
    if not tanggal or not opsi or not kategori or not jumlah:
        result_label.config(text="Mohon isi semua field.")
        return

    # Tambahkan data transaksi ke dalam listbox
    transaksi_listbox.insert(tk.END, f"{tanggal} - {opsi} - {kategori} - {jumlah}")

    # Hitung jumlah keseluruhan pemasukkan, pengeluaran, dan saldo
    if opsi == "Pemasukan":
        total_pemasukan_var.set(total_pemasukan_var.get() + float(jumlah))
    elif opsi == "Pengeluaran":
        total_pengeluaran_var.set(total_pengeluaran_var.get() + float(jumlah))

    total_saldo_var.set(total_pemasukan_var.get() - total_pengeluaran_var.get())

    # Bersihkan input setelah menambahkan transaksi
    tanggal_entry.delete(0, tk.END)
    opsi_var.set("Pemasukan")  # Setel opsi ke default "Pemasukan"
    kategori_entry.delete(0, tk.END)
    jumlah_entry.delete(0, tk.END)

    result_label.config(text="Transaksi berhasil ditambahkan.")

# Inisialisasi aplikasi Tkinter
root = tk.Tk()
root.title("BudgeBuddy App")

def main_page():
    frame = tk.Frame(root, width=1440, height=1011, bg="white")
    frame.pack_propagate(False)
    frame.pack(fill=tk.BOTH, expand=True)

    title_label = tk.Label(frame, text="BudgeBuddy", font=("Inter", 28, "bold"), fg="white", pady=20, bg="#001F3F")
    title_label.place(x=175, y=34)

    blue_area = tk.Frame(frame, width=1440, height=268, bg="#001F3F")
    blue_area.place(x=0, y=0)

    gray_area = tk.Frame(frame, width=1440, height=110, bg="#E1E1E1")
    gray_area.place(x=0, y=268)

    white_area = tk.Frame(frame, width=1440, height=1011, bg="white")
    white_area.place(x=0, y=378)

    # Input tanggal
    tanggal_label = tk.Label(frame, text="Tanggal:", font=("Inter", 12), fg="#2A2656", bg="white")
    tanggal_label.place(x=175, y=400)
    tanggal_entry = tk.Entry(frame, font=("Inter", 12), fg="black")
    tanggal_entry.place(x=275, y=400)

    # Pilihan opsi (Pemasukan atau Pengeluaran)
    opsi_label = tk.Label(frame, text="Opsi:", font=("Inter", 12), fg="#2A2656", bg="white")
    opsi_label.place(x=175, y=430)
    opsi_var = tk.StringVar()
    opsi_var.set("Pemasukan")
    opsi_combobox = ttk.Combobox(frame, textvariable=opsi_var, values=["Pemasukan", "Pengeluaran"])
    opsi_combobox.place(x=275, y=430)

    # Input kategori
    kategori_label = tk.Label(frame, text="Kategori:", font=("Inter", 12), fg="#2A2656", bg="white")
    kategori_label.place(x=175, y=460)
    kategori_entry = tk.Entry(frame, font=("Inter", 12), fg="black")
    kategori_entry.place(x=275, y=460)

    # Input jumlah
    jumlah_label = tk.Label(frame, text="Jumlah:", font=("Inter", 12), fg="#2A2656", bg="white")
    jumlah_label.place(x=175, y=490)
    jumlah_entry = tk.Entry(frame, font=("Inter", 12), fg="black")
    jumlah_entry.place(x=275, y=490)

    # Tombol Tambahkan
    tambahkan_button = tk.Button(frame, text="Tambahkan", command=add_transaction)
    tambahkan_button.place(x=275, y=530)

    # Label untuk menampilkan hasil atau pesan kesalahan
    global result_label
    result_label = tk.Label(frame, text="", font=("Inter", 14), fg="red", bg="white")
    result_label.place(x=275, y=560)

    # Listbox untuk menampilkan daftar transaksi
    global transaksi_listbox
    transaksi_listbox = tk.Listbox(frame, font=("Inter", 12), selectbackground="#2A2656", selectforeground="white", height=5)
    transaksi_listbox.place(x=600, y=400)

    # Label untuk menampilkan jumlah keseluruhan pemasukkan, pengeluaran, dan saldo
    total_pemasukan_label = tk.Label(frame, text="Total Pemasukan:", font=("Inter", 12), fg="#2A2656", bg="white")
    total_pemasukan_label.place(x=600, y=600)
    global total_pemasukan_var
    total_pemasukan_var = tk.DoubleVar()
    total_pemasukan_var.set(0.0)
    total_pemasukan_value = tk.Label(frame, textvariable=total_pemasukan_var, font=("Inter", 12), fg="black", bg="white")
    total_pemasukan_value.place(x=750, y=600)

    total_pengeluaran_label = tk.Label(frame, text="Total Pengeluaran:", font=("Inter", 12), fg="#2A2656", bg="white")
    total_pengeluaran_label.place(x=600, y=630)
    global total_pengeluaran_var
    total_pengeluaran_var = tk.DoubleVar()
    total_pengeluaran_var.set(0.0)
    total_pengeluaran_value = tk.Label(frame, textvariable=total_pengeluaran_var, font=("Inter", 12), fg="black", bg="white")
    total_pengeluaran_value.place(x=750, y=630)

    total_saldo_label = tk.Label(frame, text="Total Saldo:", font=("Inter", 12), fg="#2A2656", bg="white")
    total_saldo_label.place(x=600, y=660)
    global total_saldo_var
    total_saldo_var = tk.DoubleVar()
    total_saldo_var.set(0.0)
    total_saldo_value = tk.Label(frame, textvariable=total_saldo_var, font=("Inter", 12), fg="black", bg="white")
    total_saldo_value.place(x=750, y=660)

# Jalankan fungsi untuk menampilkan halaman utama saat membuka aplikasi
main_page()

# Jalankan loop utama
root.mainloop()