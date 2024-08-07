import numpy as np
import numpy.typing as npt

BOARD_W = 7
BOARD_H = 6
CELL_SIZE = 100
FPS = 60
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GRAY = (150, 150, 150)
# DARK_GRAY = (80, 80, 80)
# BLACK = (0, 0, 0, 0)
AI_DELAY = 0.5

ID_E = 0
ID_P1 = 1
ID_P2 = 2

SCREEN_MENU = 0
SCREEN_GAME = 1

PLAYER_MODE_HUMAN = 0
PLAYER_MODE_RANDOM = 1
PLAYER_MODE_NETWORK = 2

class Player:
    id: int
    mode: int
    win_count: int

class GameState:
    board: npt.NDArray[np.int32]
    players: list[Player]
    current_player: int
    moves_left: int
    ai_delay: float
    screen: int
    test: int

def init_game_state()-> GameState:
    player1 = Player()
    player1.id = ID_P1
    player1.is_ai = False
    player1.win_count = 0

    player2 = Player()
    player2.id = ID_P2
    player2.is_ai = True
    player2.win_count = 0

    state = GameState()
    state.board = np.zeros(BOARD_W * BOARD_H, dtype=np.int32)
    state.players = [player1, player2]
    state.current_player = 0
    state.moves_left = BOARD_W * BOARD_H
    state.ai_delay = AI_DELAY
    state.screen = SCREEN_MENU

   

    return state

def set_cell(state: GameState, x: int, y: int, v: int)-> None:
        state.board[y * BOARD_W + x] = v

def get_cell(state: GameState, x: int, y: int)-> int:
        result = state.board[y * BOARD_W + x]
        return result

def check_game_over(state: GameState, x: int, y: int, player_id: int)->tuple[bool, int]:
        count = 0
        for col in range(BOARD_W):
            v = get_cell(state, col, y)
            if v == player_id:
                count += 1
            else:
                count = 0
            if count >= 4:
                return True, player_id
        
        count = 0
        for row in range(BOARD_H):
            v = get_cell(state, x, row)
            if v == player_id:
                count += 1
            else:
                count = 0
            if count >= 4:
                return True, player_id
        
        count = 0
        curr_x = 0
        curr_y = 0
        if x > BOARD_H - 1 - y:
            curr_x = x - (BOARD_H - y - 1)
            curr_y = BOARD_H - 1
        else:
            curr_x = 0
            curr_y = y + x
        while curr_x < BOARD_W and curr_y < BOARD_H:
            v = get_cell(state, curr_x, curr_y)
            if v == player_id:
                count += 1
            else:
                count = 0
            curr_x += 1
            curr_y -= 1
            if count >= 4:
                return True, player_id
        
        count = 0
        curr_x = 0
        curr_y = 0
        if y > x:
            curr_x = 0
            curr_y = y - x
        else:
            curr_x = x - y
            curr_y = 0
        while curr_x < BOARD_W and curr_y < BOARD_H:
            v = get_cell(state, curr_x, curr_y)
            if v == player_id:
                count += 1
            else:
                count = 0
            curr_x += 1
            curr_y += 1
            if count >= 4:
                return True, player_id

        if state.moves_left == 0:
            return True, 0
        return False, 0

def get_empty_cols(state: GameState)-> list[int]:
    result = [i for i in range(BOARD_W) if get_cell(state, i, 0) == ID_E]
    return result
    
def reset_board(state: GameState)-> None:
    for i in range(len(state.board)):
        state.board[i] = 0
    state.current_player = 0
    state.moves_left = BOARD_W * BOARD_H
    state.ai_delay = AI_DELAY

def set_column(state: GameState, x: int, player_id: int)-> None:
    if x < 0 or x >= BOARD_W:
        return
    
    for y in range(BOARD_H - 1, -1, -1):
        if get_cell(state, x, y) == 0:
            set_cell(state, x, y, player_id)
            state.moves_left -= 1
            gameover_result = check_game_over(state, x, y, player_id)
            if gameover_result[0]:
                if gameover_result[1] != ID_E:
                    state.players[state.current_player].win_count += 1
                reset_board(state)
                return

            if state.current_player == 0:
                state.current_player = 1
            else:
                state.current_player = 0
            return
        
def ai_move(state: GameState, player_id: int, dt: float)-> None:
    if state.ai_delay <= 0:
        cols = get_empty_cols(state)
        col = cols[np.random.randint(len(cols))]
        set_column(state, col, player_id)
        state.ai_delay = AI_DELAY
    state.ai_delay -= dt