import pygame

from Grid import Grid
from Tile import Tile

pygame.init()

grid = Grid()

screen = pygame.display.set_mode((440, 440))
pygame.display.set_caption('2048')
screen.fill((187, 173, 160))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            playing = False
            
    grid.drawGrid(screen, tileSize=100, tileMargin=10)
    
    pygame.display.update()

pygame.quit()