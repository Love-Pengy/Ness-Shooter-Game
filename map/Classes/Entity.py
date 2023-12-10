import pygame
import math
import time

class Entity(pygame.sprite.Sprite):
    """
    Parent class of all game entities including the 
    player, enemies, and in-game objects. Entity
    provides a movement interface for all entities, 
    along with a base to build functionality of animated
    sprites for the player and enemies.
    """

    def __init__(self,x,y,width,height):

        #constructor for the pygame Sprite class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        #Velocity of entity movement for testing
        self.vel_x = 5
        self.vel_y = 5

        self.rect = self.image.get_rect()
    
    def moveX(self,x_vel):
        self.rect.x += x_vel

    def moveY(self,y_vel):
        self.rect.y += y_vel

    def update(self,window):
        """Stub function to be implemented by 
           inherited classes. Updates the entities sprites,
           actions, and position when called.
        """
        pass

class Player(Entity):
    """
    Class for the player entity. Handles
    animation of the player sprite, and provides
    an interface for attacking enemies.
    """
    
    def __init__(self,x,y,width,height):

        #constructor for the pygame Sprite class
        super().__init__(x,y,width,height)
      
        #Instantiate class to handle sprite animation
        self.player_anims = SpriteAnimation("Entities/ness_spritesheet.png")

        #Load individual sprites into animation dict
        self.player_anims.registerAnim("walk_down1",self.player_anims.getFrame(0,0,64,100))
        self.player_anims.registerAnim("walk_down2" ,self.player_anims.getFrame(-68,0,64,100))
        self.player_anims.registerAnim("walk_right1",self.player_anims.getFrame(-160,0,64,100))
        self.player_anims.registerAnim("walk_right2",self.player_anims.getFrame(-230,0,64,100))
        self.player_anims.registerAnim("walk_se1",self.player_anims.getFrame(-324,0,64,100))
        self.player_anims.registerAnim("walk_se2",self.player_anims.getFrame(-400,0,64,100))
        self.player_anims.registerAnim("walk_ne1",self.player_anims.getFrame(-568,0,64,100))
        self.player_anims.registerAnim("walk_ne2",self.player_anims.getFrame(-486,0,64,100))
        self.player_anims.registerAnim("walk_up1",self.player_anims.getFrame(0,-120,64,100))
        self.player_anims.registerAnim("walk_up2",self.player_anims.getFrame(-74,-120,64,100))
        self.player_anims.registerAnim("walk_left1",self.player_anims.getFrame(-160,-120,64,100))
        self.player_anims.registerAnim("walk_left2",self.player_anims.getFrame(-230,-120,64,100))
        self.player_anims.registerAnim("walk_sw1",self.player_anims.getFrame(-328,-120,64,100))
        self.player_anims.registerAnim("walk_sw2",self.player_anims.getFrame(-400,-120,64,100))
        self.player_anims.registerAnim("walk_nw1",self.player_anims.getFrame(-490,-120,64,100))
        self.player_anims.registerAnim("walk_nw2",self.player_anims.getFrame(-570,-120,64,100))
    
        self.image = self.player_anims.frames["walk_down1"] #initial sprite
    
        #player velocity 
        self.vel_x = 0
        self.vel_y = 0

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


    def update(self,window, key):
         window.blit(self.image, self.rect)
         if key[pygame.K_a]: 
            self.moveX(self.vel_x)
         if key[pygame.K_d]:
           # self.image = self.player_anims.frames["walk_right1"]
            self.moveX(self.vel_x)
         if key[pygame.K_w]:
            self.moveY(self.vel_y)
         if key[pygame.K_s]:
            #self.image = self.player_anims.frames["walk_down1"]
            self.moveY(self.vel_y)
    

    def setDirection(self,mouse_pos):
        """
        Function to determine mouse position
        relative to the player in order to determine 
        correct sprite and direction for aiming
        """

        x = mouse_pos[0] - self.rect.centerx
        y = mouse_pos[1] - self.rect.centery

        #Direction player is aiming in degrees 
        player_dir = (math.degrees(math.atan2(-y,x)) + 360) % 360

        #Direction player is facing split into 8 directions to determine correct sprite     
        player_facing = int(player_dir / 45)

        if player_facing == 0:
            self.image = self.player_anims.frames["walk_right1"] if self.player_anims.next else self.player_anims.frames["walk_right2"]
        elif player_facing == 1:
            self.image = self.player_anims.frames["walk_ne1"] if self.player_anims.next else self.player_anims.frames["walk_ne2"]
        elif player_facing == 2:
            self.image = self.player_anims.frames["walk_up1"] if self.player_anims.next else self.player_anims.frames["walk_up2"]
        elif player_facing == 3:
            self.image = self.player_anims.frames["walk_nw1"] if self.player_anims.next else self.player_anims.frames["walk_nw2"]
        elif player_facing == 4:
            self.image = self.player_anims.frames["walk_left1"] if self.player_anims.next else self.player_anims.frames["walk_left2"]
        elif player_facing == 5:
            self.image = self.player_anims.frames["walk_sw1"] if self.player_anims.next else self.player_anims.frames["walk_sw2"]
        elif player_facing == 6:
            self.image = self.player_anims.frames["walk_down1"] if self.player_anims.next else self.player_anims.frames["walk_down2"]
        elif player_facing == 7:
            self.image = self.player_anims.frames["walk_se1"] if self.player_anims.next else self.player_anims.frames["walk_se2"]
   
    def processInput(self, pressed):
    #    if pressed[pygame.K_w]or pressed[pygame.K_a] or pressed[pygame.K_s] or pressed[pygame.K_d]:
     #       self.player_anims.nextAnim()
