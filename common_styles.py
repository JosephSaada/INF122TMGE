import tkinter as tk
from tkinter import ttk

def configure_style(root):
    style = ttk.Style()

    style.configure('TLabel', font=('Helvetica', 12), padding=10)

    style.configure('TButton', font=('Helvetica', 12), padding=10)

    style.configure('TEntry', font=('Helvetica', 12), padding=10)

    root.geometry("300x350")

