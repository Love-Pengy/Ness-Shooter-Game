#File David made that allows buttons to be created and checked for pressed attribute
from Button import Button
import pygame
DEBUG = 1

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#usage: 
#label = myfont.render("wanted text", num, color)

pistolSprite = pygame.image.load("Assets/Pistol.png")
shotgunSprite = pygame.image.load("Assets/Shotgun.png")
machineGunSprite = pygame.image.load("Assets/MachineGun.png")

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
manaIcon = pygame.image.load("Assets/Mana_Icon.png")

class UIManager:
    #build all of respective UI's
    def __init__(self, weapons, items, stats, score, screen):
        self.wHUD = WeaponsHUD(weapons)
        #self.iHUD = ItemsHUD(items)
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
    
    def update(self, keys, stats, score):
        if(keys[pygame.K_ESCAPE]): 
            self.pMenu.toggle()
        if(not keys[pygame.K_ESCAPE]): 
            self.pMenu.setEligibleToggle()
        if(self.pMenu.active): 
            self.pMenu.execute()
        self.updateStatHUD(stats)
        self.updateScoreHUD(score)
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

        if(DEBUG): 
            print(f"{self.attack=}, {self.defense=}, {self.speed=}, {self.hp=}")
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
        if(DEBUG): 
            print(f"{self.attack=}")
            print(f"{self.defense=}")
            print(f"{self.speed=}")
            print(f"{self.hp=}")

        self.defenseTextSurface = myfont.render(str(self.defense), False, (255, 255,255))
        self.attackTextSurface = myfont.render(str(self.attack), False, (255, 255, 255))
        self.speedTextSurface = myfont.render(str(self.speed), False, (255, 255, 255))
        self.hpTextSurface = myfont.render(str(self.hp), False, (255, 255, 255))

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
            self.screen.blit(self.scoreTextSurface, (930, 15))


class WeaponsHUD: 
    def __init__(self, weapons, screen):
        self.screen = screen
        #will be none if they don't exist
        self.pistol = weapons["pistol"]
        self.shotgun = weapons["shotgun"]
        self.machineGun = weapons["machineGun"]
        self.active = 1
        self.pistolRect = pistolSprite.get_rect()
        self.pistolRect = self.pistolRect.move(950, 950)
        self.shotgunRect = shotgunSprite.get_rect()
        self.shotgunRect = self.shotgunRect.move(1050, 950)
        self.machineGunRect = machineGunSprite.get_rect()
        self.machineGunRect = self.machineGunRect.move(1150, 950)
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
            #write pistol always
            self.screen.blit(pistolSprite, self.pistolRect)
            if(self.shotgun):
                self.screen.blit(shotgunSprite, self.shotgunRect)
            if(self.machineGun): 
                self.screen.blit(machineGunSprite, self.machineGunRect)

