#asset sites: 
# https://www.ludicarts.com/free-rpg-icons/
# https://opengameart.org/content/larger-simple-heart
# https://opengameart.org/content/golden-ui
# https://opengameart.org/content/rpg-ui-icons
#File David made that allows buttons to be created and checked for pressed attribute
from Button import Button
import pygame
DEBUG = 1

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#usage: 
#label = myfont.render("wanted text", num, color)

uiBorders = pygame.image.load("Assets/UIBorders.png")
uiBorders = pygame.transform.scale_by(uiBorders, 3)

uiBorders2 = pygame.image.load("Assets/UIBorders2.png")
uiBorders2 = pygame.transform.scale_by(uiBorders2, 1.5)


currManaIcon = pygame.image.load("Assets/manaIcon.png")
currManaIcon = pygame.transform.scale(currManaIcon, (55, 45))

pistolSprite = pygame.image.load("Assets/Pistol.png")
pistolSprite = pygame.transform.scale(pistolSprite, (55, 45))
shotgunSprite = pygame.image.load("Assets/Shotgun.png")
shotgunSprite = pygame.transform.scale(shotgunSprite, (55, 45))
machineGunSprite = pygame.image.load("Assets/MachineGun.png")
machineGunSprite = pygame.transform.scale(machineGunSprite, (55, 45))

healthIcon = pygame.image.load("Assets/Health_Icon.png")
healthIcon = pygame.transform.scale(healthIcon, (40, 40))
continueButton = pygame.image.load("Assets/ContinueButton.png")
exitButton = pygame.image.load("Assets/ExitButton.png")
baseDamageIcon = pygame.image.load("Assets/Damage_Icon_Base.png")
#https://stackoverflow.com/questions/27576645/how-to-overcome-python-fonts-pygame-not-being-loaded
baseDamageIcon = pygame.transform.scale(baseDamageIcon, (50, 50))
frostyDamageIcon = pygame.image.load("Assets/Damage_Icon_Frosty.png")
flamingDamageIcon = pygame.image.load("Assets/Damage_Icon_Flaming.png")
speedIcon = pygame.image.load("Assets/Speed_Icon.png")
speedIcon = pygame.transform.scale(speedIcon, (50, 50))
defenseIcon = pygame.image.load("Assets/Defense_Icon.png")
defenseIcon = pygame.transform.scale(defenseIcon, (40, 40))
healthItemIcon = pygame.image.load("Assets/Health_Item_Icon.png")
healthItemIcon = pygame.transform.scale(healthItemIcon, (40, 40))
manaIcon = pygame.image.load("Assets/Mana_Icon.png")
manaIcon = pygame.transform.scale(manaIcon, (40, 40))

class UIManager:
    #build all of respective UI's
    def __init__(self, weapons, items, stats, score, screen):
        self.wHUD = WeaponsHUD(weapons, screen)
        self.iHUD = ItemsHUD(items, screen)
        self.stHUD = StatHUD(stats, screen)
        self.scHUD = ScoreHUD(score, screen)
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
        self.scHUD.update(newScore)
    
    def update(self, keys, stats, score, weapons, items):
        if(keys[pygame.K_ESCAPE]): 
            self.pMenu.toggle()
        if(not keys[pygame.K_ESCAPE]): 
            self.pMenu.setEligibleToggle()
        if(self.pMenu.active): 
            self.pMenu.execute()
        self.updateStatHUD(stats)
        self.updateScoreHUD(score)
        self.updateWeaponHUD(weapons)
        self.updateItemHUD(items)
        self.iHUD.execute()
        self.wHUD.execute()
        self.stHUD.execute()
        self.scHUD.execute()

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
        if(DEBUG): 
            print(f"PauseMenu Status: {self.active=} {self.eligibleToggle=}")

        if(self.active): 
            self.exitB.draw()
            self.continueB.draw()
            if(self.exitB.IsPressed()): 
                exit()
            if(self.continueB.IsPressed()): 
                self.toggle()



