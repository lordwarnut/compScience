#!/usr/bin/env python
"""
Python Version: Python 3.6.6
Author: Shannon Blackhall
Date: 29/09/2018
Program Version: V1

Simple Bus Booking System with tkinter gui
"""
import tkinter as tk


class Booking:
    def __init__(self):
        pass


class Bus:
    def __init__(self):
        pass


class FinishedFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


class OrderFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


class WelcomeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


class BusFrame(tk.Frame):
    bus_fstring = "Bus Service to {}"
    date_fstring = "Date : {}"
    seat_fstring = "Seats Available  : {}"
    bunk_fstring = "Bunks Available : {}"

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.label = tk.Label(self, text=self.bus_fstring.format(""))
        self.label.grid(row=0, column=0, sticky='w')

        self.grid_rowconfigure(1, minsize=10)

        self.datelabel = tk.Label(self, text=self.date_fstring.format(""))
        self.datelabel.grid(row=2, column=0, sticky='w')

        self.seatlabel = tk.Label(self, text=self.seat_fstring.format(""))
        self.seatlabel.grid(row=3, column=0, sticky='w')

        self.bunklabel = tk.Label(self, text=self.bunk_fstring.format(""))
        self.bunklabel.grid(row=4, column=0, sticky='w')


class MainApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bus = Bus()
        self.parent = parent

        self.busframe = BusFrame(self)
        self.busframe.grid(row=0, column=0)

        self.dataframe = WelcomeFrame(self)
        self.dataframe.grid(row=0, column=1)

def main():
    root = tk.Tk()
    mainapp = MainApp(root)
    mainapp.pack()
    root.mainloop()
    pass


if __name__ == '__main__':
    main()