import tkinter as tk
from tkinter import ttk
from base_game import BaseGame

class BejeweledGame(BaseGame):
    def __init__(self, master, username1, username2):
        self.colors = ["black", "white", "pink", "brown", "grey"]
        super().__init__(master, username1, username2, self.colors)
        self.master.title("Bejeweled")

    # def create_game_board(self):
    #     # Override the create_game_board method to customize Bejeweled game board UI
    #     super().create_game_board()



def main():
    root = tk.Tk()
    bejeweled_game = BejeweledGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
