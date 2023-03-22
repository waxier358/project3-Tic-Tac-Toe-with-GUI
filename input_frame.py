import tkinter
from tkinter import StringVar
from colors import main_frame_color, buttons_color, font, input_font


class InputFrame(tkinter.Frame):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.config(bg=main_frame_color)

        self.play = StringVar()
        self.play.set('pc')
        self.pc_radio_button = tkinter.Radiobutton(self, text='Play with PC', variable=self.play, value='pc',
                                                   bg=main_frame_color, activebackground=main_frame_color,
                                                   font=input_font)
        self.pc_radio_button.grid(row=0, column=0, pady=10)

        self.other_player_radio_button = tkinter.Radiobutton(self, text='Play with other player', variable=self.play,
                                                             value='player', bg=main_frame_color,
                                                             activebackground=main_frame_color,
                                                             font=input_font)
        self.other_player_radio_button.grid(row=0, column=1, pady=10)

        self.restart_game = tkinter.Button(self, text='Restart Game', command=self.main_window.output_frame.reset,
                                           bg=buttons_color, activebackground=buttons_color,  borderwidth=3,
                                           font=input_font)
        self.restart_game.grid(row=1, column=0, columnspan=2, sticky='WE', ipadx=94)
