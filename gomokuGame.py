class GomokuGame:
    def __init__(self, board_size=10):
        self.board_size = board_size
        self.board = [['_' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = 'W'  # 'W' represents Player 1, 'B' represents Player 2

    def switch_player(self):
        if self.current_player == 'B':
            self.current_player = 'W'
        else:
            self.current_player = 'B'

    def make_move(self, row, col):
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '_':
            self.board[row][col] = self.current_player
            self.switch_player()
            return True
        return False

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def check_win_condition(self):
        consecutive_piece = 5

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] != "_":

                    # Check row wise win condition
                    win = True
                    for i in range(consecutive_piece):
                        if (col + i) >= self.board_size or self.board[row][col + i] != self.board[row][col]:
                            win = False
                            break

                    if win:
                        print(f"{self.current_player} won row wise at {row} and {col}")
                        return True

                    # Check column wise win condition
                    win = True
                    for i in range(consecutive_piece):
                        if (row + i) >= self.board_size or self.board[row + i][col] != self.board[row][col]:
                            win = False
                            break
                    if win:
                        print(f"{self.current_player} won column wise at {row} and {col}")
                        return True

                    # Check right diagonal win condition
                    win = True
                    for i in range(consecutive_piece):
                        if (row + i) >= self.board_size or (col + i) >= self.board_size or self.board[row + i][
                            col + i] != self.board[row][col]:
                            win = False
                            break
                    if win:
                        print(f"{self.current_player} won diagonal wise at {row} and {col}")
                        return True
        return False

