import tkinter as tk
from common_styles import configure_style

class Game:
    def __init__(self, master, game_name, username1, username2):
        self.master = master
        self.master.title(game_name)
        self.game_name = game_name
        self.username1 = username1
        self.username2 = username2
        configure_style()
        self.create_game_screen()

    def create_game_screen(self):
        self.label = tk.Label(self.master, text=f"Welcome {self.username1} and {self.username2} to {self.game_name}!")
        self.label.pack()
