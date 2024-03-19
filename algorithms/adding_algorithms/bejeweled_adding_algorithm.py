import random
from tiles.bejeweled_tile import BejeweledTile  
from algorithms.adding_algorithms.base_adding_algorithm import BaseAddingAlgorithm

class BejeweledAddingAlgorithm(BaseAddingAlgorithm):
    def add(self, board) -> int:
        for col in range(board.col):
            for row in range(board.row):
                if board.board[row][col].type == "empty":
                    filtered_tileset = [tile for tile in board.tilesSet if tile != "black"]
                    tileType = random.choice(filtered_tileset)
                    is_special = self.should_be_special()  
                    board.board[row][col] = BejeweledTile(row, col, tileType, is_special)
        return super().add(board)  

    def should_be_special(self):
        #  condition for creating a special black tile to spawn
        return random.random() < 0.001  
