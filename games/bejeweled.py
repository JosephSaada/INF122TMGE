import tkinter as tk
from tkinter import ttk
from base_game import BaseGame
from algorithms.matching_algorithms.bejeweled_matching_algorithm import BejeweledMatchingAlgorithm
from algorithms.adding_algorithms.bejeweled_adding_algorithm import BejeweledAddingAlgorithm

class BejeweledGame(BaseGame):
    def __init__(self, master, username1, username2):
        matching_algorithm = BejeweledMatchingAlgorithm()
        adding_algorithm = BejeweledAddingAlgorithm()
        # self.master.title("Bejeweled")
        tile_set=["blue", "green", "orange", "purple", "red", "black"]
        super().__init__(master, username1, username2, tile_set, matching_algorithm, adding_algorithm)



def main():
    root = tk.Tk()
    bejeweled_game = BejeweledGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()