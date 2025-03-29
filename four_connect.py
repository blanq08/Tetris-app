import pygame
import sys
import math

#Constants
WHITE=(255, 255, 255)
RED = (225, 83, 47)
BLUE=(72, 156, 183)
GREEN=(196, 222, 164)

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS= int(SQUARE_SIZE / 2-5)

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
    return -1

def drop_pice(board,row,col,piece):
    board[row][col]= piece
def print_board(board):
    for row in board:
        print(row)
    print("__________")

def creat_board(ROW_COUNT, COLUMN_COUNT):
    board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
    return board

def draw_board(board,screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, GREEN, (
                c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, WHITE, (int(c * SQUARE_SIZE+RADIUS), int(r * SQUARE_SIZE+RADIUS*3)), (RADIUS))


    for x in range(ROW_COUNT):
        for y in range(COLUMN_COUNT):
            if board[x][y] == 1:
                pygame.draw.circle(screen, BLUE, (int(y * SQUARE_SIZE+RADIUS), (ROW_COUNT + 1) * SQUARE_SIZE-int(x * SQUARE_SIZE+RADIUS)-SQUARE_SIZE/5), (RADIUS))
            elif board[x][y] == 2:
                pygame.draw.circle(screen, RED, (int(y * SQUARE_SIZE+RADIUS), (ROW_COUNT + 1) * SQUARE_SIZE-int(x * SQUARE_SIZE+RADIUS)-SQUARE_SIZE/5), (RADIUS))

    pygame.display.update()
def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT - 2):
            if board[r][c] == piece and board[r + 1][c+1] == piece and board[r + 2][c+2] == piece and board[r + 3][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT - 2):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def draw_upper_row(screen, width, turn):
    pygame.draw.rect(screen, WHITE, (0, 0, width, SQUARE_SIZE))
    x = pygame.mouse.get_pos()

    if turn == 1:
        pygame.draw.circle(screen, BLUE, (x[0], RADIUS), RADIUS)
    else:
        pygame.draw.circle(screen, RED, (x[0], RADIUS), RADIUS)
    pygame.display.update()

def main():
    # game logic
    pygame.init()
    game_over= False
    width = COLUMN_COUNT * SQUARE_SIZE
    height = (ROW_COUNT + 1) * SQUARE_SIZE
    screen = pygame.display.set_mode([width,height])
    screen.fill(WHITE)

    #Set title
    pygame.display.set_caption("Connect Four")

    # Create game board
    board = creat_board(ROW_COUNT, COLUMN_COUNT)
    turn = 1

    # font for game over message
    font = pygame.font.SysFont('Comic Sans', 75)
    draw_board(board, screen)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                # pygame.draw.rect(screen, WHITE, (0, 0, width, SQUARE_SIZE))
                # x=pygame.mouse.get_pos()
                #
                # if turn == 1:
                #     pygame.draw.circle(screen, BLUE, (x[0], RADIUS), RADIUS)
                # else:
                #     pygame.draw.circle(screen, RED, (x[0], RADIUS), RADIUS)
                # pygame.display.update()
                draw_upper_row(screen, width, turn)

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = pygame.mouse.get_pos()[0]
                col= posx // SQUARE_SIZE

                open_row=get_next_open_row(board,col)
                drop_pice(board,open_row,col,turn)

                turn = 1 if turn == 2 else 2
                print_board(board)
                draw_board(board,screen)
                draw_upper_row(screen, width, turn)
            if winning_move(board, 1 if turn == 2 else 2):
                print(f"player {1 if turn == 2 else 2} wins!")
                game_over = True




main()