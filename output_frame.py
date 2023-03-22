import random
import tkinter
from colors import buttons_color, mouse_above, font


class GuiBoard(tkinter.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)

        self.main_window = main_window
        self.game_mode = ''
        self.current_symbol = 'X'
        self.value_inserted = 0
        self.buttons_already_selected = []
        self.pc_select = False
        self.still_play = True

        self.buttons = {}
        for index in range(1, 10):

            def button_function(row=(index-1)//3, column=(index-1) % 3):
                return lambda: self.button_press(row, column)

            self.buttons.update({f'button_{(index-1)//3}_{(index-1)%3}': tkinter.Button(self, text='', borderwidth=3,
                            bg=buttons_color, font=font, width=5, height=2, activebackground=buttons_color,
                            command=button_function(row=(index-1)//3, column=(index-1) % 3))})
            self.buttons[f'button_{(index-1)//3}_{(index-1)%3}'].grid(row=(index - 1) // 3, column=(index - 1) % 3)

            def mouse_over_lambda(row=(index-1)//3, column=(index - 1) % 3):
                return lambda x: self.mouse_above(row, column)

            def mouse_leave_lambda(row=(index-1)//3, column=(index - 1) % 3):
                return lambda x: self.mouse_leave(row, column)

            self.buttons[f'button_{(index - 1) // 3}_{(index - 1) % 3}'].bind("<Enter>",
                                                            mouse_over_lambda(row=(index-1)//3, column=(index - 1) % 3))
            self.buttons[f'button_{(index - 1) // 3}_{(index - 1) % 3}'].bind("<Leave>",
                                                            mouse_leave_lambda(row=(index-1)//3, column=(index - 1) % 3))

    def mouse_above(self, row, column):
        if self.buttons[f'button_{row}_{column}'].cget('text') == '':
            self.buttons[f'button_{row}_{column}'].config(bg=mouse_above)

    def mouse_leave(self, row, column):
        if self.buttons[f'button_{row}_{column}'].cget('text') == '':
            self.buttons[f'button_{row}_{column}'].config(bg=buttons_color)

    def make_radio_buttons_disabled(self):
        self.main_window.input_frame.pc_radio_button.config(state='disabled')
        self.main_window.input_frame.other_player_radio_button.config(state='disabled')

    def make_radio_buttons_normal(self):
        self.main_window.input_frame.pc_radio_button.config(state='normal')
        self.main_window.input_frame.other_player_radio_button.config(state='normal')

    def button_press(self, row, column):
        if self.still_play:
            self.game_mode = self.main_window.input_frame.play.get()
            self.make_radio_buttons_disabled()
            if self.buttons[f'button_{row}_{column}'].cget('text') == '':
                self.find_current_symbol()
                self.value_inserted += 1
                self.buttons[f'button_{row}_{column}'].config(text=f'{self.current_symbol}')
                self.buttons[f'button_{row}_{column}'].config(bg=buttons_color)
                self.buttons_already_selected.append(f'button_{row}_{column}')
                self.who_won()
                if self.game_mode == 'pc':
                    self.pc_mark_a_square()

    def reset(self):
        for index in range(1, 10):
            self.buttons[f'button_{(index-1)//3}_{(index-1)%3}'].config(text='', bg=buttons_color)
        self.current_symbol = 'X'
        self.value_inserted = 0
        self.main_window.winner_frame.winn_label.config(text='')
        self.make_radio_buttons_normal()
        self.buttons_already_selected = []
        self.still_play = True

    def find_current_symbol(self):
        if self.value_inserted % 2 == 0:
            self.current_symbol = 'X'
        else:
            self.current_symbol = '0'

    def pc_mark_a_square(self):
        self.pc_select = False
        if self.value_inserted < 9:
            while not self.pc_select:
                row_nr = random.choice(range(0, 3))
                column_nr = random.choice(range(0, 3))
                current_square = f'button_{row_nr}_{column_nr}'
                if current_square not in self.buttons_already_selected:
                    self.buttons_already_selected.append(current_square)
                    self.buttons[current_square].config(text='0')
                    self.pc_select = True
                    self.value_inserted += 1
                    self.who_won()

    def who_won(self):
        # check lines
        for line_nr in range(0, 3):
            if self.buttons[f'button_{line_nr}_0'].cget('text') != '' and (self.buttons[f'button_{line_nr}_0'].
                        cget('text') == self.buttons[f'button_{line_nr}_1'].cget('text') == self.buttons
                        [f'button_{line_nr}_2'].cget('text')):
                self.buttons[f'button_{line_nr}_0'].config(bg='green')
                self.buttons[f'button_{line_nr}_1'].config(bg='green')
                self.buttons[f'button_{line_nr}_2'].config(bg='green')
                self.main_window.winner_frame.winn_label.config(
                    text=f"{self.buttons[f'button_{line_nr}_0'].cget('text')} wins! \n Line completed!")
                self.still_play = False
                return
        # check columns
        for column_nr in range(0, 3):
            if self.buttons[f'button_0_{column_nr}'].cget('text') != '' and (self.buttons[f'button_0_{column_nr}']
                        .cget('text') == self.buttons[f'button_1_{column_nr}'].cget('text') == self.buttons[f'button_2_'
                        f'{column_nr}'].cget('text')):
                self.buttons[f'button_0_{column_nr}'].config(bg='green')
                self.buttons[f'button_1_{column_nr}'].config(bg='green')
                self.buttons[f'button_2_{column_nr}'].config(bg='green')
                self.main_window.winner_frame.winn_label.config(
                    text=f"{self.buttons[f'button_0_{column_nr}'].cget('text')} wins! \n Column completed!")
                self.still_play = False
                return

        # first diagonal win
        if self.buttons['button_0_0'].cget('text') != '' and (self.buttons['button_0_0'].cget('text') ==
                        self.buttons['button_1_1'].cget('text') == self.buttons['button_2_2'].cget('text')):
            self.buttons['button_0_0'].config(bg='green')
            self.buttons['button_1_1'].config(bg='green')
            self.buttons['button_2_2'].config(bg='green')
            self.main_window.winner_frame.winn_label.config(
                text=f"{self.buttons['button_0_0'].cget('text')} wins! \n First diagonal completed!")
            self.still_play = False
            return
        # second diagonal win
        if self.buttons['button_0_2'].cget('text') != '' and (self.buttons['button_0_2'].cget('text') ==
                        self.buttons['button_1_1'].cget('text') == self.buttons['button_2_0'].cget('text')):
            self.buttons['button_0_2'].config(bg='green')
            self.buttons['button_1_1'].config(bg='green')
            self.buttons['button_2_0'].config(bg='green')
            self.main_window.winner_frame.winn_label.config(
                text=f"{self.buttons['button_0_2'].cget('text')} wins! \n Second diagonal completed!")
            self.still_play = False
            return

        if self.value_inserted == 9:
            self.main_window.winner_frame.winn_label.config(
                text="Draw!")
            return
