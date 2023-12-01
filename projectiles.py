import pygame
from pygame.math import Vector2

class Projectile:
    def __init__(self, position, direction, speed, damage):
        self.x = position[0]
        self.y = position[1]  
        self.position = Vector2(self.x, self.y)
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.image = pygame.image.load("UIAssets/bullet.png") # Here is the bullet
        
    def update(self):
        # Move projectile 
        self.x += self.position[0] + self.speed  
        self.y += self.position[1] + self.speed
    
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