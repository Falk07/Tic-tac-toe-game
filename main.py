import pygame
import sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = 300
GRID_SIZE = WINDOW_SIZE // 3
LINE_WIDTH = 15
CIRCLE_RADIUS = GRID_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = GRID_SIZE // 4
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Tic Tac Toe')

board = [[None] * 3 for _ in range(3)]
player = 'X'
game_over = False

def draw_lines():
    
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, GRID_SIZE * i), (WINDOW_SIZE, GRID_SIZE * i), LINE_WIDTH)
    
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (GRID_SIZE * i, 0), (GRID_SIZE * i, WINDOW_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (int(col * GRID_SIZE + GRID_SIZE // 2), int(row * GRID_SIZE + GRID_SIZE // 2)), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * GRID_SIZE + SPACE, row * GRID_SIZE + GRID_SIZE - SPACE), 
                                 (col * GRID_SIZE + GRID_SIZE - SPACE, row * GRID_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * GRID_SIZE + SPACE, row * GRID_SIZE + SPACE), 
                                 (col * GRID_SIZE + GRID_SIZE - SPACE, row * GRID_SIZE + GRID_SIZE - SPACE), CROSS_WIDTH)

def check_win(player):
  
    for row in range(3):
        if all([spot == player for spot in board[row]]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                return False
    return True

def restart_game():
    global board, player, game_over
    board = [[None] * 3 for _ in range(3)]
    player = 'X'
    game_over = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // GRID_SIZE
            clicked_col = mouseX // GRID_SIZE
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    game_over = True
                elif check_draw():
                    game_over = True
                player = 'O' if player == 'X' else 'X'
        if event.type == KEYDOWN:
            if event.key == K_r:
                restart_game()

    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()
    pygame.display.update()
