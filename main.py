'''
Created on 12 apr. 2019.

@author: yulay.gafarov
'''
import pygame
import random


class Life:
    NROWS = 90
    NCOLS = 90

    def __init__(self):
        self.ncells = 0
        self.step = 0
        self.field = [0] * self.NCOLS
        for icol in range(self.NCOLS):
            self.field[icol] = [0] * self.NROWS
        self.randomizeField()
            
    def randomizeField(self):
        for icol in range(self.NCOLS):
            for irow in range(self.NROWS):
                value = random.randint(0, 30)
                self.field[icol][irow] = 1 if value == 0 else 0
    
    def printField(self):
        for icol in range(self.NCOLS):
            print(self.field[icol])
    
    def count_next_step(self):
        for icol in range(self.NCOLS):
            for irow in range(self.NROWS):
                nneighbours = self._countNeighbours(icol, irow)
                if self.field[icol][irow] == 0 and nneighbours == 3:
                    self.field[icol][irow] = 1
                if self.field[icol][irow] == 1 and (nneighbours < 2 or nneighbours > 3):
                    self.field[icol][irow] = 0
            
    def _countNeighbours(self, col, row):
        counterNeighbours = 0
        if self.field[col - 1][row - 1] == 1:
            counterNeighbours += 1
        if self.field[col][row - 1] == 1:
            counterNeighbours += 1
        if self.field[(col + 1) % (self.NCOLS - 1)][row - 1] == 1:
            counterNeighbours += 1
        if self.field[col - 1][row] == 1:
            counterNeighbours += 1
        if self.field[(col + 1) % (self.NCOLS - 1)][row] == 1:
            counterNeighbours += 1
        if self.field[col - 1][(row + 1) % (self.NROWS - 1)] == 1:
            counterNeighbours += 1
        if self.field[col ][(row + 1) % (self.NROWS - 1)] == 1:
            counterNeighbours += 1
        if self.field[(col + 1) % (self.NCOLS - 1)][(row + 1) % (self.NROWS - 1)] == 1:
            counterNeighbours += 1
        return counterNeighbours


class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    CELL_SIZE = 10
    
    def __init__(self):
        self.life = Life()
        self.screen_width = self.life.NCOLS * self.CELL_SIZE
        self.screen_height = self.life.NROWS * self.CELL_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.end = False
        
    def showState(self):
        self.screen.fill(self.WHITE) 
        for icol in range(self.life.NCOLS):
            for irow in range(self.life.NROWS):
                if self.life.field[icol][irow] == 1:
                    pygame.draw.rect(self.screen, self.BLACK, (icol * self.CELL_SIZE, irow * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        pygame.display.update()
        
    def nextState(self):
        self.life.count_next_step()
    
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end = True
    
    def run(self):
        clock = pygame.time.Clock()
        while not self.end:
            self.showState()
            self.nextState()
            self.processEvents()
            clock.tick(1)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
