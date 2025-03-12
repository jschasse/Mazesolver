from window import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 40, 30, 10, 10, win)
    maze.solve()
    win.wait_for_close()
    
    
    
if __name__ == "__main__":
    main()