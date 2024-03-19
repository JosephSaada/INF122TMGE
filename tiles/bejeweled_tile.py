from tiles.base_tile import BaseTile

class BejeweledTile(BaseTile):
    def __init__(self, row, col, tileType, is_special=False):
        super().__init__(row, col, tileType)
        self.is_special = is_special

    def make_special(self, new_type):
        self.type = new_type
        self.is_special = True

    def trigger_special_effect(self, board):
        if self.is_special and self.type == "black":
            for col in range(board.col):
                board.board[self.row][col] = BejeweledTile(self.row, col, "empty")  # Clear the row

