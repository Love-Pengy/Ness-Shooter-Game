import pygame, sys, csv
import map.Classes.GraphicDesign as GraphicDesign
from map.Classes.Entity import *


class TileProperties:
    def __init__(self, TILETYPES,TILESIZE):
        self.tile_list = []
        self.IsCollider = []
        self.IsPitfall = []
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
        self.IsPitfall.append(int(TileData[2]))

class screen(TileProperties):
    def __init__(self, Tile, MAPWIDTH, MAPHEIGHT, DISPLAY):
        self.Tiles = Tile.tile_list
        self.IsCollider = Tile.IsCollider
        self.IsPitfall = Tile.IsPitfall
        self.TILESIZE = 40
        self.screen = []
        self.DISPLAY = DISPLAY
        self.enemies = pygame.sprite.Group()
        self.all_entities = pygame.sprite.Group()
        for row in range(MAPHEIGHT + 1):
            r = [0] * MAPWIDTH
            self.screen.append(r)

    def LoadEnemies(self,x,y,enemy):
        if enemy == 1:
            enemy1 = SerpentEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 2:
            enemy1 = GolemEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 3:
            enemy1 = GoblinEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 4:
            enemy1 = GhostEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 5:
            enemy1 = DwarfEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 6:
            enemy1 = MushroomEnemy(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 7:
            enemy1 = TikiBoss1(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 8:
            enemy1 = TikiBoss2(x*self.TILESIZE,y*self.TILESIZE,50,50)
            self.enemies.add(enemy1)
        if enemy == 9:
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

    def update(self,MAPHEIGHT, MAPWIDTH, TILESIZE, DISPLAY,player):

        self.all_entities = self.enemies.copy()
        self.all_entities.add(player)

        for sprite in self.all_entities:
            for enemy in self.enemies:
                enemy.detectCollision(sprite,self.all_entities)

       #Loop to update all enemies on screen
        for enemy in self.enemies:
            enemy.update(self.DISPLAY,player)

        #Loop to check bullet on entity collision           
        for enemy in self.enemies:

            for sprite in self.all_entities:

                #Despawn if hp hits 0
                if(sprite.hp <= 0):
                    self.enemies.remove(sprite)
                    if(sprite.isDead == False):
                        player.score += sprite.score
                    sprite.isDead = True
                  
                print(player.hp)
                if(player.hp <= 0):
                    print("GAME OVER")
                    exit()

                temp = sprite.rect.collideobjects(enemy.bullets)
                temp2 = sprite.rect.collideobjects(player.bullets)
                if(temp is not None and sprite != enemy):
                    sprite.damageCalc(temp)
                    for element in enemy.bullets: 
                        if(element is temp): 
                            enemy.bullets.remove(temp)
                elif(temp2 is not None and sprite is not player): 
                    sprite.damageCalc(temp2)
                    for element in player.bullets: 
                        if(element is temp2): 
                            player.bullets.remove(temp2)
        


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
        self.LastTransition = 3
        self.tiles = TileProperties(self.TILETYPES,self.TILESIZE)
        self.color = GraphicDesign.ColorList()
        self.CurrentScreen = screen(self.tiles, self.MAPWIDTH, self.MAPHEIGHT, DISPLAY)
        self.PlayerScreen = [1,5]
        self.DISPLAY = DISPLAY
        self.player = player

        self.collision = CollisionLayer(self.DISPLAY,self.CurrentScreen,self.MAPWIDTH,self.MAPHEIGHT,self.TILESIZE)
        self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])

    def transition(self):
        if self.player.rect.centerx < 0:
            self.PlayerScreen[0] = self.PlayerScreen[0] - 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Left
            self.player.rect.x = 44 * self.TILESIZE
            self.LastTransition = 3
        elif self.player.rect.centerx > (self.MAPWIDTH * self.TILESIZE):
            self.PlayerScreen[0] = self.PlayerScreen[0] + 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Right
            self.player.rect.x = 1 * self.TILESIZE
            self.LastTransition = 1
        if self.player.rect.centery < 0:
            self.PlayerScreen[1] = self.PlayerScreen[1] + 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Up
            self.player.rect.y = 21 * self.TILESIZE
            self.LastTransition = 2
        elif self.player.rect.bottom > (self.MAPHEIGHT * self.TILESIZE) - 1:
            self.PlayerScreen[1] = self.PlayerScreen[1] - 1
            self.CurrentScreen.load(self.PlayerScreen[0],self.PlayerScreen[1])#Transitions Down
            self.player.rect.y = 1 * self.TILESIZE
            self.LastTransition = 4
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
        self.CurrentScreen.update(self.MAPHEIGHT,self.MAPWIDTH,self.TILESIZE, self.DISPLAY,self.player)
        pygame.draw.circle(DISPLAY,'red', mouse_pos, 10)
        self.collision.update(self.player,self.CurrentScreen, keys)
   
        #Detects if player is above pitfalls  
        playerposx = int(self.player.rect.x / self.TILESIZE)
        playerposy = int(self.player.rect.bottom / self.TILESIZE)
        if playerposy > 24:
            playerposy = 24
        if playerposx > 45:
            playerposx = 45
        if self.CurrentScreen.IsPitfall[self.CurrentScreen.screen[playerposy][playerposx]] == 1:
                if self.LastTransition == 1:
                    self.player.rect.x = 1 * self.TILESIZE
                    self.player.rect.y = 12 * self.TILESIZE
                if self.LastTransition == 2:
                    self.player.rect.x = 22 * self.TILESIZE
                    self.player.rect.y = 20 * self.TILESIZE
                if self.LastTransition == 3:
                    self.player.rect.x = 42 * self.TILESIZE
                    self.player.rect.y = 12 * self.TILESIZE
                if self.LastTransition == 4:
                    self.player.rect.x = 22 * self.TILESIZE
                    self.player.rect.y = 2 * self.TILESIZE
        self.player.update(self.DISPLAY,keys)
        for enemy in self.CurrentScreen.enemies:
            enemy.findPlayer(self.player)
            enemy.followPlayer(self.player)
            enemy.update(self.DISPLAY, self.player)
       
        #pygame.display.update()

FPS = 60
