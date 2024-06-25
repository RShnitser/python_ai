from tkinter import Tk, CENTER, Canvas
import numpy as np

BOARD_COLS = 7
BOARD_ROWS = 6

class Window:
    def __init__(self, cell_size):
        self.__root = Tk()
        self.__root.geometry(f"{8*cell_size}x{7*cell_size}")
        self.__root.title("Connect Four")
        self.__canvas = Canvas(self.__root, bg="white", height=BOARD_ROWS * cell_size, width=BOARD_COLS * cell_size)
        self.__canvas.pack(anchor=CENTER, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas.bind("<Button-1>", self.click_column)
        self.__cell_size = cell_size
        self.__board = np.full(BOARD_COLS * BOARD_ROWS, 0)
        self.__player_id = 1

    
    def set_cell(self, x, y, v):
        self.__board[y * BOARD_ROWS + x] = v

    def get_cell(self, x, y):
        result = self.__board[y * BOARD_ROWS + x]
        return result
    
    def check_game_over(self, x, y, player_id):
        count = 0
        for col in range(BOARD_COLS):
            v = self.get_cell(col, y)
            if v == player_id:
                count += 1
            else:
                count = 0
        if count >= 4:
            return True
        
        count = 0
        for row in range(BOARD_ROWS):
            v = self.get_cell(x, row)
            if v == player_id:
                count += 1
            else:
                count = 0
        if count >= 4:
            return True
    
        return False
        
    def click_column(self, event):
        x = event.x // self.__cell_size
        for y in range(BOARD_ROWS - 1, -1, -1):
            if self.get_cell(x, y) == 0:
                self.set_cell(x, y, self.__player_id)
                if self.__player_id == 1:
                    self.__player_id = 2
                else:
                    self.__player_id = 1
                self.draw_board()
                return

    def draw_board(self):
        for y in range(BOARD_ROWS):
            for x in range(BOARD_COLS):
                l = x * self.__cell_size
                t = y * self.__cell_size
                r = l + self.__cell_size
                b = t + self.__cell_size
                self.__canvas.create_rectangle(l, t, r, b, width=5, fill="gray70")

                v = self.get_cell(x, y)
                col = "gray"
                if v == 1:
                    col = "blue"
                elif v == 2:
                    col = "red"
                m = self.__cell_size * .2
                self.__canvas.create_oval(l + m, t + m, r - m, b - m, fill=col, width=2)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False