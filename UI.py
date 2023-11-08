#File David made that allows buttons to be created and checked for pressed attribute
from Button import Button
import pygame

continueButton = pygame.image.load("Assets/ContinueButton.png")
exitButton = pygame.image.load("Assets/ExitButton.png")

class UIManager:
    #build all of respective UI's
    def __init__(self, weapons, items, stats, score, screen):
        self.wHUD = WeaponsHUD(weapons)
        #self.iHUD = ItemsHUD(items)
        self.stHUD = StatHUD(stats)
        self.scHUD = ScoreHUD(score)
        self.pMenu = PauseMenu(screen)
        
    #update weapons HUD with the new order of weapons or weapon 
    def updateWeaponHUD(self, newWeapons):
        self.wHUD.update(newWeapons)

    #update count of items based off of the new inventory amount
    def updateItemHUD(self, newItems):
        self.iHUD.update(newItems)
    
    #update stat UI with new stats based off of Player class values
    def updateStatHUD(self, newStats):
        self.stHUD.update(newStats)

    #bring up pause menu, execute appropriate action based off of button hit
    def pauseMenuToggle(self):
        self.pMenu.toggle()

    #update score HUD
    def updateScoreHUD(self, newScore):
        self.scHUD.udpate(newScore, newScore)
    
    def update(self, keys):
        if(keys[pygame.K_ESCAPE]): 
            self.pMenu.toggle()
        if(not keys[pygame.K_ESCAPE]): 
            self.pMenu.setEligibleToggle()
        if(self.pMenu.active): 
            self.pMenu.execute()
        

class PauseMenu:
    
    def __init__(self, screen): 
        self.continueB = Button(screen, 100, 500, continueButton)
        self.exitB = Button(screen, 1400, 500, exitButton)
        #maybe instead of drawing a boring ass box I can make the bg have a gauss blur
        self.active = 0
        self.eligibleToggle = True 

    def toggle(self): 
        if(self.eligibleToggle):
            if(self.active): 
                self.active = 0
            else: 
                self.active = 1
            self.eligibleToggle = False
    
    def setEligibleToggle(self): 
        self.eligibleToggle= True

    def execute(self): 
        if(self.active): 
            self.exitB.draw()
            self.continueB.draw()
            if(self.exitB.IsPressed()): 
                exit()
            if(self.continueB.IsPressed()): 
                self.toggle()


#To make it easy HUD'S will be out of the way of hte pause menu that way the pause can just be in the middle
class WeaponsHUD: 

    def __init__(self, defaultWeapons): 
        self.currWeapons = defaultWeapons
        
    
    def build(self): 
        pass

    def update(self, newWeapons): 
        self.currWeapons = newWeapons

class StatHUD: 
    def __init__(self, stats): 
        self.attk = stats.get("attack")
        self.defense = stats.get("defense")
        self.speed = stats.get("speed")
        self.hp = stats.get("hp")
        
    
    def build(self): 
        pass
    
    def update(self, attk = None, defense = None, speed = None, hp = None): 
        #update values
        pass 

class ScoreHUD: 
    def __init__(self, score): 
        self.score = score
       
    
    def build(self): 
        pass

    def update(self, score = None): 
        #update score
        pass
