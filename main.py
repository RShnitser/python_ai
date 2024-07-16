# import pygame, sys
# from pygame.locals import *
import pyray as rl
from game import *

def main() -> None:

    # pygame.init()
    # screen = pygame.display.set_mode((BOARD_W * CELL_SIZE, BOARD_H * CELL_SIZE))
    # pygame.display.set_caption("Connect Four AI")
    # font = pygame.font.Font(pygame.font.get_default_font(), 15)
    # timer = pygame.time.Clock()
    # running = True
    rl.init_window(BOARD_W * CELL_SIZE, BOARD_H * CELL_SIZE, "Connect Four AI")
    rl.set_target_fps(30)

    state = init_game_state()

    # while running:
    while not rl.window_should_close():
        # timer.tick(FPS)
        # dt = timer.get_time() * 0.001
        # screen.fill("white")
        dt = rl.get_frame_time()
       
        # for e in pygame.event.get():
        #     if e.type == pygame.QUIT:
        #         running = False
        #     if e.type == pygame.MOUSEBUTTONDOWN:
        #          buttons = pygame.mouse.get_pressed()
        #          if buttons[0]:
        #             if state.players[state.current_player].is_ai == False:
        #                 m_pos = pygame.mouse.get_pos()
        #                 m_x = m_pos[0] // CELL_SIZE
        #                 set_column(state, m_x, state.players[state.current_player].id)

        if rl.is_mouse_button_down(rl.MouseButton.MOUSE_BUTTON_LEFT):
             if state.players[state.current_player].is_ai == False:
                # m_pos = rl.get_mouse_position()
                # m_x = int(m_pos.x // CELL_SIZE)
                m_x = rl.get_mouse_x() // CELL_SIZE
                set_column(state, m_x, state.players[state.current_player].id)

        if state.players[state.current_player].is_ai == True:
            ai_move(state, state.players[state.current_player].id, dt)
        
        rl.begin_drawing()
        rl.clear_background(rl.WHITE)

        for y in range(BOARD_H):
            for x in range(BOARD_W):
                l = x * CELL_SIZE
                t = y * CELL_SIZE
            
                # pygame.draw.rect(screen, GRAY, [l, t, CELL_SIZE, CELL_SIZE], 0)
                # pygame.draw.rect(screen, BLACK, [l, t, CELL_SIZE, CELL_SIZE], 2)
                rl.draw_rectangle(l, t, CELL_SIZE, CELL_SIZE, rl.GRAY)
                # rl.draw_rectangle_lines_ex(rl.Rectangle(l, t, CELL_SIZE, CELL_SIZE), 2, rl.BLACK)

                v = get_cell(state, x, y)
                # col = DARK_GRAY
                col = rl.DARKGRAY
                if v == ID_P1:
                    # col = BLUE
                    # col = rl.BLUE
                    col = rl.Color(0, 0, 255, 255)
                elif v == ID_P2:
                    # col = RED
                    # col = rl.RED
                    col = rl.Color(255, 0, 0, 255)
                m = CELL_SIZE * .2
            
                rl.draw_rectangle_rounded(rl.Rectangle(l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m), 1.0, 3, col)
                # rl.draw_rectangle_rounded_lines(rl.Rectangle(l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m), 1.0, 3, 10, rl.BLACK)
                # pygame.draw.ellipse(screen, col, [l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m], 0)
                # pygame.draw.ellipse(screen, BLACK, [l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m], 2)
                # text_render = font.render(f"{x},{y}", True, BLACK)
                # screen.blit(text_render, (l + m, t + m))
                rl.draw_text(f"{x},{y}", int(l +m ), int(t + m), 15, rl.BLACK)
    
        line_thickness = 4
        half_thickness = 2
        rl.draw_line_ex(rl.Vector2(half_thickness, 0), rl.Vector2(half_thickness, CELL_SIZE * BOARD_H), line_thickness, rl.BLACK)
        rl.draw_line_ex(rl.Vector2(0, half_thickness), rl.Vector2(CELL_SIZE * BOARD_W, half_thickness), line_thickness, rl.BLACK)

        for y in range(1, BOARD_H + 1):
            rl.draw_line_ex(rl.Vector2(0, CELL_SIZE * y - half_thickness), rl.Vector2(CELL_SIZE * BOARD_W, CELL_SIZE * y - half_thickness), line_thickness, rl.BLACK)
        for x in range(1, BOARD_W + 1):
            rl.draw_line_ex(rl.Vector2(CELL_SIZE * x - half_thickness, 0), rl.Vector2(CELL_SIZE * x - half_thickness, CELL_SIZE * BOARD_H), line_thickness, rl.BLACK)
        # rl.draw_line_ex(rl.Vector2(CELL_SIZE * BOARD_W - half_thickness, 0), rl.Vector2(CELL_SIZE * BOARD_W - half_thickness, CELL_SIZE * BOARD_H), line_thickness, rl.BLACK)

        rl.end_drawing()
        # pygame.display.flip()
    # pygame.quit()
    # sys.exit()

if __name__ == "__main__":
    main()