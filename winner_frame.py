import tkinter
from colors import main_frame_color, input_font


class Winn(tkinter.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)

        self.main_window = main_window
        self.config(bg=main_frame_color)
        self.winn_label = tkinter.Label(self, text='', bg=main_frame_color, font=input_font)
        self.winn_label.pack()
