import tkinter as tk
import random

class BaseGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Base Game")
        self.create_game_board()
        self.current_player = 1
        self.selected_cell = None

    def handle_player_input(self, event):
        # Get the canvas widget that triggered the event
        canvas = event.widget

        # Get the row and column of the clicked cell
        row = int(canvas.grid_info()["row"])
        col = int(canvas.grid_info()["column"])

        # Example: Handle mouse click event to select cell or piece
        if self.current_player == 1:
            # Player 1's turn: implement logic for player 1's actions
            if self.selected_cell is None:
                # If no cell is selected, store the clicked cell as the selected cell
                self.selected_cell = (row, col)
                print(f"Player 1 selected cell [{row}, {col}]")
            else:
                # If a cell is already selected, swap the pieces between the selected cell and the clicked cell
                self.swap_pieces(self.selected_cell, (row, col))
                # Reset the selected cell to None
                self.selected_cell = None
        elif self.current_player == 2:
            # Player 2's turn: implement logic for player 2's actions
            if self.selected_cell is None:
                # If no cell is selected, store the clicked cell as the selected cell
                self.selected_cell = (row, col)
                print(f"Player 2 selected cell [{row}, {col}]")
            else:
                # If a cell is already selected, swap the pieces between the selected cell and the clicked cell
                self.swap_pieces(self.selected_cell, (row, col))
                # Reset the selected cell to None
                self.selected_cell = None

    def swap_pieces(self, cell1, cell2):

        row1, col1 = cell1
        row2, col2 = cell2

        color1 = self.cells[row1][col1].itemcget(tk.ALL, "fill")
        color2 = self.cells[row2][col2].itemcget(tk.ALL, "fill")

        self.cells[row1][col1].itemconfig(tk.ALL, fill = color2)
        self.cells[row2][col2].itemconfig(tk.ALL, fill = color1)

        self.switch_player()
        print(f"Swapping pieces between cells {cell1} and {cell2}")


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
                cell.bind("<Button-1>", self.handle_player_input)
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
