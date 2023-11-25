import pygame
from UI import UIManager
import projectiles
from Weapons import Weapon
from pygame.math import Vector2
from map.map import * #Could just `import map.map` but ok

DEBUG = 0
#weapons that user starts game with
defaultWeapons = {
        "pistol" : "placeholder",  
        "shotgun" : None, 
        "machineGun" : None
        }

#default Items
defaultItems ={
        "healthPotions" : None, 
        "manaPotions" : None
        }

#default stats
defaultStats ={
        "attack" : 0, 
        "defense" : 0, 
        "speed" : 0,
        "hp" : 100, 
        "mana" : 50
        }

class Game:
    def __init__(self):
        """
        Start up Pygame and instantiate all
        relevant actors.
        @width : sets width of the screen
        @height : sets height of the screen
        """
        self.FPS = 60
        self.TILESIZE = 40
        self.MAPWIDTH = 45
        self.MAPHEIGHT = 24
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.MAPWIDTH * self.TILESIZE, self.MAPHEIGHT * self.TILESIZE))
        self.map = Map(self.screen)
        # this allows us to filter the event queue
        # for faster event processing
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN
        ])



    def loop(self, weapon):
        """
        Primary game loop. This should be
        run perpetually until the game is
        over or is closed.
        """
        self.screen.fill("black")
        self.weapons = defaultWeapons
        self.items = defaultItems
        self.stats = defaultStats
        self.score = 0
        self.UI = UIManager(self.weapons, self.items, self.stats, self.score, self.screen)

        while True:
            #self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left mouse button clicked
                    mouse_pos = pygame.mouse.get_pos()
                    weapon.fire(Vector2(mouse_pos[0], mouse_pos[1]), Vector2(1,0))
            self.screen.fill("black")
            self.map.update(self.screen)
            keys = pygame.key.get_pressed()
            self.UI.update(keys, self.stats, self.score, self.weapons, self.items)
            pygame.display.flip()
            # pygame.display.update()
            self.clock.tick(self.FPS)


if __name__ == "__main__":
    game = Game()
    weapon = Weapon(1.0, 2.0, 10, 5, 1.0)
    game.loop(weapon)