class StatHUD:
    #passed a dict of stats 
    def __init__(self, stats, screen):
        self.attack = stats.get("attack")
        self.defense = stats.get("defense")
        self.speed = stats.get("speed")
        self.hp = stats.get("hp")
        self.mana = stats.get("mana")

        self.screen = screen
        self.active = 1
        self.attackRect = baseDamageIcon.get_rect()
        self.attackRect = self.attackRect.move(50, 950)
        self.attackTextSurface = myfont.render(str(self.attack), False, (255,255, 255))
        #self.textSurface = self.textSurface.move(100, 950)
        self.defenseRect = defenseIcon.get_rect()
        self.defenseRect = self.defenseRect.move(150, 960)
        self.defenseTextSurface = myfont.render(str(self.defense), False, (255, 255, 255))
        self.speedRect = speedIcon.get_rect()
        self.speedRect = self.speedRect.move(250, 955)
        self.speedTextSurface = myfont.render(str(self.speed), False, (255, 255, 255))
        self.hpRect = healthIcon.get_rect()
        self.hpRect = self.hpRect.move(350, 962)
        self.hpTextSurface = myfont.render(str(self.hp), False, (255, 255, 255))
        self.currManaRect = manaIcon.get_rect()
        self.currManaRect = self.currManaRect.move(440, 960)

        if(DEBUG): 
            print(f"{self.attack=}, {self.defense=}, {self.speed=}, {self.hp=}, {self.mana=}")
        '''
        self.defenseRect = defenseIcon.get_rect()
        self.defenseRect = self.defenseRect.move(200, 800)
        self.speedRect = speedIcon.get_rect()
        self.speedRect = self.speedRect.move(400, 800)
        self.hpRect = healthIcon.get_rect()
        self.hpRect = self.hpRect.move(600, 800)
        '''

    def toggle(self): 
        if(self.active): 
            self.active = 0
        else: 
            self.active = 1

    def update(self, stats): 
        #update values 
        self.attack = stats["attack"]
        self.defense = stats["defense"]
        self.speed = stats["speed"]
        self.hp = stats["hp"]
        self.mana = stats["mana"]
        if(DEBUG): 
            print(f"{self.attack=}")
            print(f"{self.defense=}")
            print(f"{self.speed=}")
            print(f"{self.hp=}")
            print(f"{self.mana=}")

        self.defenseTextSurface = myfont.render(str(self.defense), False, (255, 255,255))
        self.attackTextSurface = myfont.render(str(self.attack), False, (255, 255, 255))
        self.speedTextSurface = myfont.render(str(self.speed), False, (255, 255, 255))
        self.hpTextSurface = myfont.render(str(self.hp), False, (255, 255, 255))
        self.currManaTextSurface = myfont.render(str(self.mana), False, (255, 255, 255))

    def execute(self): 
        #draw everything to the screen if active
        if(self.active): 
            #self.screen.blit(image, rectangle)
            self.screen.blit(baseDamageIcon, self.attackRect)
            self.screen.blit(self.attackTextSurface, (100,975))
            self.screen.blit(defenseIcon, self.defenseRect)
            self.screen.blit(self.defenseTextSurface, (200,975))
            self.screen.blit(speedIcon, self.speedRect)
            self.screen.blit(self.speedTextSurface, (300, 975))
            self.screen.blit(healthIcon, self.hpRect)
            self.screen.blit(self.hpTextSurface, (400, 975))
            self.screen.blit(self.currManaTextSurface, (500, 975))
            self.screen.blit(currManaIcon, self.currManaRect)
            '''
            self.screen.blit(self.screen, self.defenseRect)
            self.screen.blit(self.screen, self.speedRect)
            self.screen.blit(self.screen, self.hpRect)
            '''


class ScoreHUD: 
    def __init__(self, score, screen):
        self.screen = screen
        self.score = score
        self.scoreTextSurface = myfont.render(str(self.score), False, (255, 255, 255))
        self.active = 1

    def toggle(self): 
        if(self.active): 
            self.active = 0
        else: 
            self.active = 1
        
    def update(self, score): 
        self.score = score
        self.scoreTextSurface = myfont.render(str(self.score), False, (255, 255, 255))

    def execute(self): 
        if(self.active): 
            self.screen.blit(uiBorders2, (857, 0), (250, 275, 165, 50)) 
            self.screen.blit(self.scoreTextSurface, (930, 15))
