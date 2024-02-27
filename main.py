import game_selection
import tkinter as tk

if __name__ == "__main__":
    main_window = tk.Tk()
    gs = game_selection.GameSelection(main_window)
    gs.render()
    main_window.mainloop()
