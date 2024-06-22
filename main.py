from window import Window

def main():
    win = Window(100)
    win.draw_board()
    win.wait_for_close()

main()