#
 #       if pressed[pygame.K_w]:
  #          self.moveY(self.vel_y * -1)
   #         if pressed[pygame.K_d]:
    #           self.moveX(self.vel_x)
     #       elif pressed[pygame.K_a]:
      #         self.moveX(-1 * self.vel_x)
       # if pressed[pygame.K_s]:
        #    self.moveY(self.vel_y)
         #   if pressed[pygame.K_d]:
          #     self.moveX(self.vel_x)
           # elif pressed[pygame.K_a]:
            #   self.moveX(-1 * self.vel_x)
#        if pressed[pygame.K_a]: 
 #           self.moveX(-1 * self.vel_x)
  #      if pressed[pygame.K_d]:
   #         self.moveX(self.vel_x)   
        if pressed[pygame.K_a]:
            self.player_anims.nextAnim() 
            self.vel_x = -5
        if pressed[pygame.K_d]:
            self.player_anims.nextAnim()
            self.vel_x = 5
        if pressed[pygame.K_w]:
            self.player_anims.nextAnim()
            self.vel_y = -5
        if pressed[pygame.K_s]:
            self.player_anims.nextAnim()
            self.vel_y = 5
        
class SerpentEnemy(Entity):

    def __init__(self,x,y,width,height):
        #constructor for the pygame Sprite class
        super().__init__(x,y,width,height)
      
        #Instantiate class to handle sprite animation
        self.enemy_anim = SpriteAnimation("Entities/Serpent.gif")

        self.image = self.enemy_anim.getFrame(0,0,96,96)
        self.image =  pygame.transform.rotate(self.image, 90) #Rotates sprite image to initially face player
        self.image.set_colorkey((0,0,0)) 
        self.direction = 0

        #Entity velocity 
        self.vel_x = 2
        self.vel_y = 2

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def findPlayer(self, player):
        #Finds the angle the enemy is relative to the player
        x = self.rect.centerx - player.rect.centerx
        y = self.rect.centery - player.rect.centery
        self.direction = (math.degrees(math.atan2(-y,x)) + 360) % 360
  
    def followPlayer(self, player):

        x = player.rect.centerx - self.rect.centerx
        y = player.rect.centery - self.rect.centery

        distance = math.hypot(x,y)

        if distance > 100: #If too close to player, stop movement
            x /= distance
            y /= distance
        else:              
            x = 0
            y = 0

        self.moveX(x * self.vel_x)
        self.moveY(y * self.vel_y)

    def update(self,window):
        rotated_image = pygame.transform.rotate(self.image, self.direction)
        rotated_image.set_colorkey((0,0,0))
        rotated_rect = rotated_image.get_rect()
        rotated_rect.x, rotated_rect.y = self.rect.x,self.rect.y
        window.blit(rotated_image,rotated_rect)

