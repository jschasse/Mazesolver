from window import *
from line import *


class Cell():
    def __init__(self, point_a, point_b, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = point_a.x
        self.y1 = point_a.y
        self.x2 = point_b.x
        self.y2 = point_b.y
        self.middle = Point(((abs(point_b.x - point_a.x))//2) + self.x1, (abs((point_b.y - point_a.y))//2) + self.y1)
        self.win = win
        self.visited = False
        
    def draw(self, fill_color):
        if self.has_left_wall == True:
            left = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(left, fill_color)
        else:
            left = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(left, "white")
            
        if self.has_right_wall == True:
            right = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(right, fill_color)
        else:
            right = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(right, "white")
            
        if self.has_top_wall == True:
            top = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(top, fill_color)
        else:
            top = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(top, "white")
            
        if self.has_bottom_wall == True:
            bottom = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bottom, fill_color)
        else:
            bottom = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bottom, "white")
    
    def draw_move(self, to_cell, undo=False):
        if undo == True:
            line = Line(self.middle, to_cell.middle)
            self.win.draw_line(line, "gray")
        else:
            line = Line(self.middle, to_cell.middle)
            self.win.draw_line(line, "red")      
            