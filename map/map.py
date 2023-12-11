import pygame, sys, csv
import map.Classes.GraphicDesign as GraphicDesign
from map.Classes.Entity import *


class TileProperties:
    def __init__(self, TILETYPES,TILESIZE):
        self.tile_list = []
        self.IsCollider = []
        self.tile_names = []
        self.Data = open("map/tiles/TileData.txt")
        for x in range(TILETYPES):
            tile = pygame.image.load(f"map/tiles/{x}.png")
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
    def __init__(self, Tile, MAPWIDTH, MAPHEIGHT, DISPLAY):
        self.Tiles = Tile.tile_list
        self.IsCollider = Tile.IsCollider
        self.TILESIZE = 40
        self.screen = []
        self.DISPLAY = DISPLAY
        self.enemies = pygame.sprite.Group()

        for row in range(MAPHEIGHT + 1):
            r = [0] * MAPWIDTH
            self.screen.append(r)

    def LoadEnemies(self,x,y,enemy):
        if enemy == 1:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = SerpentEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 2:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = GolemEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 3:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = GoblinEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 4:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = GhostEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 5:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = DwarfEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 6:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = MushroomEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 7:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = TikiBoss1(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 8:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = TikiBoss2(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 9:
            print(f"Loading enemy at ({x*self.TILESIZE},{y*self.TILESIZE})")
            enemy1 = Boss3(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)

    def load(self,CurrentX,CurrentY):
        print("Now Loading...")
        for enemy in self.enemies:
            self.enemies.remove(enemy)
        with open(f'map/Screens/TileMaps/Screen{CurrentX}{CurrentY}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.screen[x][y] = int(tile)
        with open(f'map/Screens/EnemyMaps/Screen{CurrentX}{CurrentY}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for y, row in enumerate(reader):
                for x, enemy in enumerate(row):
                    self.LoadEnemies(x,y,int(enemy))
                    #self.enemies[x][y] = int(enemy)

    def update(self,MAPHEIGHT, MAPWIDTH, TILESIZE, DISPLAY):
        self.DISPLAY = DISPLAY
        for row in range(MAPHEIGHT): #Rows
            for col in range(MAPWIDTH): #Columns
                self.DISPLAY.blit(self.Tiles[self.screen[row][col]],(col*TILESIZE,row*TILESIZE))

class CollisionLayer():
    def __init__(self, DISPLAY, Currentscreen, width, height,TILESIZE):
        self.display = DISPLAY
        self.screen = Currentscreen
        self.width = width
        self.height = height
        self.Tilesize = TILESIZE
    def DrawCollision(self):
        collideRect = self.screen.Tiles[self.screen.screen[0][0]].get_rect()
        for row in range(self.height): #Rows
            for col in range(self.width): #Columns
                if self.screen.IsCollider[self.screen.screen[row][col]]:
                    collideRect = self.screen.Tiles[self.screen.screen[row][col]].get_rect()
                    collideRect.x = col * self.Tilesize
                    collideRect.y = row * self.Tilesize
                    pygame.draw.rect(self.display, color.RED, collideRect,2)
    def update(self, player, CurrentScreen, keys):
        collideRect = self.screen.Tiles[self.screen.screen[0][0]].get_rect()
        for row in range(self.height):
            for col in range(self.width):
                    if self.screen.IsCollider[self.screen.screen[row][col]]:
                        collideRect = CurrentScreen.Tiles[CurrentScreen.screen[row][col]].get_rect()
                        collideRect.x = col * self.Tilesize
                        collideRect.y = row * self.Tilesize 
                    if collideRect.colliderect(player.rect.x + player.vel_x, player.rect.y, player.rect.width, player.rect.height):
                        player.vel_x = 0
                    if collideRect.colliderect(player.rect.x, player.rect.y + player.vel_y, player.rect.width, player.rect.height):
                        player.vel_y = 0

class Map():
    def __init__(self, player, DISPLAY):
        self.TILESIZE = 40
        self.TILETYPES = 16
        self.MAPWIDTH = 45
        self.MAPHEIGHT = 24
        self.tiles = TileProperties(self.TILETYPES,self.TILESIZE)
        self.color = GraphicDesign.ColorList()
        self.CurrentScreen = screen(self.tiles, self.MAPWIDTH, self.MAPHEIGHT, DISPLAY)
        self.PlayerScreen = [1,5]
        self.DISPLAY = DISPLAY
        self.enemy_group = pygame.sprite.Group()
        self.all_entities = pygame.sprite.Group()

        #self.player = Player(23*TILESIZE,12*TILESIZE,50,50)

        self.player = player

        #self.all_entities.add(self.player,self.enemy1,self.enemy2,self.enemy3)
        #self.enemy_group.add(self.enemy1,self.enemy2,self.enemy3)

        self.collision = CollisionLayer(self.DISPLAY,self.CurrentScreen,self.MAPWIDTH,self.MAPHEIGHT,self.TILESIZE)
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

    def update(self, DISPLAY):
        self.DISPLAY = DISPLAY
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        #Change player position based off input
        self.player.processInput(keys)
        self.player.setDirection(mouse_pos)
        self.PlayerScreen = self.transition()

        #update display
        self.CurrentScreen.update(self.MAPHEIGHT,self.MAPWIDTH,self.TILESIZE, self.DISPLAY)
        pygame.draw.circle(DISPLAY,'red', mouse_pos, 10)
        self.collision.update(self.player,self.CurrentScreen, keys)
        #Sprite group for detecting entity on entity collision
        for sprite in self.all_entities:
            for enemy in self.enemy_group:
                enemy.detectCollision(sprite,self.all_entities)

        #Loop to update all enemies on screen
        for enemy in self.enemy_group:
            enemy.update(self.DISPLAY,self.player)

        #Loop to check bullet on entity collision
        for enemy in self.enemy_group:
            for sprite in self.all_entities:
                temp = sprite.rect.collideobjects(enemy.bullets)
                if(temp  != None):
                    self.all_entities.remove(temp)
                    pygame.sprite.Sprite.remove(bullet)
                

        self.player.update(self.DISPLAY,keys)
        for enemy in self.CurrentScreen.enemies:
            enemy.findPlayer(self.player)
            enemy.followPlayer(self.player)
            enemy.update(self.DISPLAY, self.player)
       
        #pygame.display.update()

FPS = 60