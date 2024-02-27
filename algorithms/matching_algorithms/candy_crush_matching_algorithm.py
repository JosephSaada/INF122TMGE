from algorithms.matching_algorithms.base_matching_algorithm import BaseMatchingAlgorithm

class CandyCrushMatchingAlgorithm(BaseMatchingAlgorithm):
    def match(self, board):
        board.clear_score_board()
        for i in range(board.row):
            for j in range(1, board.col - 1):
                if board.board[i][j].type == board.board[i][j - 1].type == board.board[i][j + 1].type:
                    board.score_board[i][j - 1] += 1
                    board.score_board[i][j] += 1
                    board.score_board[i][j + 1] += 1
        for i in range(1, board.row - 1):
            for j in range(board.col):
                if board.board[i][j].type == board.board[i - 1][j].type == board.board[i + 1][j].type:
                    board.score_board[i - 1][j] += 1
                    board.score_board[i][j] += 1
                    board.score_board[i + 1][j] += 1

        total_score = 0
        for i in range(board.row):
            for j in range(board.col):
                if board.score_board[i][j] > 0:
                    total_score += 10 * (2 ^ board.score_board[i][j])
                    board.board[i][j].type = "empty"
        return total_score