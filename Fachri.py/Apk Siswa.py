import PySimpleGUI as sg

# Layout aplikasi
layout = [
    [sg.Text("DATA SISWA BARU", size=(30, 1), justification="center", font=("Helvetica", 18), text_color="black", background_color="lightblue")],
    [sg.Text("Nama Lengkap", size=(20, 1)), sg.Input(key="-NAMA-", size=(30, 1))],
    [sg.Text("Tanggal Lahir", size=(20, 1)), sg.Input(key="-TANGGAL_LAHIR-", size=(30, 1))],
    [sg.Text("Asal Sekolah", size=(20, 1)), sg.Input(key="-ASAL_SEKOLAH-", size=(30, 1))],
    [sg.Text("NISN", size=(20, 1)), sg.Input(key="-NISN-", size=(30, 1))],
    [sg.Text("Nama Ayah", size=(20, 1)), sg.Input(key="-NAMA_AYAH-", size=(30, 1))],
    [sg.Text("Nama Ibu", size=(20, 1)), sg.Input(key="-NAMA_IBU-", size=(30, 1))],
    [sg.Text("Nomor Telepon / HP", size=(20, 1)), sg.Input(key="-NO_HP-", size=(30, 1))],
    [sg.Text("Alamat", size=(20, 1)), sg.Multiline(key="-ALAMAT-", size=(30, 5))],
    [sg.Button("Hapus", button_color=("white", "orange")), sg.Button("Simpan", button_color=("white", "green"))],
]

# Membuat jendela
window = sg.Window("Form Data Siswa Baru", layout, background_color="lightblue")

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "Hapus":
        for key in values:
            window[key].update("")
    if event == "Simpan":
        sg.popup("Data Berhasil Disimpan!", "Berikut data yang disimpan:", values)

window.close()