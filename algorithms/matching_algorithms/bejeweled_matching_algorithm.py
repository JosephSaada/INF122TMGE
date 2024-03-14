from algorithms.matching_algorithms.base_matching_algorithm import BaseMatchingAlgorithm
from tiles.bejeweled_tile import BejeweledTile

class BejeweledMatchingAlgorithm(BaseMatchingAlgorithm):
    def match(self, board) -> int:
        score = super().match(board)  # Use the base matching logic as foundation

        
        # Loop through the board to find matches
        for i in range(board.row):
            for j in range(board.col - 2):
                # Check for a horizontal match of 3
                matched_types = [board.board[i][j+k].type for k in range(3)]
                if matched_types[0] == matched_types[1] == matched_types[2]:
                    print(matched_types)
                    # Calculate the score for this match
                    match_score = self.calculate_match_score(matched_types)
                    score += match_score

                    # Mark matched tiles for clearing or special handling
                    # This part is optional and can be customized as needed

        # Here, you can include additional logic for 5+ combos or special tile handling
        for i in range(board.row):
            for j in range(board.col - 4):
                if all(board.board[i][j + k].type == board.board[i][j].type for k in range(5)):
                    # Make the middle tile of a 5+ combo special
                    board.board[i][j + 2].make_special("black")
                    break  # Assuming one special tile per row max for simplicity

        return score

    def calculate_match_score(self, matched_types):
        """Calculate the score for a match, applying a multiplier for black tiles."""
        base_score_per_tile = 30
        print("i am in calculate")
        if 'black' in matched_types:
            print("BLLLACCCKKKK")
            # Apply a multiplier of 5 for matches involving at least one black tile
            return base_score_per_tile * len(matched_types) * 5
        else:
            return base_score_per_tile * len(matched_types)
