from window import *
from cell import *

def main():
    win = Window(800, 600)
    #line = Line(Point(0, 0), Point(400, 330))
    #win.draw_line(line, "black")
    cell = Cell(Point(100, 100), Point(200, 200), win)
    cell2 = Cell(Point(300, 300), Point(400, 400), win)
    cell.has_top_wall = False
    cell.has_bottom_wall = False
    cell.has_right_wall = True
    cell.has_left_wall = False
    cell2.has_top_wall = False
    cell2.has_bottom_wall = False
    cell2.has_right_wall = False
    cell2.has_left_wall = True
    cell.draw("black")
    cell2.draw("black")
    cell.draw_move(cell2, undo=True)
    win.wait_for_close()
    
    
    
if __name__ == "__main__":
    main()