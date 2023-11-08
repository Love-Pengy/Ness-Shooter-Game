import pygame, sys, csv
import Classes.GraphicDesign as GraphicDesign
from Entity import *

class TileProperties:
    def __init__(self, TILETYPES):
        self.tile_list = []
        self.IsCollider = []
        self.tile_names = []
        self.Data = open("tiles/TileData.txt")
        for x in range(TILETYPES):
            tile = pygame.image.load(f"tiles/{x}.png")
            tiletransform = pygame.transform.scale(tile,(TILESIZE,TILESIZE))
            self.tile_list.append(tiletransform)
            self.Collision()
        self.Data.close()

 #Running Collision Checks if a tiletype is supposed to have collision and stores it in IsCollider
    def Collision(self):
        CurrentTileProperties = self.Data.readline()
        TileData = CurrentTileProperties.split()
        self.tile_names.append(TileData[0])
        self.IsCollider.append(int(TileData[1]))
class screen(TileProperties):
    def __init__(self, Tile, MAPWIDTH, MAPHEIGHT):
        self.Tiles = Tile.tile_list
        self.IsCollider = Tile.IsCollider
        self.screen = []
        
        for row in range(MAPHEIGHT + 1):
            r = [0] * MAPWIDTH
            self.screen.append(r)
    def load(self,CurrentX,CurrentY):
        print("Now Loading...")
        with open(f'map/Screen{CurrentX}{CurrentY}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.screen[x][y] = int(tile)
        print("Load Complete!")
class CollisionLayer():
    def __init__(self, DISPLAY, Currentscreen, width, height,TILESIZE):
        self.display = DISPLAY
        self.screen = Currentscreen
        self.width = width
        self.height = height
        self.Tilesize = TILESIZE
    def DrawCollision(self):
        collideRect = self.screen.Tiles[CurrentScreen.screen[0][0]].get_rect()
        for row in range(self.height): #Rows
            for col in range(self.width): #Columns
                if self.screen.IsCollider[self.screen.screen[row][col]]:
                    collideRect = CurrentScreen.Tiles[CurrentScreen.screen[row][col]].get_rect()
                    collideRect.x = col * TILESIZE
                    collideRect.y = row * TILESIZE
                    pygame.draw.rect(self.display, color.RED, collideRect,2)
    def update(self, player, keys):
        collideRect = self.screen.Tiles[self.screen.screen[0][0]].get_rect()
        for row in range(self.height):
            for col in range(self.width):
                    if self.screen.IsCollider[self.screen.screen[row][col]]:
                        collideRect = CurrentScreen.Tiles[CurrentScreen.screen[row][col]].get_rect()
                        collideRect.x = col * TILESIZE
                        collideRect.y = row * TILESIZE 
                    if collideRect.colliderect(player.rect.x + player.vel_x, player.rect.y, player.rect.width, player.rect.height):
                        player.vel_x = 0
                    if collideRect.colliderect(player.rect.x, player.rect.y + player.vel_y, player.rect.width, player.rect.height):
                        player.vel_y = 0
def transition(player, screen, PlayerScreen, MAPWIDTH, MAPHEIGHT,TILESIZE):
    if player.rect.centerx < 0:
        PlayerScreen[0] = PlayerScreen[0] - 1
        screen.load(PlayerScreen[0],PlayerScreen[1])#Transitions Left
        player.rect.x = 43 * TILESIZE
        player.rect.y = 12 * TILESIZE
    elif player.rect.centerx > (MAPWIDTH * TILESIZE):
        PlayerScreen[0] = PlayerScreen[0] + 1
        screen.load(PlayerScreen[0],PlayerScreen[1])#Transitions Right
        player.rect.x = 2 * TILESIZE
        player.rect.y = 12 * TILESIZE
    if player.rect.centery < 0:
        PlayerScreen[1] = PlayerScreen[1] + 1
        screen.load(PlayerScreen[0],PlayerScreen[1])#Transitions Up
        player.rect.x = 23 * TILESIZE
        player.rect.y = 22 * TILESIZE
    elif player.rect.centery > (MAPHEIGHT * TILESIZE):
        PlayerScreen[1] = PlayerScreen[1] - 1
        screen.load(PlayerScreen[0],PlayerScreen[1])#Transitions Down
        player.rect.x = 23 * TILESIZE
        player.rect.y = 2 * TILESIZE
    return PlayerScreen

TILESIZE = 40
TILETYPES = 15
MAPWIDTH = 45
MAPHEIGHT = 24
tiles = TileProperties(TILETYPES)
color = GraphicDesign.ColorList()
CurrentScreen = screen(tiles, MAPWIDTH, MAPHEIGHT)
PlayerScreen = [5,5]
CurrentScreen.load(PlayerScreen[0],PlayerScreen[1])


#Create Display
pygame.init()

DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
collision = CollisionLayer(DISPLAY,CurrentScreen,MAPWIDTH,MAPHEIGHT,TILESIZE)
player = Player(23*TILESIZE,12*TILESIZE,50,50)
#User Interface
while True:
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for row in range(MAPHEIGHT): #Rows
        for col in range(MAPWIDTH): #Columns
            DISPLAY.blit(CurrentScreen.Tiles[CurrentScreen.screen[row][col]],(col*TILESIZE,row*TILESIZE))
    mouse_pos = pygame.mouse.get_pos()
    #Change player position based off input
    keys = pygame.key.get_pressed()
    player.processInput(keys)
    player.setDirection(mouse_pos)
    pygame.draw.circle(DISPLAY,'red', mouse_pos, 10)

    PlayerScreen = transition(player,CurrentScreen,PlayerScreen,MAPWIDTH,MAPHEIGHT,TILESIZE)
    #Update Display
    collision.update(player, keys)
    player.update(DISPLAY, keys)#Player.rect.center
    pygame.display.update()