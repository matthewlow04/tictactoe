import pygame
import sys
pygame.init()

#Create display vars
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 6
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

#Create game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Create winner screen
winner_screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Define colors
BLACK = (0, 0, 0)
GREEN = (0,255,0)
WHITE = (255, 255, 255)

#Create the game board
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

#Initialize the player and clicks var
player = 'X'
clicks = 0

#Draw the game board func
def draw_board():
    screen.fill(BLACK)
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(screen, WHITE, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            if board[row][col] == 'X':
                pygame.draw.line(screen, WHITE, (x - 40, y - 40), (x + 40, y + 40), LINE_WIDTH)
                pygame.draw.line(screen, WHITE, (x + 40, y - 40), (x - 40, y + 40), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, WHITE, (x, y), 40, LINE_WIDTH)

def check_win(player):

    #Check rows and columns for win
    for i in range(BOARD_SIZE):
        if board[i] == [player] * BOARD_SIZE:
            return True
        if [board[j][i] for j in range(BOARD_SIZE)] == [player] * BOARD_SIZE:
            return True

    #Check diagonals for
    if [board[i][i] for i in range(BOARD_SIZE)] == [player] * BOARD_SIZE:
        return True
    if [board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)] == [player] * BOARD_SIZE:
        return True

    return False


running = True
game_over = False
winner = None
# Game loop
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if player == 'X':
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // CELL_SIZE
                clicked_col = mouse_x // CELL_SIZE
                if board[clicked_row][clicked_col] == '':
                    clicks += 1
                    board[clicked_row][clicked_col] = player
                    if check_win(player):
                        winner = player
                        game_over = True
                    player = 'O'
                    if clicks == 9:
                         game_over = True
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // CELL_SIZE
                clicked_col = mouse_x // CELL_SIZE
                if board[clicked_row][clicked_col] == '':
                    clicks +=1
                    board[clicked_row][clicked_col] = player
                    if check_win(player):
                        winner = player
                        game_over = True
                    player = 'X'
                    if clicks == 9:
                         game_over = True

    screen.fill(BLACK)
    if not game_over:
        draw_board()
        pygame.display.update()
    else:
        winner_screen.fill(GREEN)
        winner_font = pygame.font.SysFont(None, 48)
        if winner == None:
            winner_text = winner_font.render(f"Draw!", True, BLACK)
        else:
            winner_text = winner_font.render(f"Player {winner} wins!", True, BLACK)
        turns_text = winner_font.render(f"Turns: {clicks}", True, BLACK)
        winner_screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))
        winner_screen.blit(turns_text, (WIDTH // 2 - winner_text.get_width() // 2, (HEIGHT // 2 - winner_text.get_height() // 2) +100))
        pygame.display.flip()
