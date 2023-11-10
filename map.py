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
    def update(self,MAPHEIGHT, MAPWIDTH, TILESIZE):
        for row in range(MAPHEIGHT): #Rows
            for col in range(MAPWIDTH): #Columns
                DISPLAY.blit(self.Tiles[self.screen[row][col]],(col*TILESIZE,row*TILESIZE))
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
    def update(self, player, CurrentScreen, keys):
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

class Map():
    def __init__(self, DISPLAY):
        self.TILESIZE = 40
        self.TILETYPES = 16
        self.MAPWIDTH = 45
        self.MAPHEIGHT = 24
        self.tiles = TileProperties(self.TILETYPES)
        self.color = GraphicDesign.ColorList()
        self.CurrentScreen = screen(self.tiles, self.MAPWIDTH, self.MAPHEIGHT)
        self.PlayerScreen = [1,5]
        self.DISPLAY = DISPLAY
        self.player = Player(23*TILESIZE,12*TILESIZE,50,50)
        self.collision = CollisionLayer(self.DISPLAY,self.CurrentScreen,self.MAPWIDTH,self.MAPHEIGHT,TILESIZE)
        self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])
    def transition(self):
        if self.player.rect.centerx < 0:
            self.PlayerScreen[0] = self.PlayerScreen[0] - 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Left
            self.player.rect.x = 44 * self.TILESIZE
        elif self.player.rect.centerx > (self.MAPWIDTH * self.TILESIZE):
            self.PlayerScreen[0] = self.PlayerScreen[0] + 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Right
            self.player.rect.x = 1 * self.TILESIZE
        if self.player.rect.centery < 0:
            self.PlayerScreen[1] = self.PlayerScreen[1] + 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Up
            self.player.rect.y = 22 * self.TILESIZE
        elif self.player.rect.centery > (self.MAPHEIGHT * self.TILESIZE):
            self.PlayerScreen[1] = self.PlayerScreen[1] - 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Down
            self.player.rect.y = 1 * self.TILESIZE
        return self.PlayerScreen
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        #Change player position based off input
        self.player.processInput(keys)
        self.player.setDirection(mouse_pos)
        self.PlayerScreen = self.transition()
        #update display
        self.CurrentScreen.update(self.MAPHEIGHT,self.MAPWIDTH,self.TILESIZE)
        pygame.draw.circle(DISPLAY,'red', mouse_pos, 10)
        self.collision.update(self.player,self.CurrentScreen, keys)
        self.player.update(self.DISPLAY,keys)
        pygame.display.update()

FPS = 60
TILESIZE = 40
MAPWIDTH = 45
MAPHEIGHT = 24


#Create Display
pygame.init()
clock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

map = Map(DISPLAY)
#User Interface
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    map.update()