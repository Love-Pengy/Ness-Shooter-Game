import pygame
import sys
import csv

class TileProperties:
    def __init__(self, TILETYPES):
        self.tile_list = []
        for x in range(TILETYPES):
            tile = pygame.image.load(f"tiles/{x}.png")
            self.tile_list.append(tile)