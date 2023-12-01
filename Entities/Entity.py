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

    def __init__(self, x, y, width, height):

        # constructor for the pygame Sprite class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        # Velocity of entity movement for testing
        self.vel_x = 5
        self.vel_y = 5

        self.rect = self.image.get_rect()

    def moveX(self, x_vel):
        self.rect.x += x_vel

    def moveY(self, y_vel):
        self.rect.y += y_vel

    def update(self, window):
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

    def __init__(self, x, y, width, height):

        # constructor for the pygame Sprite class
        super().__init__(x, y, width, height)

        # Instantiate class to handle sprite animation
        self.player_anims = SpriteAnimation("Entities/ness_spritesheet.png")

        # Load individual sprites into animation dict
        self.player_anims.registerAnim("walk_down1", self.player_anims.getFrame(0, 0, 64, 100))
        self.player_anims.registerAnim("walk_down2", self.player_anims.getFrame(-68, 0, 64, 100))
        self.player_anims.registerAnim("walk_right1", self.player_anims.getFrame(-160, 0, 64, 100))
        self.player_anims.registerAnim("walk_right2", self.player_anims.getFrame(-230, 0, 64, 100))
        self.player_anims.registerAnim("walk_se1", self.player_anims.getFrame(-324, 0, 64, 100))
        self.player_anims.registerAnim("walk_se2", self.player_anims.getFrame(-400, 0, 64, 100))
        self.player_anims.registerAnim("walk_ne1", self.player_anims.getFrame(-568, 0, 64, 100))
        self.player_anims.registerAnim("walk_ne2", self.player_anims.getFrame(-486, 0, 64, 100))
        self.player_anims.registerAnim("walk_up1", self.player_anims.getFrame(0, -120, 64, 100))
        self.player_anims.registerAnim("walk_up2", self.player_anims.getFrame(-74, -120, 64, 100))
        self.player_anims.registerAnim("walk_left1", self.player_anims.getFrame(-160, -120, 64, 100))
        self.player_anims.registerAnim("walk_left2", self.player_anims.getFrame(-230, -120, 64, 100))
        self.player_anims.registerAnim("walk_sw1", self.player_anims.getFrame(-328, -120, 64, 100))
        self.player_anims.registerAnim("walk_sw2", self.player_anims.getFrame(-400, -120, 64, 100))
        self.player_anims.registerAnim("walk_nw1", self.player_anims.getFrame(-490, -120, 64, 100))
        self.player_anims.registerAnim("walk_nw2", self.player_anims.getFrame(-570, -120, 64, 100))
    
        self.image = self.player_anims.frames["walk_down1"]  # initial sprite
    
        # player velocity
        self.vel_x = 2.5
        self.vel_y = 2.5

        # make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, window):
         window.blit(self.image, self.rect)
    
    def setDirection(self, mouse_pos):
        """
        Function to determine mouse position
        relative to the player in order to determine 
        correct sprite and direction for aiming
        """

        x = mouse_pos[0] - self.rect.centerx
        y = mouse_pos[1] - self.rect.centery

        # Direction player is aiming in degrees 
        player_dir = (math.degrees(math.atan2(-y, x)) + 360) % 360

        # Direction player is facing split into 8 directions to determine correct sprite     
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
        if pressed[pygame.K_w] or pressed[pygame.K_a] or pressed[pygame.K_s] or pressed[pygame.K_d]:
            self.player_anims.nextAnim()

        if pressed[pygame.K_w]:
            self.moveY(self.vel_y * -1)
            if pressed[pygame.K_d]:
               self.moveX(self.vel_x)
            elif pressed[pygame.K_a]:
               self.moveX(-1 * self.vel_x)
        if pressed[pygame.K_s]:
            self.moveY(self.vel_y)
            if pressed[pygame.K_d]:
               self.moveX(self.vel_x)
            elif pressed[pygame.K_a]:
               self.moveX(-1 * self.vel_x)
        if pressed[pygame.K_a]: 
            self.moveX(-1 * self.vel_x)
        if pressed[pygame.K_d]:
            self.moveX(self.vel_x)    
        
class SerpentEnemy(Entity):

    def __init__(self, x, y, width, height):
        # constructor for the pygame Sprite class
        super().__init__(x, y, width, height)

        # Instantiate class to handle sprite animation
        self.enemy_anim = SpriteAnimation("Entities/Serpent.gif")

        self.image = self.enemy_anim.getFrame(0, 0, 96, 96)
        self.image = pygame.transform.rotate(self.image, 90)  # Rotates sprite image to initially face player
        self.image.set_colorkey((0, 0, 0)) 
        self.direction = 0

        # Entity velocity 
        self.vel_x = 2
        self.vel_y = 2

        # make rectangle from sprite image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y


    def findPlayer(self, player):
        x = self.rect.x - player.rect.x
        y = self.rect.y - player.rect.y
        self.direction = (math.degrees(math.atan2(-y, x)) + 360) % 360
  


    def update(self, window):
        rotated_image = pygame.transform.rotate(self.image, self.direction)
        rotated_rect = rotated_image.get_rect()
        rotated_rect.x, rotated_rect.y = self.rect.x,self.rect.y
        window.blit(rotated_image,rotated_rect)


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

    def registerAnim(self, name, image):
        """
          Adds new frame of animation from the
          spritesheet to the frame dictionary
        """
        self.frames[name] = image

    def getFrame(self, x, y, width, height):
        #converts spritesheet to pygame surface
        image = pygame.Surface((width, height)).convert_alpha()

        #Cuts out individual sprite from spritesheet
        image.blit(self.sheet,(x, y, width, height))

        #Removes colored outline around the sprite 
        image.set_colorkey((0, 0, 0)) 
        return image

    def getSprite(self, name):
        return self.frames[name]

    def nextAnim(self):
        #switches sprites twice a second
        if (self.count == 30):
            self.next = not self.next
            self.count = 0
        self.count += 1