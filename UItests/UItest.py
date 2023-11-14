import pygame
from UI import UIManager
DEBUG = 0
#weapons binds
weaponBinds = [1, 2, 3, 4]
#consumable binds but only if we allow quick consumesi
#lets make q heal and e mana pot
consumableBinds = ['q','e']
pauseBind = 'esc'
#weapons that user starts game with
defaultWeapons = {
        "pistol" : "placeholder",  
        "shotgun" : None, 
        "machineGun" : None
        }


#bind for inventory
inventoryBind = 'tab'

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

#another placeholder
currentScore = 0

def itemsGen(): 
    index = 0
    while True: 
        if(((index % 300) == 0)):
            defaultItems["healthPotions"] = None
            defaultItems["manaPotions"] = None
            if(DEBUG): 
                print("HERE\n\n\n\n\n\n")
            index += 1
            yield
        elif((index % 300) == 50): 
            defaultItems["healthPotions"] = 1
            defaultItems["manaPotions"] = 1
            index += 1
            if(DEBUG): 
                print("HERE2\n\n\n\n\n\n")
            yield    
        elif(((index % 300) >  50) & ((index % 300) < 200)): 
            index += 1
            defaultItems["manaPotions"] = None
            defaultItems["healthPotions"] = index
            if(DEBUG): 
                print("HERE3\n\n\n\n\n\n\n")
            yield
        elif(((index % 300) > 200) & ((index % 300) <  300)): 
            index += 1
            defaultItems["healthPotions"] = None
            defaultItems["manaPotions"] = index
            yield
        else:
            if(DEBUG): 
                print("ONLY GETTING TO ELSE")
            index += 1
            yield
        

def weaponsGen(): 
    index = 0
    while True: 
        if((index % 300) == 0): 
            defaultWeapons["pistol"] = "placeholder"
            defaultWeapons["shotgun"] = None
            defaultWeapons["machineGun"] = None
            yield
        elif((index % 300) == 100): 
            defaultWeapons["pistol"] = None
            defaultWeapons["shotgun"] = "placeholder"
            defaultWeapons["machineGun"] = None
            yield
        elif((index % 300) == 200): 
            defaultWeapons["pistol"] = None
            defaultWeapons["shotgun"] = None
            defaultWeapons["machineGun"] = "placeholder"
            yield
        else: 
            yield
        index += 1


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
            defaultStats["mana"] = val
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
        self.weaponsGenerator = weaponsGen()
        self.itemsGenerator = itemsGen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            keys = pygame.key.get_pressed()
            self.screen.fill("black")
            self.score = next(self.scoreGenerator)
            next(self.weaponsGenerator)
            next(self.gen)
            next(self.itemsGenerator)
            UI.update(keys, defaultStats, self.score, defaultWeapons, defaultItems)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game(1800, 960)
    game.loop()
