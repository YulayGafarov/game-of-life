'''
Created on Apr 12, 2019

@author: yulay
'''
import random


class Lifegame:

    def __init__(self, ncols, nrows, cell_alive_probability):
        self.ncols = ncols
        self.nrows = nrows
        self.ncells = 0
        self.generation = 0
        self.field = self._get_new_field()
        self.randomize_field(cell_alive_probability)
    
    def randomize_field(self, cell_alive_probability):
        for icol in range(self.ncols):
            for irow in range(self.nrows):
                if random.random() < cell_alive_probability:
                    self.field[icol][irow] = 1 
                    self.ncells += 1
                else :
                    self.field[icol][irow] = 0
    
    def calculate_next_generation(self):
        next_generation_field = self._get_new_field();
        for icol in range(self.ncols):
            for irow in range(self.nrows):
                next_generation_field[icol][irow] = self._will_cell_live_in_next_generation(icol, irow)
                if self.field[icol][irow] == 0 and next_generation_field[icol][irow] == 1:
                    self.ncells += 1
                if self.field[icol][irow] == 1 and next_generation_field[icol][irow] == 0:
                    self.ncells -= 1
        self.field = next_generation_field        
        self.generation += 1
        
    def _get_new_field(self):
        new_field = [0] * self.ncols
        for icol in range(self.ncols):
            new_field[icol] = [0] * self.nrows
        return new_field
    
    def _will_cell_live_in_next_generation(self, icol, irow):
        nneighbours = self._count_neighbours(icol, irow)
        if self.field[icol][irow] == 0:
            if nneighbours == 3:
                return True
            else:
                return False
        if self.field[icol][irow] == 1:
            if nneighbours < 2 or nneighbours > 3:
                return False
            else:
                return True
            
    def _count_neighbours(self, col, row):
        nneighbours = 0
        if self.field[col - 1][row - 1] == 1:
            nneighbours += 1
        if self.field[col][row - 1] == 1:
            nneighbours += 1
        if self.field[(col + 1) % self.ncols][row - 1] == 1:
            nneighbours += 1
        if self.field[col - 1][row] == 1:
            nneighbours += 1
        if self.field[(col + 1) % self.ncols][row] == 1:
            nneighbours += 1
        if self.field[col - 1][(row + 1) % self.nrows] == 1:
            nneighbours += 1
        if self.field[col ][(row + 1) % self.nrows ] == 1:
            nneighbours += 1
        if self.field[(col + 1) % self.ncols][(row + 1) % self.nrows] == 1:
            nneighbours += 1
        return nneighbours
