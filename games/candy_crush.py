import tkinter as tk
from tkinter import ttk
from base_game import BaseGame

class CandyCrushGame(BaseGame):
    def __init__(self, master, username1, username2, tileSet, matching_algorithm, adding_algorithm):
        super().__init__(master, username1, username2, tileSet, matching_algorithm, adding_algorithm)
        self.master.title("Candy Crush")
        #self.set_colors(["red", "green", "blue", "yellow", "orange", "purple"])

def main():
    root = tk.Tk()
    candy_crush_game = CandyCrushGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
