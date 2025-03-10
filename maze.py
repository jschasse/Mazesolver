from cell import *
from time import *

class Maze():
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.create_cells()
        
    def create_cells(self):
        for i in range(0, self.num_cols):
            cols = []
            for j in range(0, self.num_rows):
                x1_pos = self.x1 + (i * self.cell_size_x)
                y1_pos = self.y1 + (j * self.cell_size_y)
                x2_pos = x1_pos + self.cell_size_x
                y2_pos = y1_pos + self.cell_size_y
                cols.append(Cell(Point(x1_pos, y1_pos), Point(x2_pos, y2_pos), self.win)) 
            self.cells.append(cols)
            
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.draw_cell(i, j)


                
    def draw_cell(self, i, j):
        self.cells[i][j].draw("black")
        self.animate()
        
    def animate(self):
        self.win.redraw()
        sleep(0.05)
        
            
            
                
                