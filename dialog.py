import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox



class Dialog:
    def create_window(self) -> Tk:
        window=Tk()
        window.title("계산기")
        geometry = f"{self._window_width}x{self._window_height}+{self._window_append}+{self._window_append}"
        window.geometry(geometry)
        window.resizable(False, False)
        return window

    def __init__(self):
        self._window_width = 340
        self._window_height = 180
        self._window_append = 200
        self._display_height = 2
        self._display_width  = 30
        self._window = self.create_window()

    @property
    def display_height(self):
        return self._display_height

    @display_height.setter
    def display_height(self, val):
        self._display_height = val

    @property
    def display_width(self):
        return self._display_width

    @display_width.setter
    def display_width(self, val):
        self._display_width = val

