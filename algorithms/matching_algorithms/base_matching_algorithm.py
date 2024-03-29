class BaseMatchingAlgorithm:
    # Match will return score of the match
    def match(self, board) -> int:
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
                    if board.board[i][j].type == "black":
                        total_score += 150  # Assuming 150 for special black tile matches
                    else:
                        total_score += 10 * (2 ^ board.score_board[i][j])
                    board.board[i][j].type = "empty"
        return total_score