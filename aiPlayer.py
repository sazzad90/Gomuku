from minimax import Minimax
class AIPlayer:
    def __init__(self, player_marker):
        self.player_marker = player_marker
        self.minimax = Minimax()

    def make_move(self, board):
        print(f"{self.player_marker}'s turn (AI)")

        # Define the depth for minimax search (you can adjust this)
        depth = 4

        # Calculate the next move using the Minimax algorithm
        move = self.minimax.calculateNextMove(depth, board, self.player_marker)

        if move is not None and all(isinstance(coord, int) for coord in move):
            row, col = move[0], move[1]
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '_':
                print(f"AI's move: Row {row + 1}, Column {col + 1}")
                return row, col

        print("AI couldn't find a valid move.")
        return None, None
