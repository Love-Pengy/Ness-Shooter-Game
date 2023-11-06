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
        self.player_anims.registerAnim("walk_down2" ,self.player_anims.getFrame(0,0,64,100))
        self.player_anims.registerAnim("walk_right1",self.player_anims.getFrame(-160,0,64,100))
        self.player_anims.registerAnim("walk_right2",self.player_anims.getFrame(-156,0,64,100))
        # self.image = player_anims.getFrame(-180,0,64,100)
        self.image = self.player_anims.getFrame(0,0,64,100)
        # self.image = player_anims.getFrame(200,-100,500,100)

        #player velocity 
        self.vel_x = 1
        self.vel_y = 1

        #make rectangle from sprite image
        self.rect = self.image.get_rect()

    def update(self,window):
         window.blit(self.image, self.rect)
    

    def setDirection(self,mouse_x,mouse_y):
        """
        Function to determine mouse position
        relative to the player in order to determine 
        correct sprite and direction for aiming
        """

        x = mouse_x - self.rect.x
        y = mouse_y - self.rect.y

        #Direction player is aiming in degrees
        player_dir = math.atan2(y,x) *  (180.0 / math.pi) 
     
        #print("TEST")
        #print(player_dir)

        #Sets sprite according to position of the mouse
        if player_dir < 180:
            self.image = self.player_anims.frames["walk_right1"]
        else:
            self.image = self.player_anims.frames["walk_down1"]

        





    def processInput(self, pressed):
        if pressed[pygame.K_LEFT]: 
            self.moveX(-1 * self.vel_x)
        if pressed[pygame.K_RIGHT]:
            self.image = self.player_anims.frames["walk_right1"]
            self.moveX(self.vel_x)
        if pressed[pygame.K_UP]:
            self.moveY(self.vel_y * -1)
            if pressed[pygame.K_RIGHT]:
               self.moveX(self.vel_x)
            elif pressed[pygame.K_LEFT]:
               self.moveX(-1 * self.vel_x)
        if pressed[pygame.K_DOWN]:
            self.image = self.player_anims.frames["walk_down1"]
            self.moveY(self.vel_y)
            if pressed[pygame.K_RIGHT]:
               self.moveX(self.vel_x)
            elif pressed[pygame.K_LEFT]:
               self.moveX(-1 * self.vel_x)

        
class SpriteAnimation:

    """
    Implements interface for splitting up spritesheets
    into individual frames of animation to be used by 
    various entity classes
    """

    def __init__(self, filepath, scale_by=None):

        self.sheet = pygame.image.load(filepath)
        self.frames = dict() #contains all frames of animation

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