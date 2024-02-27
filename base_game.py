import tkinter as tk
from tkinter import ttk
import random
from renderable import Renderable
from board import Board
import tiles
from  tiles_color_dict import TilesColorDict

class BaseGame(Renderable):
    def __init__(self, master, username1, username2, tileSet, matching_algorithm=None, add_tiles_algorithm=None):
        super(BaseGame, self).__init__(master)
        self.username1 = username1
        self.username2 = username2
        self.master.title("Base Game")
        self.current_player = 1
        self.selected_cell = None
        self.matching_algorithm = matching_algorithm
        self.add_tiles_algorithm = add_tiles_algorithm
        self.add_tiles_algorithm.register_matching_algorithm(self.matching_algorithm)
        self.board = Board(5, 5, tileSet)
        self.TilesColorDict = TilesColorDict()
        self.board_frame = ttk.Frame(self.master)
        self.board_frame.pack()
        self.add_tiles_algorithm.add(self.board)
    
    def clear_board(self):
        for i in self.board_frame.winfo_children():
            i.destroy()
        
    def render(self):
        self.clear_board()
        self.render_game_board()
    
    def create_label(self):
        self.turn_label = ttk.Label(self.master, text = f"{self.username1}'s Turn")
        self.turn_label.pack()

    # modify here to avoid using self.cells to avoid bug
    def handle_player_input(self, event):
        canvas = event.widget
        row = int(canvas.grid_info()["row"])
        col = int(canvas.grid_info()["column"])

        if self.selected_cell is None:
            self.selected_cell = (row, col)
            self.highlight_cell(canvas)
        else:
            if self.selected_cell == (row, col):
                self.unhighlight_cell()
                self.selected_cell = None
            elif self.are_adjacent(self.selected_cell, (row, col)):
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
        # Maybe re-render the whole things here
        row1, col1 = cell1
        row2, col2 = cell2

        temp = self.board.board[row1][col1]
        self.board.board[row1][col1] = self.board.board[row2][col2]
        self.board.board[row2][col2] = temp

        self.matching_algorithm.match(self.board)
        self.add_tiles_algorithm.add(self.board)

        self.render()

        self.switch_player()
        self.update_turn_label()

    def update_turn_label(self):
        if self.current_player == 1:
            self.turn_label.config(text=f"{self.username1}'s Turn")
        else:
            self.turn_label.config(text=f"{self.username2}'s Turn")

    def render_game_board(self):
        # Now render the whole game board based on the data we have
        self.clear_board()
        
        num_rows = self.board.row
        num_cols = self.board.col
        cell_size = 50
        self.cells = []  # Hold references on the rendered cells, so we can modify them like changing highlight color
        for i in range(num_rows):
            self.cells.append([])
            for j in range(num_cols):
                cell = tk.Canvas(self.board_frame, width=cell_size, height=cell_size,
                                 bg="white", highlightthickness=1,
                                 highlightbackground="black")
                cell.grid(row=i, column=j)
                color = self.TilesColorDict.get_color(self.board.board[i][j].type)
                cell.create_rectangle(2, 2, cell_size-2, cell_size-2, fill=color, outline="")
                cell.bind("<Button-1>", self.handle_player_input)
                self.cells[-1].append(cell)
        self.create_label()

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1