import PySimpleGUI as sg

# Konstanta biaya per jam
BIAYA_PER_JAM = 2000

# Layout aplikasi
layout = [
    [sg.Text("Aplikasi Parkir Kelompok 6", font=("Helvetica", 16), justification="center")],
    [sg.Text("Cari NoPol"), sg.Input(key="-CARI_NOPOL-", size=(20, 1)), sg.Button("Cari", key="-CARI-")],
    [sg.Text("No Plat Polisi"), sg.Input(key="-NOPOL-", size=(20, 1))],
    [sg.Text("Waktu Masuk (HH:MM)"), sg.Input(key="-MASUK-", size=(20, 1))],
    [sg.Text("Waktu Keluar (HH:MM)"), sg.Input(key="-KELUAR-", size=(20, 1))],
    [sg.Text("Biaya"), sg.Input("0", key="-BIAYA-", size=(20, 1), readonly=True), sg.Button("Hitung", key="-HITUNG-")],
    [sg.Text("Biaya Per Jam", font=("Helvetica", 14)), sg.Text(f"Rp. {BIAYA_PER_JAM:,}", font=("Helvetica", 14), text_color="red")],
    [sg.Text("List Pelanggan Urut Terakhir Keluar", font=("Helvetica", 10))],
    [sg.Table(values=[], headings=["No Plat Polisi", "Masuk", "Keluar", "Biaya"], key="-TABEL1-", size=(50, 5))],
    [sg.Text("List Pelanggan Banyak Bayar", font=("Helvetica", 10))],
    [sg.Table(values=[], headings=["No Plat Polisi", "Masuk", "Keluar", "Biaya"], key="-TABEL2-", size=(50, 5))],
]

# Membuat jendela
window = sg.Window("Aplikasi Parkir", layout)

# Data pelanggan
data_terakhir_keluar = []
data_banyak_bayar = []

# Fungsi menghitung biaya
def hitung_biaya(waktu_masuk, waktu_keluar):
    try:
        # Konversi waktu ke jam dan menit
        jam_masuk, menit_masuk = map(int, waktu_masuk.split(":"))
        jam_keluar, menit_keluar = map(int, waktu_keluar.split(":"))
        # Hitung total waktu dalam menit
        total_masuk = jam_masuk * 60 + menit_masuk
        total_keluar = jam_keluar * 60 + menit_keluar
        durasi_menit = total_keluar - total_masuk
        durasi_jam = max(1, (durasi_menit + 59) // 60)  # Pembulatan ke atas
        return durasi_jam * BIAYA_PER_JAM
    except Exception as e:
        sg.popup_error("Format waktu tidak valid. Gunakan HH:MM.")
        return 0

# Loop event
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "-HITUNG-":
        nopol = values["-NOPOL-"]
        waktu_masuk = values["-MASUK-"]
        waktu_keluar = values["-KELUAR-"]
        biaya = hitung_biaya(waktu_masuk, waktu_keluar)
        window["-BIAYA-"].update(biaya)

        # Tambahkan ke tabel data pelanggan terakhir keluar
        if nopol and biaya > 0:
            data_terakhir_keluar.append([nopol, waktu_masuk, waktu_keluar, biaya])
            data_terakhir_keluar = sorted(data_terakhir_keluar, key=lambda x: x[2], reverse=True)
            window["-TABEL1-"].update(values=data_terakhir_keluar)

            # Update data banyak bayar
            data_banyak_bayar.append([nopol, waktu_masuk, waktu_keluar, biaya])
            data_banyak_bayar = sorted(data_banyak_bayar, key=lambda x: x[3], reverse=True)
            window["-TABEL2-"].update(values=data_banyak_bayar)

window.close()