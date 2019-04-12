'''
Created on 12 apr. 2019.

@author: yulay.gafarov
'''
import pygame


def calculate():
    pass


def show():
    pass


if __name__ == '__main__':
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (125, 125, 125)
    LIGHT_BLUE = (64, 128, 255)
    GREEN = (0, 200, 64)
    YELLOW = (225, 225, 0)
    PINK = (230, 50, 230)
    
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    
    radius = 100
    inc = 1
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        screen.fill(WHITE) 
        pygame.draw.circle(screen, (64, 128, 255), (300, 300), radius, 4)
        radius += inc
        if(radius > 200):
            inc = -1
        if(radius == 5):
            inc = 1
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
