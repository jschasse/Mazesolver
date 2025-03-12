from cell import *
from time import *
import random

class Maze():
    
    def __init__(self, _x1, _y1, _num_rows, _num_cols, _cell_size_x, _cell_size_y, _win=None, seed=None):
        self._x1 = _x1
        self._y1 = _y1
        self._num_rows = _num_rows
        self._num_cols = _num_cols
        self._cell_size_x = _cell_size_x
        self._cell_size_y = _cell_size_y
        self._win = _win
        self._cells = []
        if seed != None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        for i in range(0, self._num_cols):
            cols = []
            for j in range(0, self._num_rows):
                x1_pos = self._x1 + (i * self._cell_size_x)
                y1_pos = self._y1 + (j * self._cell_size_y)
                x2_pos = x1_pos + self._cell_size_x
                y2_pos = y1_pos + self._cell_size_y
                cols.append(Cell(Point(x1_pos, y1_pos), Point(x2_pos, y2_pos), self._win)) 
            self._cells.append(cols)
            
        for i in range(0, self._num_cols):
            for j in range(0, self._num_rows):
                self._draw_cell(i, j)


                
    def _draw_cell(self, i, j):
        self._cells[i][j].draw("black")
        self._animate()
        
    def _animate(self):
        self._win.redraw()
        sleep(0.05)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i + 1, j))
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j + 1))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if len(to_visit) == 0:
                self._cells[i][j].draw("black")
                return
            
            
            direction = random.randrange(len(to_visit))
            next_ind = to_visit[direction]
            

            if next_ind[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif next_ind[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            elif next_ind[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            elif next_ind[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                
            self._break_walls_r(next_ind[0], next_ind[1])
            
            
        
    def solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        if i < self._num_cols - 1 and not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self.solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
                
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self.solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
                
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self.solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
                
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self.solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
                
        return False
    
    def solve(self):
        return self.solve_r(0, 0)
                

            
            
                
                