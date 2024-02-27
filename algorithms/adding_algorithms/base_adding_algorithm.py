class BaseAddingAlgorithm:
    def register_matching_algorithm(self, matching_algorithm):
        self.matching_algorithm = matching_algorithm
    # Add will also return an integer for chain match scores
    def add(self, board) -> int:
        return 0