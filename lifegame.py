'''
Created on Apr 12, 2019

@author: yulay
'''
import random
import math


class Lifegame:

    def __init__(self, ncols, nrows, cell_alive_probability):
        self.ncols = ncols
        self.nrows = nrows
        self.generation = 0
        self.alive_cells = []
        self.cells_with_alive_neighbour = []
        self.field = self._get_empty_field()
        self._set_random_init_field(cell_alive_probability)

    def _set_random_init_field(self, cell_alive_probability):
        for icol in range(self.ncols):
            for irow in range(self.nrows):
                if self._cell_alive_with_probability(cell_alive_probability):
                    self.field[icol][irow] = 1 
                    self.alive_cells.append((icol, irow))
                    self.cells_with_alive_neighbour.extend(self._get_neighbours(icol, irow))
                else :
                    self.field[icol][irow] = 0
        self._count_neighbours()
        
    def _cell_alive_with_probability(self, cell_alive_probability):
        return random.random() < cell_alive_probability

    def set_next_generation_field(self):
        n_alive_cells = len(self.alive_cells)
        if self.nrows * self.ncols <= 9 * n_alive_cells * math.log(n_alive_cells, 2) or False:
            self._set_next_generation_by_loop_all_cells()
        else :
            self._set_next_generation_by_loop_alive_cells()
        self.generation += 1
        self._count_neighbours()
        
    def _set_next_generation_by_loop_all_cells(self):
        field_next_generation = self._get_empty_field()
        alive_cells_next_generation = []
        for icol in range(self.ncols):
            for irow in range(self.nrows):
                field_next_generation[icol][irow] = self._will_cell_live_in_next_generation(icol, irow)
                if (field_next_generation[icol][irow] == 1):
                    alive_cells_next_generation.append((icol, irow))
        self.field = field_next_generation
        self.alive_cells = alive_cells_next_generation
        
    def _set_next_generation_by_loop_alive_cells(self):
        field_next_generation = self._get_empty_field()
        alive_cells_next_generation = []
        checked_cells = set()
        for cell in self.alive_cells:
            icol = cell[0]
            irow = cell[1]
            neighbours = self._get_neighbours(icol, irow)
            for neighbour in neighbours:
                if neighbour not in checked_cells:
                    icol = neighbour[0]
                    irow = neighbour[1]
                    field_next_generation[icol][irow] = self._will_cell_live_in_next_generation(icol, irow)
                    if(field_next_generation[icol][irow] == 1):
                        alive_cells_next_generation.append((icol, irow))
                    checked_cells.add((icol, irow))
        self.field = field_next_generation
        self.alive_cells = alive_cells_next_generation
    
    def _will_cell_live_in_next_generation(self, icol, irow):
        nneighbours = self.nneighbours[icol][irow]
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

    def _count_neighbours(self):
        self.nneighbours = self._get_empty_neighbours_counter()
        for cell in self.alive_cells:
            col = cell[0]
            row = cell[1]
            self.nneighbours[col - 1][row - 1] += 1
            self.nneighbours[col][row - 1] += 1
            self.nneighbours[(col + 1) % self.ncols][row - 1] += 1
            self.nneighbours[col - 1][row] += 1
            self.nneighbours[(col + 1) % self.ncols][row] += 1
            self.nneighbours[col - 1][(row + 1) % self.nrows] += 1
            self.nneighbours[col][(row + 1) % self.nrows] += 1
            self.nneighbours[(col + 1) % self.ncols][(row + 1) % self.nrows] += 1
            
    def _get_empty_field(self):
        new_field = [0] * self.ncols
        for icol in range(self.ncols):
            new_field[icol] = [0] * self.nrows
        return new_field

    def _get_empty_neighbours_counter(self):
        return self._get_empty_field()

    def _get_neighbours(self, col, row):
        neighbours = []
        neighbours.append(((col - 1 + self.ncols) % self.ncols, (row - 1 + self.nrows) % self.nrows))
        neighbours.append((col , (row - 1 + self.nrows) % self.nrows))
        neighbours.append(((col + 1) % self.ncols, (row - 1 + self.nrows) % self.nrows))
        neighbours.append(((col - 1 + self.ncols) % self.ncols, row))
        neighbours.append((col, row))
        neighbours.append(((col + 1) % self.ncols, row))
        neighbours.append(((col - 1 + self.ncols) % self.ncols, (row + 1) % self.nrows))
        neighbours.append((col , (row + 1) % self.nrows))
        neighbours.append(((col + 1) % self.ncols, (row + 1) % self.nrows))
        return neighbours
