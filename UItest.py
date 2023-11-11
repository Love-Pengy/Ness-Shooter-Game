import pygame
from UI import UIManager
DEBUG = 1
#weapons binds
weaponBinds = [1, 2, 3, 4]
#consumable binds but only if we allow quick consumesi
#lets make q heal and e mana pot
consumableBinds = ['q','e']
pauseBind = 'esc'
#weapons that user starts game with
defaultWeapons = ['handgun', None]

#bind for inventory
inventoryBind = 'tab'

#default Items
defaultItems = list()

#default stats
defaultStats ={
        "attack" : 0, 
        "defense" : 0, 
        "speed" : 0,
        "hp" : 100
        }

#another placeholder
currentScore = 0

def scoreGen(): 
    val = 0
    index = 0
    while True: 
        if(not (index % 3)): 
            val += 5
            yield val
        else: 
            yield val
        index += 1

def statGen(): 
    i = 0
    val = 0
    while True: 
        if(not (i % 10)): 
            val += 1
            defaultStats["attack"] = val
            defaultStats["defense"] = val
            defaultStats["speed"] = val
            defaultStats["hp"] = val
            yield
        else: 
            yield 
        i += 1

class Game:
    def __init__(self, width, height):
        """
        Start up Pygame and instantiate all
        relevant actors.
        @width : sets width of the screen
        @height : sets height of the screen
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))

        # this allows us to filter the event queue
        # for faster event processing
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN
        ])



    def loop(self):
        """
        Primary game loop. This should be
        run perpetually until the game is
        over or is closed.
        """
        self.screen.fill("black")
        UI = UIManager(defaultWeapons, defaultItems, defaultStats, 0, self.screen)
        self.gen = statGen()
        self.scoreGenerator = scoreGen()
        self.score = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            keys = pygame.key.get_pressed()
            self.screen.fill("black")
            self.score = next(self.scoreGenerator)
            next(self.gen)
            UI.update(keys, defaultStats, self.score)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game(1800, 960)
    game.loop()
