import tkinter as tk
import pickle
from add_station_window import Window


class Manager:
    def __init__(self):
        self.stations = self.load_stations()
        self.root = tk.Tk()
        print(self.root)
        self.root.geometry('500x500')
        self.root.title("Operator")

        btn_add_station = tk.Button(self.root,
                                    text='Добавить станцию',
                                    command=self.add_station)
        btn_add_station.pack()
        self.root.mainloop()

    @staticmethod
    def load_stations():
        try:
            with open('./data/stations', 'rb') as input_file:
                return pickle.load(input_file)
        except (FileNotFoundError, EOFError):
            return []

    @staticmethod
    def save_stations(stations):
        with open('./data/stations', 'wb') as output:
            pickle.dump(stations, output)

    def add_train(self):
        pass

    def add_station(self):
        add_window = Window(self.root, self.stations, self.save_stations)
