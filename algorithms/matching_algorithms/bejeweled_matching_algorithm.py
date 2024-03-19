from algorithms.matching_algorithms.base_matching_algorithm import BaseMatchingAlgorithm
from tiles.bejeweled_tile import BejeweledTile

class BejeweledMatchingAlgorithm(BaseMatchingAlgorithm):
    def match(self, board) -> int:
        score = super().match(board)  # Use base matching logic as foundation
        
        # Handle horizontal matches of 3 for scoring
        for i in range(board.row):
            for j in range(board.col - 2):
                matched_types = [board.board[i][j+k].type for k in range(3)]
                if matched_types[0] == matched_types[1] == matched_types[2]:
                    match_score = self.calculate_match_score(matched_types)
                    score += match_score

        # Make horizontal 5 patterns special
        for i in range(board.row):
            for j in range(board.col - 4):
                if all(board.board[i][j + k].type == board.board[i][j].type for k in range(5)):
                    board.board[i][j + 2].make_special("black")  # Middle tile of a 5 match
                    break  # One special tile per row for simplicity

        # Make vertical 5 patterns special
        for j in range(board.col):
            for i in range(board.row - 4):
                if all(board.board[i + k][j].type == board.board[i][j].type for k in range(5)):
                    board.board[i + 2][j].make_special("black")  # Middle tile of a vertical 5 match
                    break  # One special tile per column for simplicity

        return score

    def calculate_match_score(self, matched_types):
        """Calculate the score for a match, with a multiplier for black tiles."""
        base_score_per_tile = 30
        if 'black' in matched_types:
            # If any of the matched tiles is black, apply a special score multiplier
            return base_score_per_tile * len(matched_types) * 5
        else:
            # Regular scoring for matches without a black tile
            return base_score_per_tile * len(matched_types)