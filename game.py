import tkinter as tk

class GameSelection:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Selection")
        self.create_game_selection_screen()

    def create_game_selection_screen(self):
        self.game_label = tk.Label(self.master, text="Select a game:")
        self.game_label.grid(row=0, column=0)

        games = [("Game 1", self.start_game_1), ("Game 2", self.start_game_2)]
        for i, (game_name, callback) in enumerate(games):
            button = tk.Button(self.master, text=game_name, command=callback)
            button.grid(row=i+1, column=0)

    def start_game_1(self):
        self.master.destroy()
        root = tk.Tk()
        login = Login(root, "Game 1")
        root.mainloop()

    def start_game_2(self):
        self.master.destroy()
        root = tk.Tk()
        login = Login(root, "Game 2")
        root.mainloop()

class Login:
    def __init__(self, master, game_name):
        self.master = master
        self.master.title("Login - " + game_name)
        self.game_name = game_name
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
        empty_screen = EmptyScreen(root, username1, username2)
        root.mainloop()

class EmptyScreen:
    def __init__(self, master, username1, username2):
        self.master = master
        self.master.title("Empty Screen")
        self.username1 = username1
        self.username2 = username2

        self.label = tk.Label(self.master, text=f"Welcome {username1} and {username2}!")
        self.label.pack()

def main():
    root = tk.Tk()
    game_selection = GameSelection(root)
    root.mainloop()

