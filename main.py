#from window import Window
import pygame, sys
import numpy as np
from pygame.locals import *

BOARD_W = 7
BOARD_H = 6
CELL_SIZE = 100
FPS = 60
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (80, 80, 80)
BLACK = (0, 0, 0, 0)

class GameState:
    def __init__(self):
         self.board = np.full(BOARD_W * BOARD_H, 0)

def get_cell(state, x, y):
        result = state.board[y * BOARD_W + x]
        return result

def main():


    pygame.init()
    screen = pygame.display.set_mode((BOARD_W * CELL_SIZE, BOARD_H * CELL_SIZE))
    pygame.display.set_caption("Connect Four AI")
    timer = pygame.time.Clock()
    #win = Window(100)
    #win.draw_board()
    #win.wait_for_close()
    running = True

    state = GameState()

    while running:
        timer.tick(FPS)
        dt = timer.get_time() * 0.001
        screen.fill("white")


        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        for y in range(BOARD_H):
            for x in range(BOARD_W):
                l = x * CELL_SIZE
                t = y * CELL_SIZE
                #r = l + CELL_SIZE
                #b = t + CELL_SIZE
                #self.__canvas.create_rectangle(l, t, r, b, width=5, fill="gray70")
                pygame.draw.rect(screen, GRAY, [l, t, CELL_SIZE, CELL_SIZE], 0)
                pygame.draw.rect(screen, BLACK, [l, t, CELL_SIZE, CELL_SIZE], 2)

                v = get_cell(state, x, y)
                col = DARK_GRAY
                if v == 1:
                    col = BLUE
                elif v == 2:
                    col = RED
                m = CELL_SIZE * .2
                #self.__canvas.create_oval(l + m, t + m, r - m, b - m, fill=col, width=2)
                pygame.draw.ellipse(screen, col, [l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m], 0)
                pygame.draw.ellipse(screen, BLACK, [l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m], 2)
                #self.__canvas.create_text(l + m, t + m, text=f"{x},{y}", fill="black", font=("Helvetica 15 bold"))

        pygame.display.flip()
    pygame.quit()
    sys.exit()

main()