import tkinter as tk
import tkinter.messagebox


class Window(tk.Toplevel):
    def __init__(self, master, stations: list, save_command: callable):
        super().__init__(master)
        self.save_command = save_command
        self.stations = stations
        self.geometry('250x300')
        self.title('Добавление станции')

        ent_frame = tk.Frame(master=self, pady=5)
        lbl_ent = tk.Label(master=ent_frame, text='Название')
        lbl_ent.pack(fill=tk.Y, side=tk.LEFT)
        self.ent_station = tk.Entry(master=ent_frame)
        self.ent_station.pack(fill=tk.Y, side=tk.LEFT)
        ent_frame.pack()

        btn_add = tk.Button(self,
                            text='Добавить',
                            command=self.add)
        btn_add.pack()
        self.lst_stations = tk.Listbox(master=self)
        for station in stations:
            self.lst_stations.insert(tk.END, station)
        self.lst_stations.pack(fill=tk.X, padx=5)

        buts_frame = tk.Frame(master=self)
        self.lbl_save = tk.Label(master=buts_frame, text='Данные сохранены')
        btn_save = tk.Button(buts_frame,
                             text='Сохранить',
                             compound=tk.LEFT,
                             command=self.save)
        btn_cancel = tk.Button(master=buts_frame,
                               text='Отмена',
                               command=self.cancel)
        btn_save.pack(side=tk.LEFT)
        btn_cancel.pack(side=tk.RIGHT)
        buts_frame.pack(side=tk.BOTTOM,
                        fill=tk.X,
                        padx=5,
                        pady=5)

    def add(self):
        station = str(self.ent_station.get()).strip()
        if station and station not in self.stations:
            self.lst_stations.insert(tk.END, station)
            self.ent_station.delete(0)
            self.stations.append(station)
            self.lbl_save.pack_forget()
        else:
            tkinter.messagebox.showerror(parent=self,
                                         title='Ошибка',
                                         message='Пожалуйста введите станцию')

    def save(self):
        self.save_command(self.stations)
        self.lbl_save.pack(side=tk.BOTTOM, pady=5)

    def cancel(self):
        self.destroy()