class GolemEnemy(Entity):

    def __init__(self,x,y,width,height):
        #constructor for the pygame Sprite class
        super().__init__(x,y,width,height)
      
        #Instantiate class to handle sprite animation
        self.enemy_anims = SpriteAnimation("Entities/golem.png")
      
        self.enemy_anims.registerAnim(0,pygame.transform.scale(self.enemy_anims.getFrame(0,0,15,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(1,pygame.transform.scale(self.enemy_anims.getFrame(-20,0,15,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(2,pygame.transform.scale(self.enemy_anims.getFrame(-35,0,15,27), (width * 1.5, height * 1.7)))

        self.image = self.enemy_anims.frames[0]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[1]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[2]
        self.image.set_colorkey((0,0,0)) 
       
        self.direction = 0

        #Entity velocity 
        self.vel_x = 2
        self.vel_y = 2

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def findPlayer(self, player):
        #Finds the angle the enemy is relative to the player
        x = self.rect.centerx - player.rect.centerx
        y = self.rect.centery - player.rect.centery
        self.direction = (math.degrees(math.atan2(-y,x)) + 360) % 360
  
    def followPlayer(self, player):

        x = player.rect.centerx - self.rect.centerx
        y = player.rect.centery - self.rect.centery

        distance = math.hypot(x,y)

        if distance > 100: #If too close to player, stop movement
            x /= distance
            y /= distance
        else:              
            x = 0
            y = 0

        self.moveX(x * self.vel_x)
        self.moveY(y * self.vel_y)

    def update(self,window):
        self.image = self.enemy_anims.nextEnemyAnim()
        window.blit(self.image,self.rect)

class GoblinEnemy(Entity):

    def __init__(self,x,y,width,height):
        #constructor for the pygame Sprite class
        super().__init__(x,y,width,height)
      
        #Instantiate class to handle sprite animation
        self.enemy_anims = SpriteAnimation("Entities/goblinguy.png")
      
        self.enemy_anims.registerAnim(0,pygame.transform.scale(self.enemy_anims.getFrame(-1,0,15,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(1,pygame.transform.scale(self.enemy_anims.getFrame(-20,0,15,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(2,pygame.transform.scale(self.enemy_anims.getFrame(-35,0,15,27), (width * 1.5, height * 1.7)))

        self.image = self.enemy_anims.frames[0]
        self.image.set_colorkey((0,0,0)) 
       
        self.direction = 0

        #Entity velocity 
        self.vel_x = 3
        self.vel_y = 3

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def findPlayer(self, player):
        #Finds the angle the enemy is relative to the player
        x = self.rect.centerx - player.rect.centerx
        y = self.rect.centery - player.rect.centery
        self.direction = (math.degrees(math.atan2(-y,x)) + 360) % 360
  
    def followPlayer(self, player):

        x = player.rect.centerx - self.rect.centerx
        y = player.rect.centery - self.rect.centery

        distance = math.hypot(x,y)

        if distance > 20: #If too close to player, stop movement
            x /= distance
            y /= distance
        else:              
            x = 0
            y = 0

        self.moveX(x * self.vel_x)
        self.moveY(y * self.vel_y)

    def update(self,window):
        self.image = self.enemy_anims.nextEnemyAnim()
        window.blit(self.image,self.rect)

class GhostEnemy(Entity):

    def __init__(self,x,y,width,height):
        #constructor for the pygame Sprite class
        super().__init__(x,y,width,height)
      
        #Instantiate class to handle sprite animation
        self.enemy_anims = SpriteAnimation("Entities/Ghost.png")
      
        self.enemy_anims.registerAnim(0,pygame.transform.scale(self.enemy_anims.getFrame(-1,0,15,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(1,pygame.transform.scale(self.enemy_anims.getFrame(-20,0,15,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(2,pygame.transform.scale(self.enemy_anims.getFrame(-35,0,15,27), (width * 1.5, height * 1.7)))

        self.image = self.enemy_anims.frames[0]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[1]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[2]
        self.image.set_colorkey((0,0,0)) 
       
        self.direction = 0

        #Entity velocity 
        self.vel_x = 3
        self.vel_y = 3

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def findPlayer(self, player):
        #Finds the angle the enemy is relative to the player
        x = self.rect.centerx - player.rect.centerx
        y = self.rect.centery - player.rect.centery
        self.direction = (math.degrees(math.atan2(-y,x)) + 360) % 360
  
    def followPlayer(self, player):

        x = player.rect.centerx - self.rect.centerx
        y = player.rect.centery - self.rect.centery

        distance = math.hypot(x,y)

        if distance > 20: #If too close to player, stop movement
            x /= distance
            y /= distance
        else:              
            x = 0
            y = 0

        self.moveX(x * self.vel_x)
        self.moveY(y * self.vel_y)

    def update(self,window):
        self.image = self.enemy_anims.nextEnemyAnim()
        window.blit(self.image,self.rect)

class DwarfEnemy(Entity):

    def __init__(self,x,y,width,height):
        #constructor for the pygame Sprite class
        super().__init__(x,y,width,height)
      
        #Instantiate class to handle sprite animation
        self.enemy_anims = SpriteAnimation("Entities/lilguy.png")
      
        self.enemy_anims.registerAnim(0,pygame.transform.scale(self.enemy_anims.getFrame(2,0,17,27), (width * 1.5, height * 2)))
        self.enemy_anims.registerAnim(1,pygame.transform.scale(self.enemy_anims.getFrame(-16,0,16,27), (width * 1.5, height * 2)))
        self.enemy_anims.registerAnim(2,pygame.transform.scale(self.enemy_anims.getFrame(-32,0,17,27), (width * 1.5, height * 2)))

        self.image = self.enemy_anims.frames[0]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[1]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[2]
        self.image.set_colorkey((0,0,0)) 
       
        self.direction = 0

        #Entity velocity 
        self.vel_x = 3
        self.vel_y = 3

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def findPlayer(self, player):
        #Finds the angle the enemy is relative to the player
        x = self.rect.centerx - player.rect.centerx
        y = self.rect.centery - player.rect.centery
        self.direction = (math.degrees(math.atan2(-y,x)) + 360) % 360
  
    def followPlayer(self, player):

        x = player.rect.centerx - self.rect.centerx
        y = player.rect.centery - self.rect.centery

        distance = math.hypot(x,y)

        if distance > 20: #If too close to player, stop movement
            x /= distance
            y /= distance
        else:              
            x = 0
            y = 0

        self.moveX(x * self.vel_x)
        self.moveY(y * self.vel_y)

    def update(self,window):
        self.image = self.enemy_anims.nextEnemyAnim()
        window.blit(self.image,self.rect)

class MushroomEnemy(Entity):

    def __init__(self,x,y,width,height):
        #constructor for the pygame Sprite class
        super().__init__(x,y,width,height)
      
        #Instantiate class to handle sprite animation
        self.enemy_anims = SpriteAnimation("Entities/Mushroom.png")
      
        self.enemy_anims.registerAnim(0,pygame.transform.scale(self.enemy_anims.getFrame(0,0,16,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(1,pygame.transform.scale(self.enemy_anims.getFrame(-16,0,16,27), (width * 1.5, height * 1.7)))
        self.enemy_anims.registerAnim(2,pygame.transform.scale(self.enemy_anims.getFrame(-32,0,16,27), (width * 1.5, height * 1.7)))

        self.image = self.enemy_anims.frames[0]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[1]
        self.image.set_colorkey((0,0,0)) 
        self.image = self.enemy_anims.frames[2]
        self.image.set_colorkey((0,0,0)) 
        self.direction = 0

        #Entity velocity 
        self.vel_x = 3
        self.vel_y = 3

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def findPlayer(self, player):
        #Finds the angle the enemy is relative to the player
        x = self.rect.centerx - player.rect.centerx
        y = self.rect.centery - player.rect.centery
        self.direction = (math.degrees(math.atan2(-y,x)) + 360) % 360
  
    def followPlayer(self, player):

        x = player.rect.centerx - self.rect.centerx
        y = player.rect.centery - self.rect.centery

        distance = math.hypot(x,y)

        if distance > 20: #If too close to player, stop movement
            x /= distance
            y /= distance
        else:              
            x = 0
            y = 0

        self.moveX(x * self.vel_x)
        self.moveY(y * self.vel_y)

    def update(self,window):
        self.image = self.enemy_anims.nextEnemyAnim()
        window.blit(self.image,self.rect)

class SpriteAnimation:
    """
    Implements interface for splitting up spritesheets
    into individual frames of animation to be used by 
    various entity classes
    """

    def __init__(self, filepath, scale_by=None):

        self.sheet = pygame.image.load(filepath)
        self.frames = dict() #contains all frames of animation
        self.next = False #moves animation foward
        self.count = 0
        self.curr_anim = 0#current animation in animation cycle

    def registerAnim(self,name,image):
        """
          Adds new frame of animation from the
          spritesheet to the frame dictionary
        """
        self.frames[name] = image

    def getFrame(self,x,y,width,height):
        #converts spritesheet to pygame surface
        image = pygame.Surface((width,height)).convert_alpha()

        #Cuts out individual sprite from spritesheet
        image.blit(self.sheet,(x,y,width,height))

        #Removes colored outline around the sprite 
        image.set_colorkey((0,0,0)) 
        return image

    def getSprite(self, name):
        return self.frames[name]

    def nextAnim(self):
        #Alternates the player walking sprite
        if (self.count == 5):
            self.next = not self.next
            self.count = 0
        self.count += 1

    def nextEnemyAnim(self):
        temp_dict = list(self.frames)
        #Alternates the enemy walking sprite
        if (self.count == 5):
            self.count = 0
            self.curr_anim += 1
      
        if(self.curr_anim == 3):
            self.curr_anim = 0

        temp_anim = self.frames[self.curr_anim]
        self.count += 1
        return temp_anim

   


       

    


    

