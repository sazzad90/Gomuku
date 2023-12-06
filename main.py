import pygame
from gomokuGame import GomokuGame
from aiPlayer import AIPlayer

pygame.init()

font = pygame.font.Font(None, 36)  # You can adjust the font size and style as needed

ai_player = AIPlayer(player_marker='B')
window_width = 700
window_height = 700
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gomoku")

background_color = (70, 39, 25)  # RGB values for darker wood color
board_color = (159, 100, 60)  # RGB values for light wood color
black = (0, 0, 0)
white = (255, 255, 255)

board_size = 10
board_cell_size = 40
board_offset = ((window_width - board_size * board_cell_size) // 2, (window_height - board_size * board_cell_size) // 2)

checker_radius = board_cell_size // 2

# Initialize game state
game_board = [['' for _ in range(board_size)] for _ in range(board_size)]
current_player = 0  # 'X' starts the game

# Define reset button dimensions and position
reset_button_width = 100
reset_button_height = 40
reset_button_x = (window_width - reset_button_width) // 2
reset_button_y = window_height - 60  # Adjust the vertical position as needed

# ... (previous code)

# Function to reset the game board
def reset_board():
    global game_board, current_player, matchEnd
    game_board = [['' for _ in range(board_size)] for _ in range(board_size)]
    current_player = 0
    matchEnd = False

if __name__ == "__main__":
    pygame.init()
    # print("Welcome to Gomoku!")
    game = GomokuGame()
    running = True
    matchEnd = False
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if reset_button_x <= mouse_x <= reset_button_x + reset_button_width and \
                reset_button_y <= mouse_y <= reset_button_y + reset_button_height:
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is clicked
                reset_board()  # Call the reset_board function when the reset button is clicked

        # ... (previous code)

        # Draw the reset button
        pygame.draw.rect(screen, (0, 255, 0), (reset_button_x, reset_button_y, reset_button_width, reset_button_height))
        reset_text = font.render("Reset", True, (0, 0, 0))
        text_rect = reset_text.get_rect(center=(reset_button_x + reset_button_width // 2, reset_button_y + reset_button_height // 2))
        screen.blit(reset_text, text_rect)

        if not matchEnd:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and current_player == 0:
                    x, y = event.pos
                    row = (y - board_offset[1]) // board_cell_size
                    col = (x - board_offset[0]) // board_cell_size
                    print(current_player)
                    if 0 <= row < board_size and 0 <= col < board_size and game_board[row][col] == '':
                        game_board[row][col] = current_player
                        if game.make_move(row, col):
                            if game.check_win_condition():
                                print("\n\t" + ("AI WON" if game.current_player == "W" else "Player WON"))
                                matchEnd = True
                                winning_player = "AI" if game.current_player == "W" else "Player"
                                winning_message = f"{winning_player} WON!"
                                text = font.render(winning_message, True, (255, 255, 255))  # You can adjust the color as needed
                                text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
                                screen.blit(text, text_rect)
                        else:
                            print("Invalid move. Try again.")
                    else:
                        continue
                    current_player = not current_player
                    continue

                elif current_player == 1:
                    ai_move = ai_player.make_move(game.board)
                    game_board[ai_move[0]][ai_move[1]] = current_player
                    game.make_move(ai_move[0], ai_move[1])

                    if game.check_win_condition():
                        print("\n\t" + ("AI WON" if game.current_player == "W" else "PLayer WON"))
                        matchEnd = True
                        winning_player = "AI" if game.current_player == "W" else "Player"
                        winning_message = f"{winning_player} WON!"
                        text = font.render(winning_message, True, (255, 255, 255))  # You can adjust the color as needed
                        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
                        screen.blit(text, text_rect)

                    current_player = not current_player


        # Clear the screen
        screen.fill(background_color)

        # Draw the smaller game board
        pygame.draw.rect(screen, board_color,
                         (board_offset[0], board_offset[1], board_size * board_cell_size, board_size * board_cell_size))
        for row in range(board_size):
            for col in range(board_size):
                pygame.draw.rect(screen, white, (
                board_offset[0] + col * board_cell_size, board_offset[1] + row * board_cell_size, board_cell_size,
                board_cell_size), 1)

        # Draw the checkers
        for row in range(board_size):
            for col in range(board_size):
                if game_board[row][col] == 0:
                    pygame.draw.circle(screen, black, (
                    board_offset[0] + col * board_cell_size, board_offset[1] + row * board_cell_size), checker_radius)
                elif game_board[row][col] == 1:
                    pygame.draw.circle(screen, white, (
                    board_offset[0] + col * board_cell_size, board_offset[1] + row * board_cell_size), checker_radius)

        # Update the display
        pygame.display.flip()

    pygame.quit()
