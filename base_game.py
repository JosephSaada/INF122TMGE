import tkinter as tk
from tkinter import ttk
import random
from renderable import Renderable

class BaseGame(Renderable):
    def __init__(self, master, username1, username2):
        super(BaseGame, self).__init__(master)
        self.username1 = username1
        self.username2 = username2
        self.master.title("Base Game")
        self.current_player = 1
        self.selected_cell = None

    def set_colors(self, colors):
        self.colors = colors
        self.create_game_board()
        self.turn_label = ttk.Label(self.master, text = f"{self.username1}'s Turn")
        self.turn_label.pack()

    def handle_player_input(self, event):
        canvas = event.widget
        row = int(canvas.grid_info()["row"])
        col = int(canvas.grid_info()["column"])

        if self.selected_cell is None:
            self.selected_cell = (row, col)
            self.highlight_cell(canvas)
        else:
            if self.are_adjacent(self.selected_cell, (row, col)):
                self.swap_pieces(self.selected_cell, (row, col))
                self.unhighlight_cell()
                self.selected_cell = None
            else:
                print("Selected cells are not adjacent. Please select an adjacent cell.")

    def highlight_cell(self, canvas):
        canvas.config(highlightbackground="red", highlightthickness=2)

    def unhighlight_cell(self):
        row, col = self.selected_cell
        self.cells[row][col].config(highlightbackground="black", highlightthickness=1)

    def are_adjacent(self, cell1, cell2):
        row1, col1 = cell1
        row2, col2 = cell2
        return abs(row1 - row2) + abs(col1 - col2) == 1

    def swap_pieces(self, cell1, cell2):
        row1, col1 = cell1
        row2, col2 = cell2

        color1 = self.cells[row1][col1].itemcget(tk.ALL, "fill")
        color2 = self.cells[row2][col2].itemcget(tk.ALL, "fill")

        self.cells[row1][col1].itemconfig(tk.ALL, fill=color2)
        self.cells[row2][col2].itemconfig(tk.ALL, fill=color1)

        self.switch_player()
        self.update_turn_label()

    def update_turn_label(self):
        if self.current_player == 1:
            self.turn_label.config(text=f"{self.username1}'s Turn")
        else:
            self.turn_label.config(text=f"{self.username2}'s Turn")

    def create_game_board(self):
        num_rows = 5
        num_cols = 5
        cell_size = 50

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        self.cells = []

        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                cell = tk.Canvas(self.board_frame, width=cell_size, height=cell_size,
                                 bg="white", highlightthickness=1,
                                 highlightbackground="black")
                cell.grid(row=i, column=j)
                cell.bind("<Button-1>", self.handle_player_input)
                row.append(cell)
                color = random.choice(self.colors)
                cell.create_rectangle(2, 2, cell_size-2, cell_size-2, fill=color, outline="")
            self.cells.append(row)

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1