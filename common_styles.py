import tkinter as tk
from tkinter import ttk

def configure_style():
    style = ttk.Style()

    style.configure('TLabel', font=('Helvetica', 12), padding=10)

    style.configure('TButton', font=('Helvetica', 12), padding=10)
