class TilesColorDict:
    def __init__(self):
        self.tiles_color_dict = {"red": "red", "blue": "blue", "green": "green", "yellow": "yellow", "orange": "orange", "purple": "purple", "pink": "pink", "empty": "white"} # for more tiles and how to display them, add their names and corresponding colors here
    
    def get_color(self, tileType):
        return self.tiles_color_dict[tileType]