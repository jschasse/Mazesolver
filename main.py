from window import *


def main():
    win = Window(800, 600)
    line = Line(Point(0, 0), Point(400, 330))
    win.draw_line(line, "black")
    win.wait_for_close()
    
    
    
if __name__ == "__main__":
    main()