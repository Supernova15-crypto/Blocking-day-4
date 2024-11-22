import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Inisialisasi
window = tk.Tk()  # Membuat objek window berisi window Tk()
window.configure(bg="white")  # Mengubah background window menjadi putih
window.geometry("300x200")  # Mengubah size window dalam satuan pixel
window.resizable(False, False)  # Window tidak bisa di-resize
window.title("Sapa")  # Mengubah title window

# Variabel
NAMA_DEPAN = tk.StringVar()  # Membuat constant
NAMA_BELAKANG = tk.StringVar()  # Membuat constant

# Fungsi
def tombol_click():
    pesan = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Have nice day!"
    showinfo(title="Hi", message=pesan)

# Frame input
input_frame = ttk.Frame(window)  # Menggunakan widget ttk untuk memakai frame yang akan berisi window
input_frame.pack(padx=10, pady=10, fill="x", expand=True)  # Membuat layout dengan pack

# Komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)

# 2. Entry nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)

# 4. Entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Tombol
tombol = ttk.Button(input_frame, text="Sapa!", command=tombol_click)
tombol.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()  # Metode mainloop menjalankan program hingga app close