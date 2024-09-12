import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('2048')
screen.fill((250, 248, 239))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            
    pygame.display.update()

pygame.quit()