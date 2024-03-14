import random
from tiles.bejeweled_tile import BejeweledTile  # Assuming BejeweledTile is in a module named tiles
from algorithms.adding_algorithms.base_adding_algorithm import BaseAddingAlgorithm

class BejeweledAddingAlgorithm(BaseAddingAlgorithm):
    def add(self, board) -> int:
        for col in range(board.col):
            for row in range(board.row):
                if board.board[row][col].type == "empty":
                    tileType = random.choice(board.tilesSet)
                    is_special = self.should_be_special()  # You define this method
                    board.board[row][col] = BejeweledTile(row, col, tileType, is_special)
        return super().add(board)  # Optionally use the base method for additional logic

    def should_be_special(self):
        # Example condition for creating a special tile
        return random.random() < 0.1  # 10% chance
