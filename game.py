import tkinter as tk
from common_styles import configure_style
from games import bejeweled, candy_crush
from renderable import Renderable
from algorithms.adding_algorithms.candy_crush_adding_algorithm import CandyCrushAddingAlgorithm
from algorithms.matching_algorithms.candy_crush_matching_algorithm import CandyCrushMatchingAlgorithm
from base_game import BaseGame


class Game(Renderable):
    def __init__(self, master, game_name, username1, username2):
        super(Game, self).__init__(master)
        self.master.title(game_name)
        self.game_name = game_name
        self.username1 = username1
        self.username2 = username2
        configure_style(self.master)
    
    def render(self):
        self.clear_screen()
        self.create_game_screen()

    def create_game_screen(self):
        self.label = tk.Label(self.master,
                              text = f"Welcome {self.username1} and {self.username2} to {self.game_name}!")
        self.label.pack(expand = True)

        if self.game_name == "Candy Crush":
            candy_crush_game = candy_crush.CandyCrushGame(self.master, self.username1, self.username2)
            candy_crush_game.render()
        elif self.game_name == "Bejeweled":
            bejeweled_game = bejeweled.BejeweledGame(self.master, self.username1, self.username2)
            bejeweled_game.render()
        elif self.game_name == "Base Game":
            base_game = BaseGame(self.master, self.username1, self.username2)
            base_game.render()



