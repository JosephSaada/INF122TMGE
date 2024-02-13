import tkinter as tk
from game import Game
from common_styles import configure_style

class Login:
    def __init__(self, master, game_name):
        self.master = master
        self.master.title("Login - " + game_name)
        self.game_name = game_name
        configure_style()
        self.create_login_screen()

    def create_login_screen(self):
        self.username1_label = tk.Label(self.master, text="Username 1:")
        self.username1_label.grid(row=0, column=0)
        self.username1_entry = tk.Entry(self.master)
        self.username1_entry.grid(row=0, column=1)

        self.username2_label = tk.Label(self.master, text="Username 2:")
        self.username2_label.grid(row=1, column=0)
        self.username2_entry = tk.Entry(self.master)
        self.username2_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2)

    def login(self):
        username1 = self.username1_entry.get()
        username2 = self.username2_entry.get()

        # Assign default usernames if not provided
        if not username1:
            username1 = "user1"
        if not username2:
            username2 = "user2"

        self.master.destroy()  # Close login window after both usernames are provided

        root = tk.Tk()
        game = Game(root, self.game_name, username1, username2)
        root.mainloop()
