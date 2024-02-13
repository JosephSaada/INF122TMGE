import tkinter as tk
from tkinter import ttk

class BaseGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Base Game")
        self.create_game_board()

    def create_game_board(self):
        pass

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
