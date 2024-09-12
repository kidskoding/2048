import pygame

from Grid import Grid

pygame.init()

grid = Grid()

screenSize = grid.gridSize * grid.tileSize + (grid.gridSize + 1) * grid.tileMargin
screen = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption('2048')
screen.fill((187, 173, 160))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            
    grid.drawGrid(screen)
    pygame.display.update()

pygame.quit()