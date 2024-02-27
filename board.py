from tiles.base_tile import BaseTile

class Board:
    def __init__(self, row, col, tilesSet):
        self.row = row
        self.col = col
        self.tilesSet = tilesSet
        self.board = []
        self.score_board = []
        for i in range(row):
            self.board.append([])
            self.score_board.append([])
            for j in range(col):
                self.board[-1].append(BaseTile(i, j, "empty"))
                self.score_board[-1].append(0)
    
    def clear_score_board(self):
        for i in range(self.row):
            for j in range(self.col):
                self.score_board[i][j] = 0