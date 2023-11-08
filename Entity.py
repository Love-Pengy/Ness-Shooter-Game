import pygame
import math
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
        self.player_anims = SpriteAnimation("ness_spritesheet.png")

        #load individual sprites into animation dict
        self.player_anims.registerAnim("walk_down1",self.player_anims.getFrame(0,0,64,100))
        self.player_anims.registerAnim("walk_down2" ,self.player_anims.getFrame(-68,0,64,100))
        self.player_anims.registerAnim("walk_right1",self.player_anims.getFrame(-160,0,64,100))
        self.player_anims.registerAnim("walk_right2",self.player_anims.getFrame(-230,0,64,100))
        self.player_anims.registerAnim("walk_se1",self.player_anims.getFrame(-324,0,64,100))
        self.player_anims.registerAnim("walk_se2",self.player_anims.getFrame(-400,0,64,100))
        self.player_anims.registerAnim("walk_ne1",self.player_anims.getFrame(-400,0,64,100))
        self.player_anims.registerAnim("walk_ne2",self.player_anims.getFrame(-568,0,64,100))
        self.player_anims.registerAnim("walk_up1",self.player_anims.getFrame(0,-120,64,100))
        self.player_anims.registerAnim("walk_up2",self.player_anims.getFrame(-74,-120,64,100))
        self.player_anims.registerAnim("walk_left1",self.player_anims.getFrame(-160,-120,64,100))
        self.player_anims.registerAnim("walk_left2",self.player_anims.getFrame(-230,-120,64,100))
        self.player_anims.registerAnim("walk_sw1",self.player_anims.getFrame(-328,-120,64,100))
        self.player_anims.registerAnim("walk_sw2",self.player_anims.getFrame(-400,-120,64,100))
        self.player_anims.registerAnim("walk_nw1",self.player_anims.getFrame(-568,-120,64,100))
        self.player_anims.registerAnim("walk_nw2",self.player_anims.getFrame(-570,-120,64,100))
        # self.image = player_anims.getFrame(-180,0,64,100)
        self.image = self.player_anims.getFrame(-570,-120,64,100)
        # self.image = player_anims.getFrame(200,-100,500,100)

        #player initial velocity 
        self.vel_x = 0
        self.vel_y = 0

        #make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self,window,key):
        window.blit(self.image, self.rect)
        if key[pygame.K_a]: 
            self.moveX(self.vel_x)
        if key[pygame.K_d]:
            self.image = self.player_anims.frames["walk_right1"]
            self.moveX(self.vel_x)
        if key[pygame.K_w]:
            self.moveY(self.vel_y)
            #if pressed[pygame.K_RIGHT]:
               #self.moveX(self.vel_x)
           # elif pressed[pygame.K_LEFT]:
               #self.moveX(-1 * self.vel_x)
        if key[pygame.K_s]:
            self.image = self.player_anims.frames["walk_down1"]
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
        player_dir = (math.degrees(math.atan2(-y,x)) + 360.0) % 360.0

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
     
        #print("TEST")
        #print(player_dir)

        #Sets sprite according to position of the mouse
        #if player_dir < 180:
            #self.image = self.player_anims.frames["walk_right1"]
        #else:
            #self.image = self.player_anims.frames["walk_down1"]

        





    def processInput(self, pressed):
        if pressed[pygame.K_a]: 
            self.vel_x = -1
            #self.moveX(-1 * self.vel_x)
        if pressed[pygame.K_d]:
            self.image = self.player_anims.frames["walk_right1"]
            self.vel_x = 1
            #self.moveX(self.vel_x)
        if pressed[pygame.K_w]:
            self.vel_y = -1
            #self.moveY(-1 * self.vel_y)
            #if pressed[pygame.K_RIGHT]:
               #self.moveX(self.vel_x)
           # elif pressed[pygame.K_LEFT]:
               #self.moveX(-1 * self.vel_x)
        if pressed[pygame.K_s]:
            self.image = self.player_anims.frames["walk_down1"]
            self.vel_y = 1
            #self.moveY(self.vel_y)
            #if pressed[pygame.K_RIGHT]:
               #self.moveX(self.vel_x)
            #elif pressed[pygame.K_LEFT]:
               #self.moveX(-1 * self.vel_x)

        
class SpriteAnimation:

    """
    Implements interface for splitting up spritesheets
    into individual frames of animation to be used by 
    various entity classes
    """

    def __init__(self, filepath, scale_by=None):

        self.sheet = pygame.image.load(filepath)
        self.frames = dict() #contains all frames of animation
        self.next = False #moves animations forward
        self.count = 0

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
    
    def nextAnim(self):
        if (self.count % 60 == 0):
            self.next = not self.next
            count = 0
        count += 1
        self.next = not self.next