def checkDeco(weapon, screen): 
    '''
    if(isInstance(weapon, FlamingDeco)):
        screen.blit(uiBorders, (1400, 250), (145, 360, 47, 50))
    elif(isInstance(weapon, FrostyDeco)): 
        screen.blit(uiBorders, (1450, 250), (95, 360, 47, 50))
    elif(isInstance(weapon, ShroomDeco)): 
        screen.blit(uiBorders, (1500, 250), (45, 360, 50, 50))
    else:
    '''
    pass


class WeaponsHUD: 
    def __init__(self, weapons, screen):
        self.screen = screen
        #will be none if they don't exist
        self.pistol = weapons["pistol"]
        self.shotgun = weapons["shotgun"]
        self.machineGun = weapons["machineGun"]
        self.active = 1
        self.pistolRect = pistolSprite.get_rect()
        self.pistolRect = self.pistolRect.move(1522, 935)
        self.shotgunRect = shotgunSprite.get_rect()
        self.shotgunRect = self.shotgunRect.move(1595, 935)
        self.machineGunRect = machineGunSprite.get_rect()
        self.machineGunRect = self.machineGunRect.move(1665, 935)

    def toggle(self): 
        if(self.active): 
            self.active = 0
        else: 
            self.active = 1
        
    def update(self, weapons):
        self.pistol = weapons["pistol"]
        self.shotgun = weapons["shotgun"]
        self.machineGun = weapons["machineGun"]        



    def execute(self):
        if(self.active):
            if(DEBUG): 
                print(f"{self.pistol=}, {self.shotgun=}, {self.machineGun=}")
            #this is crop for weapons bar (location of blit, location of contents for crop, dimensions of crop)
            self.screen.blit(uiBorders, (1500, 925), (2300, 150, 250, 75))
            if(self.pistol):
                #checks for power up, if found it blits the associated icon
                checkDeco(self.pistol, self.screen)
                self.screen.blit(pistolSprite, self.pistolRect)

            if(self.shotgun):
                checkDeco(self.shotgun, self.screen)
                self.screen.blit(shotgunSprite, self.shotgunRect)

            if(self.machineGun): 
                checkDeco(self.machineGun, self.screen)
                self.screen.blit(machineGunSprite, self.machineGunRect)




class ItemsHUD:

    def __init__(self, items, screen):
        self.screen = screen
        self.healthPots = items["healthPotions"]
        self.manaPots = items["manaPotions"]
        self.active = 1
        self.hPotRect = healthItemIcon.get_rect()
        self.hPotRect = self.hPotRect.move(1492, 843)
        self.mPotRect = manaIcon.get_rect()
        self.mPotRect = self.mPotRect.move(1703, 843)
        self.hPotTextSurface = myfont.render(str(self.healthPots), False, (255, 255, 255))
        self.mPotTextSurface = myfont.render(str(self.manaPots), False, (255, 255, 255))
        self.emptyhPotTextSurface = myfont.render("~", False, (255, 255, 255))
        self.emptymPotTextSurface = myfont.render("~", False, (255, 255, 255))
    def toggle(self): 
        if(self.active): 
            self.active = 0
        else: 
            self.active = 1
        
    def update(self, items): 
        self.healthPots = items["healthPotions"]
        self.manaPots = items["manaPotions"]
        self.hPotTextSurface = myfont.render(str(self.healthPots), False, (255, 255, 255))
        self.mPotTextSurface = myfont.render(str(self.manaPots), False, (255, 255, 255))


    def execute(self):
        if(DEBUG): 
            print(f"{self.active=}, {self.healthPots=}, {self.manaPots=}")

        if(self.active): 
            self.screen.blit(uiBorders, (1475, 825), (2125, 425, 300, 75)) 
            if(self.healthPots): 
                self.screen.blit(self.hPotTextSurface, (1576, 855))
                self.screen.blit(healthItemIcon, self.hPotRect)
            else: 
                self.screen.blit(self.emptyhPotTextSurface, (1580, 855))
            if(self.manaPots): 
                self.screen.blit(self.mPotTextSurface, (1633, 855))
                self.screen.blit(manaIcon, self.mPotRect)
            else: 
                self.screen.blit(self.emptymPotTextSurface, (1636, 855))

