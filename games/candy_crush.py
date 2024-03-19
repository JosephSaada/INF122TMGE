import tkinter as tk
from tkinter import ttk
from base_game import BaseGame
from algorithms.adding_algorithms.candy_crush_adding_algorithm import CandyCrushAddingAlgorithm
from algorithms.matching_algorithms.candy_crush_matching_algorithm import CandyCrushMatchingAlgorithm

class CandyCrushGame(BaseGame):
    def __init__(self, master, username1, username2):
        tileSet = ["red", "blue", "green", "yellow", "orange", "purple"]
        matching_algorithm = CandyCrushMatchingAlgorithm()
        adding_algorithm = CandyCrushAddingAlgorithm()
        adding_algorithm.register_matching_algorithm(matching_algorithm)
        super().__init__(master, username1, username2, tileSet)
        self.tileSet = tileSet
        self.add_tiles_algorithm = adding_algorithm
        self.matching_algorithm = matching_algorithm
        self.master.title("Candy Crush")

    def swap_pieces(self, cell1, cell2):
        if self.board.board[cell1[0]][cell1[1]].type != "special_4_connected" and self.board.board[cell1[0]][cell1[1]].type != "special_5_connected" and self.board.board[cell2[0]][cell2[1]].type != "special_4_connected" and self.board.board[cell2[0]][cell2[1]].type != "special_5_connected":
            super().swap_pieces(cell1, cell2)
            return

        print("Inside swap_pieces in CandyCrushGame")
        row1, col1 = cell1
        row2, col2 = cell2
        temp = self.board.board[row1][col1]
        self.board.board[row1][col1] = self.board.board[row2][col2]
        self.board.board[row2][col2] = temp

        # two special_4_connected tiles
        # Clear all tiles in the same row and col for each special_4_connected tile and add num tiles * 10 score to the current player
        if self.board.board[row1][col1].type == "special_4_connected" and self.board.board[row2][col2].type == "special_4_connected":
            count = 0
            count += self.clear_tiles_in_same_row_and_col(row1, col1)
            count += self.clear_tiles_in_same_row_and_col(row2, col2)

            addScore = self.add_tiles_algorithm.add(self.board)
            
            if self.current_player == 1:
                self.playerOneScore += addScore + count * 10
            else:
                self.playerTwoScore += addScore + count * 10
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return 
        # two special_5_connected tiles
        # CLEAR ALL TILES and add num tiles * 30 score to the current player
        if self.board.board[row1][col1].type == "special_5_connected" and self.board.board[row2][col2].type == "special_5_connected":
            count = self.clear_all_tiles()

            addScore = self.add_tiles_algorithm.add(self.board)
            
            if self.current_player == 1:
                self.playerOneScore += addScore + count * 30
            else:
                self.playerTwoScore += addScore + count * 30
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return

        # one special_4_connected and one special_5_connected
        # Clear all tiles within three rows and three cols of the special_5_connected tile and num tiles * 20 score to the current player
        if self.board.board[row1][col1].type == "special_4_connected" and self.board.board[row2][col2].type == "special_5_connected":
            count = self.clear_tiles_within_three_rows_and_cols(row2, col2)

            addScore = self.add_tiles_algorithm.add(self.board)

            if self.current_player == 1:
                self.playerOneScore += addScore + count * 20
            else:
                self.playerTwoScore += addScore + count * 20
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return
        
        if self.board.board[row1][col1].type == "special_5_connected" and self.board.board[row2][col2].type == "special_4_connected":
            count = self.clear_tiles_within_three_rows_and_cols(row1, col1)

            addScore = self.add_tiles_algorithm.add(self.board)

            if self.current_player == 1:
                self.playerOneScore += addScore + count * 20
            else:
                self.playerTwoScore += addScore + count * 20
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return

        # one normal tile and one special_4_connected
        # Clear all tiles in the same row and add num tiles * 10 score to the current player
        if self.board.board[row1][col1].type != "empty" and self.board.board[row2][col2].type == "special_4_connected":
            count = self.clear_tiles_in_same_row(row1, col1)

            addScore = self.add_tiles_algorithm.add(self.board)

            if self.current_player == 1:
                self.playerOneScore += addScore + count * 10
            else:
                self.playerTwoScore += addScore + count * 10
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return
        
        if self.board.board[row1][col1].type == "special_4_connected" and self.board.board[row2][col2].type != "empty":
            count = self.clear_tiles_in_same_row(row2, col2)

            addScore = self.add_tiles_algorithm.add(self.board)

            if self.current_player == 1:
                self.playerOneScore += addScore + count * 10
            else:
                self.playerTwoScore += addScore + count * 10
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return

        # one normal tile and one special_5_connected
        # Clear all tiles in the same row and col and add num tiles * 15 score to the current player
        if self.board.board[row1][col1].type != "empty" and self.board.board[row2][col2].type == "special_5_connected":
            count = self.clear_tiles_in_same_row_and_col(row1, col1)

            addScore = self.add_tiles_algorithm.add(self.board)

            if self.current_player == 1:
                self.playerOneScore += addScore + count * 15
            else:
                self.playerTwoScore += addScore + count * 15
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return
        
        if self.board.board[row1][col1].type == "special_5_connected" and self.board.board[row2][col2].type != "empty":
            count = self.clear_tiles_in_same_row_and_col(row2, col2)

            addScore = self.add_tiles_algorithm.add(self.board)

            if self.current_player == 1:
                self.playerOneScore += addScore + count * 15
            else:
                self.playerTwoScore += addScore + count * 15
            
            self.render()
            self.switch_player()
            self.update_turn_label()
            return

    def clear_tiles_in_same_row(self, row, col):
        count = 0
        for i in range(self.board.row):
            if self.board.board[i][col].type != "empty":
                self.board.board[i][col].type = "empty"
                count += 1
        return count
    
    def clear_tiles_in_same_col(self, row, col):
        count = 0
        for j in range(self.board.col):
            if self.board.board[row][j].type != "empty":
                self.board.board[row][j].type = "empty"
                count += 1
        return count

    def clear_all_tiles(self):
        count = 0
        for i in range(self.board.row):
            for j in range(self.board.col):
                if self.board.board[i][j].type != "empty":
                    self.board.board[i][j].type = "empty"
                    count += 1
        return count
    
    def clear_tiles_in_same_row_and_col(self, row, col):
        count = 0
        count += self.clear_tiles_in_same_row(row, col)
        count += self.clear_tiles_in_same_col(row, col)
        return count

    def clear_tiles_within_three_rows_and_cols(self, row, col):
        count = 0
        if row - 1 >= 0:
            count += self.clear_tiles_in_same_row_and_col(row - 1, col)
        if row + 1 < self.board.row:
            count += self.clear_tiles_in_same_row_and_col(row + 1, col)
        if col - 1 >= 0:
            count += self.clear_tiles_in_same_row_and_col(row, col - 1)
        if col + 1 < self.board.col:
            count += self.clear_tiles_in_same_row_and_col(row, col + 1)
        count += self.clear_tiles_in_same_row_and_col(row, col)
        return count