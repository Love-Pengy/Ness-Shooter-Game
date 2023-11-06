import pygame, sys
from Entities.Entity import *


class screen:
    def __init__(self):
        W = 0 #Water
        C = 1 #Cliff
        G = 2 #Grass
        F = 3 #ForestGrass

        BLUE = (0,0,255)
        BROWN = (150,75,0)
        GRASSGREEN = (124,252,0)
        FORESTGREEN = (0,100,0)

        self.TileColor = {W : pygame.image.load("Map Sprites/Pitfall.png"),
                          C : pygame.image.load("Map Sprites/Valley_Wall.png"),
                          G : pygame.image.load("Map Sprites/Grass.png"),
                          F : pygame.image.load("Map Sprites/Forest_Grass.png")
                        }

        self.map1 = [[C,C,C,C,C,C,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,C,C,C,C,C,C,C,C,C,C,C,C,C],
                     [C,G,G,G,G,G,G,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,F,F,F,F,F,F,F,F,F,F,F,C],
                     [C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C,C]]

TILESIZE = 40
MAPWIDTH = 45
MAPHEIGHT = 24
TestScreen = screen()

#Create Display
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
player = Player(100,100,50,50)
#User Interface
while True:
    for event in pygame.event.get():
        "Quit"
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for row in range(MAPHEIGHT): #Rows
        for col in range(MAPWIDTH): #Columns
            #pygame.draw.rect(DISPLAY,TestScreen.TileColor[TestScreen.map1[row][col]],(col*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
            DISPLAY.blit(TestScreen.TileColor[TestScreen.map1[row][col]],(col*TILESIZE,row*TILESIZE))
 

    keys = pygame.key.get_pressed()
    #Change player position based off input
    player.processInput(keys)
    player.update(DISPLAY)

    #Update Display
    pygame.display.update()
    
    
    
    



