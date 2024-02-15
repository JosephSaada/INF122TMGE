import tkinter as tk
import random

class BaseGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Base Game")
        self.create_game_board()
        self.current_player = 1

    def create_game_board(self):
        # Define the size of the game board (number of rows and columns)
        num_rows = 5
        num_cols = 5
        cell_size = 50

        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()

        self.cells = []

        colors = ["red", "blue", "green", "yellow", "orange"]

        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                cell = tk.Canvas(self.board_frame, width=cell_size, height=cell_size,
                                 bg="white", highlightthickness=1,
                                 highlightbackground="black")
                cell.grid(row=i, column=j)
                row.append(cell)
                color = random.choice(colors)
                cell.create_rectangle(2, 2, cell_size-2, cell_size-2, fill=color, outline="")
            self.cells.append(row)

    def switch_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
    def start_game(self):
        pass

    def end_game(self):
        pass

def main():
    root = tk.Tk()
    base_game = BaseGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
