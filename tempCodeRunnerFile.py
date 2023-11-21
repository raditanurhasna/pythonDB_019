import  tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

uiApp = tk.Tk()
uiApp.configure(background='grey')
uiApp.geometry("1000x1000")
uiApp.resizable()
uiApp.title("Prediksi Prodi Pilihan")

#make canvas
inputFrame = tk.Frame(uiApp)
inputFrame.pack(padx=10, fill="x", expand = True)

#make label
inputLabel = tk.Label(inputFrame, text="Prediksi Prodi Pilihan")
inputLabel.pack(padx=10, pady=10, fill="x", expand=True)

#..
labelMapel1 = ttk.Label(inputFrame, text = "Masukan Nilai Bahasa Indonesia")
labelMapel1.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel1= ttk.Entry(inputFrame)
entryInputMapel1.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel2 = ttk.Label(inputFrame, text = "Masukan Nilai Matematika")
labelMapel2.pack(padx=10, pady=5, fill="x", expand=True)

entryInputMapel2= ttk.Entry(inputFrame)
entryInputMapel2.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel3 = ttk.Label(inputFrame, text = "Masukan Nilai Bahasa Inggris")
labelMapel3.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel3= ttk.Entry(inputFrame)
entryInputMapel3.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel4 = ttk.Label(inputFrame, text = "Masukan Nilai Kimia")
labelMapel4.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel4= ttk.Entry(inputFrame)
entryInputMapel4.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel5 = ttk.Label(inputFrame, text = "Masukan Nilai Fisika")
labelMapel5.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel5= ttk.Entry(inputFrame)
entryInputMapel5.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel6 = ttk.Label(inputFrame, text = "Masukan Nilai Biologi")
labelMapel6.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel6= ttk.Entry(inputFrame)
entryInputMapel6.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel7 = ttk.Label(inputFrame, text = "Masukan Nilai Ekonomi")
labelMapel7.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel7= ttk.Entry(inputFrame)
entryInputMapel7.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel8 = ttk.Label(inputFrame, text = "Masukan Nilai Geografi")
labelMapel8.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel8= ttk.Entry(inputFrame)
entryInputMapel8.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel9 = ttk.Label(inputFrame, text = "Masukan Nilai Sosiologi")
labelMapel9.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel9= ttk.Entry(inputFrame)
entryInputMapel9.pack(padx=10, pady=3, fill="x", expand=True)

labelMapel10 = ttk.Label(inputFrame, text = "Masukan Nilai Sejarah")
labelMapel10.pack(padx=10, pady=3, fill="x", expand=True)

entryInputMapel10= ttk.Entry(inputFrame)
entryInputMapel10.pack(padx=10, pady=3, fill="x", expand=True)

#.. 
#fungsi dialog 
def klikButton():
    Mapel1 = entryInputMapel1.get()
    Mapel2 = entryInputMapel2.get()
    Mapel3 = entryInputMapel3.get()
    Mapel4 = entryInputMapel4.get()
    Mapel5 = entryInputMapel5.get()
    Mapel6 = entryInputMapel6.get()
    Mapel7 = entryInputMapel7.get()
    Mapel8 = entryInputMapel8.get()
    Mapel9 = entryInputMapel9.get()
    Mapel10 = entryInputMapel10.get()

    messagebox.showinfo("Prediksi nilai prodi",

                         " \n Prodi Teknologi Informasi" )


ButtonSubmit = ttk.Button(inputFrame, text="Hasil Prediksi", command=klikButton)
ButtonSubmit.pack(padx=10, pady=10, fill="x", expand=True)
uiApp.mainloop()
