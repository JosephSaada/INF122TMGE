from tiles.base_tile import BaseTile
import random
class BaseAddingAlgorithm:
    def register_matching_algorithm(self, matching_algorithm):
        self.matching_algorithm = matching_algorithm
    # Add will also return an integer for chain match scores
    def add(self, board) -> int:
        # top-down flood to fill all empty tiles with existing tiles, then for each column, fill the top with new tiles
        for col in range(board.col):
            unemptyCol = []
            for row in range(board.row):
                if board.board[row][col].type != "empty":
                    unemptyCol.append(board.board[row][col])
            # now col contains all non-empty tiles
            emptyTiles = board.row - len(unemptyCol)
            for row in range(board.row):
                if row < emptyTiles:
                    board.board[row][col] = BaseTile(row, col, random.choice(board.tilesSet))
                else:
                    board.board[row][col] = unemptyCol[row - emptyTiles]
        chain_match_score = self.matching_algorithm.match(board)
        if chain_match_score > 0:
            chain_match_score += self.add(board)
        return chain_match_score  # Not used right now, but we can use it to calculate the score of the player