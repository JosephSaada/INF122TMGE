from algorithms.adding_algorithms.base_adding_algorithm import BaseAddingAlgorithm
from tiles.base_tile import BaseTile
import random

class CandyCrushAddingAlgorithm(BaseAddingAlgorithm):
    def add(self, board) -> int:
        # if there are 4-connected tiles, add one special tile which can destroy all tiles in the same col or row
        # if there are 5-connected tiles, add one special tile which can destroy all tiles in the same col and row
        # use board.score_board to detect 4-connected and 5-connected tiles
        for i in range(board.row):
            for j in range(board.col):
                if board.score_board[i][j] > 1:
                    if board.score_board[i][j] == 2:
                        board.board[i][j].type = "special_4_connected"
                    else:
                        board.board[i][j].type = "special_5_connected"
                else:
                    continue
        # Check T-Pose and L-Pose to change them to speical_5_connected tiles
        # Also make 5-connected tiles become just one special_5_connected tile rather than one 5-connected tile and two 4-connected tiles
        for i in range(board.row):
            for j in range(board.col):
                if board.board[i][j].type == "special_5_connected":
                    if i - 1 >= 0 and board.board[i - 1][j].type == "special_4_connected":
                        board.board[i - 1][j].type = "empty"
                    if i + 1 < board.row and board.board[i + 1][j].type == "special_4_connected":
                        board.board[i + 1][j].type = "empty"
                    if j - 1 >= 0 and board.board[i][j - 1].type == "special_4_connected":
                        board.board[i][j - 1].type = "empty"
                    if j + 1 < board.col and board.board[i][j + 1].type == "special_4_connected":
                        board.board[i][j + 1].type = "empty"
                if board.board[i][j].type == "special_4_connected":
                    # left t-pose
                    if i - 1 >= 0 and i - 2 >= 0 and board.score_board[i - 1][j] == 1 and board.score_board[i - 2][j] == 1:
                        board.board[i][j].type = "special_5_connected"
                        board.board[i - 1][j].type = "empty"
                        board.board[i - 2][j].type = "empty"
                    # right t-pose
                    if i + 1 < board.row and i + 2 < board.row and board.score_board[i + 1][j] == 1 and board.score_board[i + 2][j] == 1:
                        board.board[i][j].type = "special_5_connected"
                        board.board[i + 1][j].type = "empty"
                        board.board[i + 2][j].type = "empty"
                    # up t-pose
                    if j - 1 >= 0 and j - 2 >= 0 and board.score_board[i][j - 1] == 1 and board.score_board[i][j - 2] == 1:
                        board.board[i][j].type = "special_5_connected"
                        board.board[i][j - 1].type = "empty"
                        board.board[i][j - 2].type = "empty"
                    # down t-pose
                    if j + 1 < board.col and j + 2 < board.col and board.score_board[i][j + 1] == 1 and board.score_board[i][j + 2] == 1:
                        board.board[i][j].type = "special_5_connected"
                        board.board[i][j + 1].type = "empty"
                        board.board[i][j + 2].type = "empty"
                    # convert two 4-connected tiles to one 4-connected tile
                    if i - 1 >= 0 and board.board[i - 1][j].type == "special_4_connected":
                        board.board[i - 1][j].type = "empty"
                    if i + 1 < board.row and board.board[i + 1][j].type == "special_4_connected":
                        board.board[i + 1][j].type = "empty"
                    if j - 1 >= 0 and board.board[i][j - 1].type == "special_4_connected":
                        board.board[i][j - 1].type = "empty"
                    if j + 1 < board.col and board.board[i][j + 1].type == "special_4_connected":
                        board.board[i][j + 1].type = "empty"
        # top-down flood to fill all empty tiles with existing tiles, then for each column, fill the top with new tiles
        return super().add(board)