import pygame
import sys
import csv

class TileProperties:
    def __init__(self, TILETYPES):
        self.tile_list = []
        for x in range(TILETYPES):
            tile = pygame.image.load(f"tiles/{x}.png")
            self.tile_list.append(tile)
        #def TileProperties(self, ):
class screen(TileProperties):
    def __init__(self, Tile, MAPWIDTH, MAPHEIGHT):

        self.TileColor = Tile.tile_list

        self.screen = []
        for row in range(MAPHEIGHT + 1):
            r = [0] * MAPWIDTH
            self.screen.append(r)

        with open('map/Screen0.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.screen[x][y] = int(tile)

TILESIZE = 40
TILETYPES = 4
MAPWIDTH = 45
MAPHEIGHT = 24
tiles = TileProperties(TILETYPES)
screens = []

TestScreen = screen(tiles, MAPWIDTH, MAPHEIGHT)


#Create Display
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#User Interface
while True:
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for row in range(MAPHEIGHT): #Rows
        for col in range(MAPWIDTH): #Columns

            #pygame.draw.rect(DISPLAY,TestScreen.TileColor[TestScreen.map1[row][col]],(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            DISPLAY.blit(TestScreen.TileColor[TestScreen.screen[row][col]],(col*TILESIZE,row*TILESIZE))
    #Update Display
    pygame.display.update()