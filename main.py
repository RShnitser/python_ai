# import pygame, sys
# from pygame.locals import *
import pyray as rl
from game import *

player1_mode = rl.ffi.new("int *", 0)
player2_mode = rl.ffi.new("int *", 0)

def update_main_menu(state: GameState, dt: float) ->None:
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)

    if rl.gui_button(rl.Rectangle(24, 24, 120, 30), "Play"):
        state.screen = SCREEN_GAME

    rl.gui_toggle_group(rl.Rectangle(24, 64, 120, 30), "Human;Random;Neural Network", player1_mode)
    state.players[0].mode = player1_mode[0]

    rl.gui_toggle_group(rl.Rectangle(24, 104, 120, 30), "Human;Random;Neural Network", player2_mode)
    state.players[1].mode = player2_mode[0]
    
    rl.end_drawing()

def update_game(state: GameState, dt: float) ->None:
    if rl.is_mouse_button_down(rl.MouseButton.MOUSE_BUTTON_LEFT):
        if state.players[state.current_player].mode == PLAYER_MODE_HUMAN:
            m_x = rl.get_mouse_x() // CELL_SIZE
            set_column(state, m_x, state.players[state.current_player].id)

    if state.players[state.current_player].mode != PLAYER_MODE_HUMAN:
        ai_move(state, state.players[state.current_player].id, dt)
    
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)

    for y in range(BOARD_H):
        for x in range(BOARD_W):
            l = x * CELL_SIZE
            t = y * CELL_SIZE
        
            rl.draw_rectangle(l, t, CELL_SIZE, CELL_SIZE, rl.GRAY)

            v = get_cell(state, x, y)
            col = rl.DARKGRAY
            if v == ID_P1:
                col = rl.Color(0, 0, 255, 255)
            elif v == ID_P2:
                col = rl.Color(255, 0, 0, 255)
            m = CELL_SIZE * .2
        
            rl.draw_rectangle_rounded(rl.Rectangle(l + m, t + m, CELL_SIZE - 2 * m, CELL_SIZE - 2 * m), 1.0, 3, col)
            rl.draw_text(f"{x},{y}", int(l +m ), int(t + m), 15, rl.BLACK)

    line_thickness = 4
    half_thickness = 2
    rl.draw_line_ex(rl.Vector2(half_thickness, 0), rl.Vector2(half_thickness, CELL_SIZE * BOARD_H), line_thickness, rl.BLACK)
    rl.draw_line_ex(rl.Vector2(0, half_thickness), rl.Vector2(CELL_SIZE * BOARD_W, half_thickness), line_thickness, rl.BLACK)

    for y in range(1, BOARD_H + 1):
        rl.draw_line_ex(rl.Vector2(0, CELL_SIZE * y - half_thickness), rl.Vector2(CELL_SIZE * BOARD_W, CELL_SIZE * y - half_thickness), line_thickness, rl.BLACK)
    for x in range(1, BOARD_W + 1):
        rl.draw_line_ex(rl.Vector2(CELL_SIZE * x - half_thickness, 0), rl.Vector2(CELL_SIZE * x - half_thickness, CELL_SIZE * BOARD_H), line_thickness, rl.BLACK)

    rl.end_drawing()

def main() -> None:

 
    rl.init_window(BOARD_W * CELL_SIZE, BOARD_H * CELL_SIZE, "Connect Four AI")
    rl.set_target_fps(30)

    state = init_game_state()

    while not rl.window_should_close():
        dt = rl.get_frame_time()
       
        if state.screen == SCREEN_MENU:
            update_main_menu(state, dt)
        elif state.screen == SCREEN_GAME:
            update_game(state, dt)

if __name__ == "__main__":
    main()