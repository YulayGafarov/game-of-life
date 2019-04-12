'''
Created on 12 apr. 2019.

@author: yulay.gafarov
'''
import pygame
from lifegame import Lifegame


class LifeGameVisualizer:
    CELL_COLOR = (69, 139, 0)
    SCREEN_COLOR = (255, 255, 255)
    BLACK = (0, 0, 0)
    CELL_SIZE = 16
    
    def __init__(self):
        self.life = Lifegame(60, 60, 0.2)
        self.screen_width = self.life.ncols * self.CELL_SIZE
        self.screen_height = self.life.nrows * self.CELL_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.end = False
        
    def showState(self):
        self._drawBackground()
        for icol in range(self.life.ncols):
            for irow in range(self.life.nrows):
                if self.life.field[icol][irow] == 1:
                    self._drawCell(icol, irow)
        pygame.display.update()
        pygame.display.set_caption('generation: ' + str(self.life.generation) + ', cells: ' + str(self.life.ncells))
    
    def _drawBackground(self):
        self.screen.fill(self.SCREEN_COLOR)
        for icol in range(self.life.ncols):
            pygame.draw.line(self.screen, self.BLACK, (icol * self.CELL_SIZE, 0), (icol * self.CELL_SIZE, self.screen_height))
        for irow in range(self.life.nrows):
            pygame.draw.line(self.screen, self.BLACK, (0, irow * self.CELL_SIZE), (self.screen_width, irow * self.CELL_SIZE))
    
    def _drawCell(self, icol, irow):
        pygame.draw.circle(self.screen, self.CELL_COLOR, (icol * self.CELL_SIZE + int(self.CELL_SIZE / 2), irow * self.CELL_SIZE + int(self.CELL_SIZE / 2)), int(self.CELL_SIZE / 2))
#         pygame.draw.rect(self.screen, self.CELL_COLOR, (icol * self.CELL_SIZE, irow * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        
    def nextState(self):
        self.life.calculate_next_generation()
    
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end = True
    
    def run(self, ticks):
        clock = pygame.time.Clock()
        while not self.end:
            self.showState()
            self.nextState()
            self.processEvents()
            clock.tick(ticks)
        pygame.quit()


if __name__ == '__main__':
    visualizer = LifeGameVisualizer()
    visualizer.run(10)
