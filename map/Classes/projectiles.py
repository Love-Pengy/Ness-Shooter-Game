import pygame
from pygame.math import Vector2
from math import cos, sin
from math import radians as rads
from math import atan2

DEBUG = 0

class Projectile:
    def __init__(self, position, direction, speed, damage):
        self.x = position[0]
        self.y = position[1]  
        #self.position = Vector2(self.x, self.y)
        self.position = position
        self.direction = direction
        self.image = pygame.image.load("UIAssets/bullet.png") # Here is the bullet
        self.speed = speed
        self.damage = damage
        if(DEBUG): 
            print(f"angleTesting: {self.position.angle_to((0, 0))}")
        self.image = pygame.transform.rotate(self.image, (direction+270))
        self.rect = self.image.get_rect()

    def update(self):
        # Move projectile, trig functions are from basic vector math 
        self.x += self.speed * cos(rads(self.direction))
        self.y += ((self.speed * -1) * sin(rads(self.direction)))
    
    def draw(self, win):
        win.blit(self.image, (self.x, self.y)) # Draws the bullet
           
    def collide(self, enemy):
        # Collision check
        if self.x >= enemy.x and self.x <= enemy.x + enemy.width:
            if self.y >= enemy.y and self.y <= enemy.y + enemy.height:
                return True
    
        return False
        
def create_projectile(position, direction, speed, damage):
    return Projectile(position, direction, speed, damage)
