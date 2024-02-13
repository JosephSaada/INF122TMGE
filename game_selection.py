import tkinter as tk
from tkinter import ttk
from login import Login
from common_styles import configure_style

class GameSelection:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Selection")
        configure_style(self.master)
        self.create_game_selection_screen()

    def create_game_selection_screen(self):
        frame = ttk.Frame(self.master)
        frame.pack(expand = True, fill = 'both')

        self.game_label = ttk.Label(frame, text = "Select a game:")
        self.game_label.pack(pady = 10)

        games = [("Candy Crush", lambda: self.start_game("Candy Crush")),
                 ("Bejeweled", lambda: self.start_game("Bejeweled"))]

        for game_name, callback in games:
            button = ttk.Button(frame, text = game_name, command = callback)
            button.pack(pady = 5)

    def start_game(self, game_name):
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
