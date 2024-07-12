import pygame, sys
from pygame.locals import *
from game import *


def process_input_state(button: ButtonState, is_down: bool):
    if button.is_down != is_down:
        button.is_down = is_down
        button.was_changed = True

def main():


    pygame.init()
    screen = pygame.display.set_mode((BOARD_W * CELL_SIZE, BOARD_H * CELL_SIZE))
    pygame.display.set_caption("Connect Four AI")
    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    timer = pygame.time.Clock()
    running = True

    state = GameState()
    input = GameInput()

    while running:
        timer.tick(FPS)
        input.dt = timer.get_time() * 0.001
        screen.fill("white")

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            #if e.type == pygame.MOUSEBUTTONDOWN:
        m_pos = pygame.mouse.get_pos()
        input.mouse_x = m_pos[0]
        buttons = pygame.mouse.get_pressed()
        process_input_state(input.mouse_left, buttons[0])
                # if buttons[0]:
                    # input.mouse_left.is_down = True
                    # if state.players[state.current_player].is_ai == False:
                    #     m_pos = pygame.mouse.get_pos()
                    #     m_x = m_pos[0] // CELL_SIZE
                    #     set_column(state, m_x, state.players[state.current_player].id)

        update(state, input)

        for y in range(BOARD_H):
            for x in range(BOARD_W):
                l = x * CELL_SIZE
                t = y * CELL_SIZE
            
                pygame.draw.rect(screen, GRAY, [l, t, CELL_SIZE, CELL_SIZE], 0)
                pygame.draw.rect(screen, BLACK, [l, t, CELL_SIZE, CELL_SIZE], 2)

                v = get_cell(state, x, y)
                col = DARK_GRAY
                if v == ID_P1:
                    col = BLUE
                elif v == ID_P2:
                    col = RED
                m = CELL_SIZE * .2
            
                pygame.draw.ellipse(screen, col, [l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m], 0)
                pygame.draw.ellipse(screen, BLACK, [l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m], 2)
                text_render = font.render(f"{x},{y}", True, BLACK)
                screen.blit(text_render, (l + m, t + m))
        input.mouse_left.was_changed = False

        pygame.display.flip()
    pygame.quit()
    sys.exit()

main()