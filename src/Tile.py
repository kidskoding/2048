import pygame

tileColors = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

class Tile:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.size = 100
        self.margin = 10
        self.x = col * (self.size + self.margin) + self.margin
        self.y = row * (self.size + self.margin) + self.margin
        self.fontSize = 55
        
    def drawTile(self, screen):
        if tileColors.get(self.value) is None: 
            raise ValueError('Invalid tile value. Must pick a value that is a power of 2!')
        
        color = tileColors.get(self.value)
        
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size), 0)
        
        font = pygame.font.Font(None, self.fontSize)
        text = font.render(str(self.value), True, (255, 255, 255) if self.value > 4 else (119, 110, 101))
        text_rect = text.get_rect(center=(self.x + self.size / 2, self.y + self.size / 2))
        
        screen.blit(text, text_rect)
        
    def moveTile(self, newRow, newCol):
        self.row = newRow
        self.col = newCol
        self.x = self.col * (self.size + self.margin) + self.margin
        self.y = self.row * (self.size + self.margin) + self.margin