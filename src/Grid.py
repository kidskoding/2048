import pygame

class Grid:
    def __init__(self):
        self.gridSize = 4
        self.tileSize = 100
        self.tileMargin = 10
        self.gridLineColor = (204, 192, 179) 
        
    def drawGrid(self, screen):
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                x = col * (self.tileSize + self.tileMargin) + self.tileMargin
                y = row * (self.tileSize + self.tileMargin) + self.tileMargin
                
                pygame.draw.rect(screen, self.gridLineColor, (x, y, self.tileSize, self.tileSize), 0)