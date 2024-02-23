import tkinter as tk
from tkinter import ttk
from base_game import BaseGame

class BejeweledGame(BaseGame):
    def __init__(self, master, username1, username2):
        super().__init__(master, username1, username2)
        self.master.title("Candy Crush")
        self.set_colors(["black", "white", "pink", "brown", "grey"])

def main():
    root = tk.Tk()
    bejeweled_game = BejeweledGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()