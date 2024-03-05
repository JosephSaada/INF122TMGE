import tkinter as tk
from tkinter import ttk
from game import Game
from common_styles import configure_style
from renderable import Renderable

class Login(Renderable):
    def __init__(self, master, game_name):
        super(Login, self).__init__(master)
        self.master.title("Login - " + game_name)
        self.game_name = game_name
        configure_style(self.master)

    def render(self):
        self.clear_screen()
        self.create_login_screen()

    def create_login_screen(self):
        frame = ttk.Frame(self.master)
        frame.pack(expand = True, fill = 'both')

        username1_frame = ttk.Frame(frame)
        username1_frame.pack(fill = 'x', padx = 10, pady = (10, 5))

        self.username1_label = ttk.Label(username1_frame, text = "Username 1:")
        self.username1_label.pack(side = 'left')

        self.username1_entry = ttk.Entry(username1_frame)
        self.username1_entry.pack(side = 'right', fill = 'x', expand = True)

        username2_frame = ttk.Frame(frame)
        username2_frame.pack(fill = 'x', padx = 10, pady = 5)

        self.username2_label = ttk.Label(username2_frame, text = "Username 2:")
        self.username2_label.pack(side = 'left')

        self.username2_entry = ttk.Entry(username2_frame)
        self.username2_entry.pack(side = 'right', fill = 'x', expand = True)

        # Login button
        self.login_button = ttk.Button(frame, text = "Login", command = self.login)
        self.login_button.pack(fill = 'x', padx = 10, pady = (5, 10))

    def login(self):
        username1 = self.username1_entry.get()
        username2 = self.username2_entry.get()

        if not username1:
            username1 = "user1"
        if not username2:
            username2 = "user2"

        game = Game(self.master, self.game_name, username1, username2)
        game.render()
