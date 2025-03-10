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
        self.middle = Point((point_a.x + point_b.x)/2, (point_a.y + point_b.y)/2)
        self.win = win
        
    def draw(self, fill_color):
        if self.has_left_wall == True:
            left = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(left, fill_color)
        
        if self.has_right_wall == True:
            right = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(right, fill_color)
        
        if self.has_top_wall == True:
            top = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(top, fill_color)
        
        if self.has_bottom_wall == True:
            bottom = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bottom, fill_color)
    
    def draw_move(self, to_cell, undo=False):
        if undo == True:
            line = Line(self.middle, to_cell.middle)
            self.win.draw_line(line, "gray")
        else:
            line = Line(self.middle, to_cell.middle)
            self.win.draw_line(line, "red")      
            