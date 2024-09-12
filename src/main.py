import pygame

from Grid import Grid

pygame.init()

grid = Grid()

screen = pygame.display.set_mode((440, 440))
pygame.display.set_caption('2048')
screen.fill((187, 173, 160))

def isGameOver():
    for row in range(grid.size):
        for col in range(grid.size):
            if(grid.tiles[row][col] is None 
                or (row > 0 and grid.tiles[row][col].value == grid.tiles[row - 1][col].value)
                or (col > 0 and grid.tiles[row][col].value == grid.tiles[row][col - 1].value)):
                    return False
    return True

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            playing = False
        elif event.type == pygame.KEYDOWN:
            grid.moveTiles()
            
    grid.drawGrid(screen, tileSize=100, tileMargin=10)
    
    if isGameOver():
        overlay = pygame.Surface((440, 440))
        overlay.set_alpha(128)
        overlay.fill((187, 173, 160))
        screen.blit(overlay, (0, 0))
        
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over', True, (119, 110, 101))
        text_rect = text.get_rect(center=(220, 220))
        screen.blit(text, text_rect)
    
    pygame.display.update()

pygame.quit()