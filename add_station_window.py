import tkinter as tk
import tkinter.messagebox


class Window(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry('250x250')
        self.title = 'Добавление станции'
        self.ent_station = tk.Entry(self)
        self.ent_station.pack()
        btn_add = tk.Button(self, text='Добавить', command=self.add)
        btn_add.pack()
        self.lst_stations = tk.Listbox(self)
        self.lst_stations.pack()
        btn_close = tk.Button(self, text='Сохранить')
        btn_close.pack()

    def add(self):
        station = str(self.ent_station.get()).strip()
        if station:
            self.lst_stations.insert(tk.END, station)
        else:
            tkinter.messagebox.showerror('Пожалуйста введите станцию')
