import tkinter as tk
from tkinter import ttk
from login import Login
from common_styles import configure_style

class GameSelection:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Selection")
        configure_style()  # Apply common style
        self.create_game_selection_screen()

    def create_game_selection_screen(self):
        self.game_label = ttk.Label(self.master, text="Select a game:")
        self.game_label.grid(row=0, column=0)

        games = [("Candy Crush", self.start_game_1), ("Bejeweled", self.start_game_2)]
        for i, (game_name, callback) in enumerate(games):
            button = ttk.Button(self.master, text=game_name, command=lambda name=game_name: callback(name))
            button.grid(row=i+1, column=0)

    def start_game_1(self, game_name):
        self.master.destroy()
        root = tk.Tk()
        login = Login(root, game_name)
        root.mainloop()

    def start_game_2(self, game_name):
        self.master.destroy()
        root = tk.Tk()
        login = Login(root, game_name)
        root.mainloop()

def main():
    root = tk.Tk()
    game_selection = GameSelection(root)
    root.mainloop()

if __name__ == "__main__":
    main()
