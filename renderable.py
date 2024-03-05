class Renderable:
    def __init__(self, master):
        self.master = master
    
    def render(self):
        pass
    
    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()