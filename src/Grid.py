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
        
    def getTileAt(self, row, col):
        for tile in self.tiles:
            if tile.row == row and tile.col == col:
                return tile
        return None