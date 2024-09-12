import pygame

from Grid import Grid

pygame.init()

grid = Grid()

dim = 440

screen = pygame.display.set_mode((dim, dim))
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
        overlay = pygame.Surface((dim, dim))
        overlay.set_alpha(150)
        overlay.fill((187, 173, 160))
        screen.blit(overlay, (0, 0))
        
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over!', True, (119, 110, 101))
        text_rect = text.get_rect(center=(dim / 2, dim / 2 - 70))
        screen.blit(text, text_rect)
        
        rect_width = 200
        rect_height = 50
        rect_font = pygame.font.Font(None, 36)
        
        play_again_rect = pygame.Rect(dim / 2 - rect_width / 2, dim / 2 - 20, rect_width, rect_height)
        text = rect_font.render('Play Again', True, (255, 255, 255))
        text_rect = text.get_rect(center=play_again_rect.center)
        pygame.draw.rect(screen, (143, 122, 102), play_again_rect)
        screen.blit(text, text_rect)
        
        quit_rect = pygame.Rect(dim / 2 - rect_width / 2, dim / 2 + 50, rect_width, rect_height)
        text = rect_font.render('Quit', True, (255, 255, 255))
        text_rect = text.get_rect(center=quit_rect.center)
        pygame.draw.rect(screen, (143, 122, 102), quit_rect)
        screen.blit(text, text_rect)
        
    pygame.display.update()

pygame.quit()