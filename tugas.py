import  tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

uiApp = tk.Tk()
uiApp.configure(background='black')
uiApp.geometry("1000x1000")
uiApp.resizable()
uiApp.title("Prediksi Prodi Pilihan")

#make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10, fill="x", expand = True)

#make label
inputLabel = tk.Label(inputFrame, text="Nilai Tabel Siswa")
inputLabel.pack(padx=10, pady=10, fill="x", expand=True)

#..
labelNamaSiswa = ttk.Label(inputFrame, text = "Masukan Nama Siswa")
labelNamaSiswa.pack(padx=10, pady=3, fill="x", expand=True)

entryNamaSiswa= ttk.Entry(inputFrame)
entryNamaSiswa.pack(padx=10, pady=3, fill="x", expand=True)

labelNilai1 = ttk.Label(inputFrame, text = "Masukan Nilai Biologi")
labelNilai1.pack(padx=10, pady=5, fill="x", expand=True)

entryNilai1= ttk.Entry(inputFrame)
entryNilai1.pack(padx=10, pady=3, fill="x", expand=True)

labelNilai2 = ttk.Label(inputFrame, text = "Masukan Nilai Fisika")
labelNilai2.pack(padx=10, pady=3, fill="x", expand=True)

entryNilai2= ttk.Entry(inputFrame)
entryNilai2.pack(padx=10, pady=3, fill="x", expand=True)

labelNilai3 = ttk.Label(inputFrame, text = "Masukan Nilai Bahasa Inggris")
labelNilai3.pack(padx=10, pady=3, fill="x", expand=True)

entryNilai3= ttk.Entry(inputFrame)
entryNilai3.pack(padx=10, pady=3, fill="x", expand=True)

labelPrediksiFakultas = ttk.Label(inputFrame, text = "Hasil Prediksi")
labelPrediksiFakultas.pack(padx=10, pady=3, fill="x", expand=True)

#Membuat Button
def klikbutton():
    nama_siswa = entryNamaSiswa.get()
    Nilai1 = float(entryNilai1.get())
    Nilai2 = float(entryNilai2.get())
    Nilai3 = float(entryNilai3.get())

    if Nilai1 > Nilai2 and Nilai1 > Nilai3:
        prediksi_fakultas = "Kedokteran"
    elif Nilai2 > Nilai1 and Nilai2 > Nilai3:
        prediksi_fakultas = "Teknik"
    elif Nilai3 > Nilai1 and Nilai3 > Nilai2:
        prediksi_fakultas = "Bahasa"
    else:
        prediksi_fakultas = "Tidak dapat diprediksi"

    messagebox.showinfo("Hasil prediksi", f"\nHasil Prediksi Prodi {prediksi_fakultas}!")
    simpan_data_ke_sqlite(NamaSiswa, Nilai1, Nilai2, Nilai3, prediksi_fakultas)

def simpan_data_ke_sqlite(namasiswa, Nilai1, Nilai2, Nilai3, prodi_terpilih):
# Membuka atau membuat database SQLite
    conn = sqlite3.connect("appdb.db")
    cursor = conn.cursor()
    cursor.excecute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nilai1 INTEGER, 
                        nilai2 INTEGER,
                        prodi_terpilih TEXT)''')
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, nilai1, nilai2, nilai3, prodi_terpilih) VALUES (?, ?, ?)",
                        (NamaSiswa, Nilai1, Nilai2, Nilai3, prodi_terpilih))
    conn.commit()
    conn.close()


ButtonSubmit = ttk.Button(inputFrame, text="Hasil Prediksi", command=klikbutton)
ButtonSubmit.pack(padx=10, pady=10, fill="x", expand=True)
 
import sqlite3

   
    

    











uiApp.mainloop()


