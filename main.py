'''
Created on 12 apr. 2019.

@author: yulay.gafarov
'''
import pygame
from lifegame import Lifegame


class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    CELL_SIZE = 10
    
    def __init__(self):
        self.life = Lifegame(60, 60)
        self.screen_width = self.life.ncols * self.CELL_SIZE
        self.screen_height = self.life.nrows * self.CELL_SIZE
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.end = False
        
    def showState(self):
        self.screen.fill(self.WHITE) 
        for icol in range(self.life.ncols):
            for irow in range(self.life.nrows):
                if self.life.field[icol][irow] == 1:
                    pygame.draw.rect(self.screen, self.BLACK, (icol * self.CELL_SIZE, irow * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE))
        pygame.display.update()
        
    def nextState(self):
        self.life.calculate_next_generation()
    
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
