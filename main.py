import tkinter
from output_frame import GuiBoard
from input_frame import InputFrame
from winner_frame import Winn
from colors import *


class Gui(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tic Tac Toe')
        self.config(bg=main_frame_color)
        self.geometry('300x420')
        self.iconbitmap('x.ico')

        self.output_frame = GuiBoard(self)
        self.input_frame = InputFrame(self)
        self.winner_frame = Winn(self)

        self.input_frame.pack()
        self.output_frame.pack(pady=(30, 5))
        self.winner_frame.pack()


if __name__ == '__main__':
    app = Gui()
    app.mainloop()
