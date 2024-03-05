import tkinter as tk
from tkinter import ttk
from base_game import BaseGame
from algorithms.adding_algorithms.candy_crush_adding_algorithm import CandyCrushAddingAlgorithm
from algorithms.matching_algorithms.candy_crush_matching_algorithm import CandyCrushMatchingAlgorithm

class CandyCrushGame(BaseGame):
    def __init__(self, master, username1, username2):
        tileSet = ["red", "blue", "green", "yellow", "orange", "purple"]
        matching_algorithm = CandyCrushMatchingAlgorithm()
        adding_algorithm = CandyCrushAddingAlgorithm()
        super().__init__(master, username1, username2, tileSet, matching_algorithm, adding_algorithm)
        self.master.title("Candy Crush")