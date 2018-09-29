#!/usr/bin/env python
"""
Python Version: Python 3.6.6
Author: Shannon Blackhall
Date: 29/09/2018
Program Version: V1

Simple Bus Booking System with tkinter gui
"""
import tkinter as tk


class booking:
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
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent


class MainApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bus = Bus()
        self.parent = parent


def main():
    root = tk.Tk()
    mainapp = MainApp(root)
    mainapp.pack()
    root.mainloop()
    pass


if __name__ == '__main__':
    main()