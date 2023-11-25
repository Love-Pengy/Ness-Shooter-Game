import pygame
from pygame.math import Vector2

class Projectile:
    def __init__(self, position, direction, speed, damage):
        self.x = x 
        self.y = y
        self.position = Vector2(self.x, self.y)
        self.direction = direction
        self.speed = speed
        self.damage = damage 
        self.image = pygame.image.load("projectile.png")
        
    def update(self):
        # Move projectile
        self.x += self.direction.x * self.speed  
        self.y += self.direction.y * self.speed  
    
    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        
    def collide(self, enemy):
        # Simple collision check
        if self.x >= enemy.x and self.x <= enemy.x + enemy.width:
            if self.y >= enemy.y and self.y <= enemy.y + enemy.height:
                return True
  
        return False
        
def create_projectile(x, y, direction, speed, damage):
    return Projectile(x, y, direction, speed, damage) 
    
def handle_projectiles(projectiles, enemies):
    for projectile in projectiles:
        projectile.update()
        projectile.draw(win)
        
        # Check collision with enemies
        for enemy in enemies:
            if projectile.collide(enemy):
                enemy.take_damage(projectile.damage)
                projectiles.remove(projectile)
                break
        
    # Remove offscreen projectiles            
    for projectile in projectiles:
        if projectile.x < -32 or projectile.x > WIDTH or projectile.y < -32 or projectile.y > HEIGHT:
            projectiles.remove(projectile)
