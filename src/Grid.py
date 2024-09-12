import pygame
import random
from Tile import Tile

class Grid:
    def __init__(self):
        self.size = 4
        self.gridLineColor = (204, 192, 179)
        self.tiles = [[None for _ in range(self.size)] for _ in range(self.size)]
        
        self.initializeGrid()
        
    def initializeGrid(self):
        self.addRandomTile()
        self.addRandomTile()
        
    def drawGrid(self, screen, tileSize, tileMargin):
        for row in range(self.size):
            for col in range(self.size):
                x = col * (tileSize + tileMargin) + tileMargin
                y = row * (tileSize + tileMargin) + tileMargin
                
                pygame.draw.rect(screen, self.gridLineColor, (x, y, tileSize, tileSize), 0)
                
        for tileRow in self.tiles:
            for tile in tileRow:
                if tile is not None:
                    tile.drawTile(screen)
                    
    def getTileAt(self, row, col):
        for tileRow in self.tiles:
            for tile in tileRow:
                if tile != None and tile.row == row and tile.col == col:
                    return tile
        return None
                
    def addRandomTile(self):
        empty_positions = [(row, col) for row in range(self.size) for col in range(self.size) if self.tiles[row][col] is None]
        if empty_positions:
            row, col = random.choice(empty_positions)
            tile = Tile(2, row, col)
            self.addTile(tile)
            
    def addTile(self, tile):
        self.tiles[tile.row][tile.col] = tile
        tile.x = tile.col * (tile.size + tile.margin) + tile.margin
        tile.y = tile.row * (tile.size + tile.margin) + tile.margin
    
    def moveTiles(self):
        keys = pygame.key.get_pressed()
        tileHasMoved = False
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            for col in range(len(self.tiles)):
                for row in range(1, len(self.tiles)):
                    tile = self.tiles[row][col]
                    if tile is not None:
                        while row > 0 and self.tiles[row - 1][col] is None:
                            self.tiles[row - 1][col] = tile
                            self.tiles[row][col] = None
                            tile.moveTile(row - 1, col)
                            row -= 1
                            tileHasMoved = True
                        if row > 0 and self.tiles[row - 1][col].value == tile.value:
                            self.mergeTiles(self.tiles[row - 1][col], tile)
                            tile.moveTile(row - 1, col)
                            tileHasMoved = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            for col in range(len(self.tiles)):
                for row in range(len(self.tiles) - 2, -1, -1):
                    tile = self.tiles[row][col]
                    if tile is not None:
                        while row < self.size - 1 and self.tiles[row + 1][col] is None:
                            self.tiles[row + 1][col] = tile
                            self.tiles[row][col] = None
                            tile.moveTile(row + 1, col)
                            row += 1
                            tileHasMoved = True
                        if row < self.size - 1 and self.tiles[row + 1][col].value == tile.value:
                            self.mergeTiles(self.tiles[row + 1][col], tile)
                            tile.moveTile(row + 1, col)
                            tileHasMoved = True
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            for row in range(len(self.tiles)):
                for col in range(1, len(self.tiles)):
                    tile = self.tiles[row][col]
                    if tile is not None:
                        while col > 0 and self.tiles[row][col - 1] is None:
                            self.tiles[row][col - 1] = tile
                            self.tiles[row][col] = None
                            tile.moveTile(row, col - 1)
                            col -= 1
                            tileHasMoved = True
                        if col > 0 and self.tiles[row][col - 1].value == tile.value:
                            self.mergeTiles(self.tiles[row][col - 1], tile)
                            tile.moveTile(row, col - 1)
                            tileHasMoved = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            for row in range(len(self.tiles)):
                for col in range(len(self.tiles) - 2, -1, -1):
                    tile = self.tiles[row][col]
                    if tile is not None:
                        while col < self.size - 1 and self.tiles[row][col + 1] is None:
                            self.tiles[row][col + 1] = tile
                            self.tiles[row][col] = None
                            tile.moveTile(row, col + 1)
                            col += 1
                            tileHasMoved = True
                        if col < self.size - 1 and self.tiles[row][col + 1].value == tile.value:
                            self.mergeTiles(self.tiles[row][col + 1], tile)
                            tile.moveTile(row, col + 1)
                            tileHasMoved = True
        if tileHasMoved:
            self.addRandomTile()
            tileHasMoved = False
        
    def mergeTiles(self, tile1, tile2):
        tile1 = Tile(tile1.value * 2, tile1.row, tile1.col)
        self.tiles[tile1.row][tile1.col] = tile1
        self.tiles[tile2.row][tile2.col] = None