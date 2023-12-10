#asset sites: 
# https://www.ludicarts.com/free-rpg-icons/
# https://opengameart.org/content/larger-simple-heart
# https://opengameart.org/content/golden-ui
# https://opengameart.org/content/rpg-ui-icons
from Weapons import Weapon
from Weapons import FlamingDeco
from Weapons import FrostyDeco
from Weapons import ShroomDeco
from Button import Button
from time import time
import pygame
DEBUG = 0
# https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangles-and-polygons-in-pygame # got function to draw semi-transparent shape from here
# https://www.pygame.org/docs/ref/surface.html // learning what SRCALPHA is

def draw_rect_alpha(screen, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    screen.blit(shape_surf, rect)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


uiBorders = pygame.image.load("UIAssets/UIBorders.png")
uiBorders = pygame.transform.scale_by(uiBorders, 3)

uiBorders2 = pygame.image.load("UIAssets/UIBorders2.png")
uiBorders2 = pygame.transform.scale_by(uiBorders2, 1.5)


currManaIcon = pygame.image.load("UIAssets/manaIcon.png")
currManaIcon = pygame.transform.scale(currManaIcon, (55, 45))

pistolSprite = pygame.image.load("UIAssets/Pistol.png")
pistolSprite = pygame.transform.scale(pistolSprite, (55, 45))
shotgunSprite = pygame.image.load("UIAssets/Shotgun.png")
shotgunSprite = pygame.transform.scale(shotgunSprite, (55, 45))
machineGunSprite = pygame.image.load("UIAssets/MachineGun.png")
machineGunSprite = pygame.transform.scale(machineGunSprite, (55, 45))

healthIcon = pygame.image.load("UIAssets/Health_Icon.png")
healthIcon = pygame.transform.scale(healthIcon, (40, 40))
continueButton = pygame.image.load("UIAssets/ContinueButton.png")
exitButton = pygame.image.load("UIAssets/ExitButton.png")
baseDamageIcon = pygame.image.load("UIAssets/Damage_Icon_Base.png")
baseDamageIcon = pygame.transform.scale(baseDamageIcon, (50, 50))
#https://stackoverflow.com/questions/27576645/how-to-overcome-python-fonts-pygame-not-being-loaded
frostyDamageIcon = pygame.image.load("UIAssets/Damage_Icon_Frosty.png")
flamingDamageIcon = pygame.image.load("UIAssets/Damage_Icon_Flaming.png")
speedIcon = pygame.image.load("UIAssets/Speed_Icon.png")
speedIcon = pygame.transform.scale(speedIcon, (50, 50))
defenseIcon = pygame.image.load("UIAssets/Defense_Icon.png")
defenseIcon = pygame.transform.scale(defenseIcon, (40, 40))
healthItemIcon = pygame.image.load("UIAssets/Health_Item_Icon.png")
healthItemIcon = pygame.transform.scale(healthItemIcon, (40, 40))
manaIcon = pygame.image.load("UIAssets/Mana_Icon.png")
manaIcon = pygame.transform.scale(manaIcon, (40, 40))

class UIManager:
    def __init__(self, weapons, items, stats, score, inventory, screen):
        self.wHUD = WeaponsHUD(inventory, screen)
        self.iHUD = ItemsHUD(inventory, screen)
        self.stHUD = StatHUD(stats, screen)
        self.scHUD = ScoreHUD(score, screen)
        self.pMenu = PauseMenu(screen)
        self.inventory = inventory

    def update(self, keys, stats):
        changeGun = None #bars
        if(keys[pygame.K_ESCAPE]): 
            self.pMenu.toggle()
        if(not keys[pygame.K_ESCAPE]): 
            self.pMenu.setEligibleToggle()
        if(self.pMenu.active): 
            self.pMenu.execute()
        if(keys[pygame.K_1]):
            changeGun = 0
        elif(keys[pygame.K_2]): 
            changeGun = 1
        elif(keys[pygame.K_3]): 
            changeGun = 2
            
        self.stHUD.update(stats)
        self.scHUD.update(self.inventory.getItem(int))
        self.wHUD.update(changeGun)
        self.iHUD.update()
        self.iHUD.execute()
        self.wHUD.execute()
        self.stHUD.execute()
        self.scHUD.execute()

class PauseMenu: 
    
    def __init__(self, screen): 
        self.continueB = Button(screen, 200, 480, continueButton)
        self.exitB = Button(screen, 1300, 480, exitButton)
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



class StatHUD:

    def __init__(self, stats, screen):
        self.attack = stats.get("Attack")
        self.defense = stats.get("Defense")
        self.speed = stats.get("Speed")
        self.hp = stats.get("HP")
        self.mana = stats.get("Mana")
        self.screen = screen
        self.active = 1
        self.attackRect = baseDamageIcon.get_rect()
        self.attackRect = self.attackRect.move(10, 900)
        self.attackTextSurface = myfont.render(str(self.attack), False, (255,255, 255))
        self.defenseRect = defenseIcon.get_rect()
        self.defenseRect = self.defenseRect.move(100, 910)
        self.defenseTextSurface = myfont.render(str(self.defense), False, (255, 255, 255))
        self.speedRect = speedIcon.get_rect()
        self.speedRect = self.speedRect.move(185, 905)
        self.speedTextSurface = myfont.render(str(self.speed), False, (255, 255, 255))
        self.hpRect = healthIcon.get_rect()
        self.hpRect = self.hpRect.move(265, 912)
        self.hpTextSurface = myfont.render(str(self.hp), False, (255, 255, 255))
        self.currManaRect = manaIcon.get_rect()
        self.currManaRect = self.currManaRect.move(360, 910) 
        
    def toggle(self): 
        if(self.active): 
            self.active = 0
        else: 
            self.active = 1

    def update(self, stats): 
        self.attack = stats.get("Attack")
        self.defense = stats.get("Defense")
        self.speed = stats.get("Speed")
        self.hp = stats.get("HP")
        self.mana = stats.get("Mana")
        
        self.defenseTextSurface = myfont.render(str(self.defense), False, (255, 255,255))
        self.attackTextSurface = myfont.render(str(self.attack), False, (255, 255, 255))
        self.speedTextSurface = myfont.render(str(self.speed), False, (255, 255, 255))
        self.hpTextSurface = myfont.render(str(self.hp), False, (255, 255, 255))
        self.currManaTextSurface = myfont.render(str(self.mana), False, (255, 255, 255))

    def execute(self): 
        if(self.active): 
            draw_rect_alpha(self.screen, (0, 0, 0, 75), (0, 900, 465, 65))
            self.screen.blit(baseDamageIcon, self.attackRect)
            self.screen.blit(self.attackTextSurface, (65,920))
            self.screen.blit(defenseIcon, self.defenseRect)
            self.screen.blit(self.defenseTextSurface, (155,920))
            self.screen.blit(speedIcon, self.speedRect)
            self.screen.blit(self.speedTextSurface, (245, 920))
            self.screen.blit(healthIcon, self.hpRect)
            self.screen.blit(self.hpTextSurface, (320, 920))
            self.screen.blit(self.currManaTextSurface, (420, 920))
            self.screen.blit(currManaIcon, self.currManaRect)


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
            self.screen.blit(uiBorders2, (817, 0), (250, 275, 165, 50)) 
            self.screen.blit(self.scoreTextSurface, (900, 15))

def checkDeco(weapon, screen): 
    if(isinstance(weapon, FlamingDeco)):
        screen.blit(uiBorders, (1400, 250), (145, 360, 47, 50))
    elif(isinstance(weapon, FrostyDeco)): 
        screen.blit(uiBorders, (1450, 250), (95, 360, 47, 50))
    elif(isinstance(weapon, ShroomDeco)): 
        screen.blit(uiBorders, (1500, 250), (45, 360, 50, 50))
    else:
        pass


class WeaponsHUD: 
    def __init__(self, inventory, screen):
        self.screen = screen
        self.inventory = inventory
        self.pistol = self.inventory.getItem(Weapon, 0)
        self.shotgun = self.inventory.getItem(Weapon, 1)
        self.machineGun = self.inventory.getItem(Weapon, 2)
        self.active = 1
        self.pistolRect = pistolSprite.get_rect()
        self.pistolRect = self.pistolRect.move(1522, 885)
        self.shotgunRect = shotgunSprite.get_rect()
        self.shotgunRect = self.shotgunRect.move(1595, 885)
        self.machineGunRect = machineGunSprite.get_rect()
        self.machineGunRect = self.machineGunRect.move(1665, 885)
        self.activeGun = 0
        self.pistolCurrAmmo = myfont.render(str(0), False, (255, 255, 255))
        self.shotgunCurrAmmo = myfont.render(str(0), False, (255, 255, 255))
        self.machineGunCurrAmmo = myfont.render(str(0), False, (255, 255, 255))
        self.pistolReloadTime = myfont.render(str(0), False, (255, 0, 0))
        self.shotgunReloadTime = myfont.render(str(0), False, (255, 0, 0))
        self.machineGunReloadTime = myfont.render(str(0), False, (255, 0, 0))
        
        
    def toggle(self): 
        if(self.active): 
            self.active = 0
        else: 
            self.active = 1
        
    def update(self, gunChange=None):
        self.inventory.weapons.update()
        self.pistol = self.inventory.getItem(Weapon, 0)
        self.shotgun = self.inventory.getItem(Weapon, 1)
        self.machineGun = self.inventory.getItem(Weapon, 2)
        
        self.pistolCurrAmmo = myfont.render(str(self.pistol.currAmmo), False, (255, 255, 255))
        if(self.pistol.reloading): 
            self.pistolReloadTime = myfont.render(str(round((self.pistol.reloadSpeed - (time() - self.pistol.lastShotTime)), 1)), False, (255, 0, 0))
        else: 
            self.pistolReloadTime = None

        if(self.shotgun):
            if(self.shotgun.reloading): 
                self.shotgunReloadTime = myfont.render(str(round((self.shotgun.reloadSpeed - (time() - self.shotgun.lastShotTime)), 1)), False, (255, 0, 0))
            else: 
                self.shotgunCurrAmmo = myfont.render(str(self.shotgun.currAmmo), False, (255, 255, 255))
                self.shotgunReloadTime = None

        if(self.machineGun):
            if(self.machineGun.reloading): 
                self.machineGunReloadTime = myfont.render(str(round((self.machineGun.reloadSpeed - (time() - self.machineGun.lastShotTime)), 1)), False, (255, 0, 0))
            else: 
                self.machineGunCurrAmmo = myfont.render(str(self.machineGun.currAmmo), False, (255, 255, 255))
                self.machineGunReloadTime = None
        
        if(gunChange is not None): 
            if(gunChange == 0): 
                if(self.pistol): 
                    self.activeGun = gunChange
            elif(gunChange == 1): 
                if(self.shotgun):  
                    self.activeGun = gunChange
            else: 
                if(self.machineGun): 
                    self.activeGun = gunChange
            



    def execute(self):
        if(self.active):
            self.screen.blit(uiBorders, (1500, 875), (2300, 150, 250, 75))

            if(self.activeGun == 0): 
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1507, 875, 77, 73), 5, 5)
            elif(self.activeGun == 1): 
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1581, 875, 80, 73), 5, 5)
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1655, 875, 78, 73), 5, 5)

        if(self.pistol):
            checkDeco(self.pistol, self.screen)
            self.screen.blit(pistolSprite, self.pistolRect)

            if(self.pistolReloadTime): 
                self.screen.blit(self.pistolReloadTime, (1535, 900))
            else: 
                self.screen.blit(self.pistolCurrAmmo, (1557,925))

        if(self.shotgun):
            checkDeco(self.shotgun, self.screen)
            self.screen.blit(shotgunSprite, self.shotgunRect)
            if(self.shotgunReloadTime): 
                self.screen.blit(self.shotgunReloadTime, (1613, 900))
            else: 
                self.screen.blit(self.shotgunCurrAmmo, (1640,925))

        if(self.machineGun): 
            checkDeco(self.machineGun, self.screen)
            self.screen.blit(machineGunSprite, self.machineGunRect)
            if(self.machineGunReloadTime): 
                self.screen.blit(self.machineGunReloadTime, (1680, 900))
            else:
                self.screen.blit(self.machineGunCurrAmmo, (1705,925))


class ItemsHUD:

    def __init__(self, inventory, screen):
        self.screen = screen
        self.inventory = inventory
        self.healthPots = self.inventory.getItem("healthPot")
        self.manaPots = self.inventory.getItem("manaPot")
        self.active = 1
        self.hPotRect = healthItemIcon.get_rect()
        self.hPotRect = self.hPotRect.move(1492, 743)
        self.mPotRect = manaIcon.get_rect()
        self.mPotRect = self.mPotRect.move(1703, 743)
        self.hPotTextSurface = myfont.render(str(self.healthPots), False, (255, 255, 255))
        self.mPotTextSurface = myfont.render(str(self.manaPots), False, (255, 255, 255))
        self.emptyhPotTextSurface = myfont.render("~", False, (255, 255, 255))
        self.emptymPotTextSurface = myfont.render("~", False, (255, 255, 255))

    def toggle(self): 
        if(self.active): 
            self.active = 0
        else: 
            self.active = 1
        
    def update(self): 
        self.healthPots = self.inventory.getItem("healthPot")
        self.manaPots = self.inventory.getItem("manaPot")
        self.hPotTextSurface = myfont.render(str(self.healthPots), False, (255, 255, 255))
        self.mPotTextSurface = myfont.render(str(self.manaPots), False, (255, 255, 255))


    def execute(self):
        if(self.active): 
            self.screen.blit(uiBorders, (1475, 790), (2125, 430, 300, 70)) 
            if(self.healthPots): 
                self.screen.blit(self.hPotTextSurface, (1576, 815))
                self.screen.blit(healthItemIcon, self.hPotRect)
            else: 
                self.screen.blit(self.emptyhPotTextSurface, (1580, 815))

            if(self.manaPots): 
                self.screen.blit(self.mPotTextSurface, (1633, 815))
                self.screen.blit(manaIcon, self.mPotRect)
            else: 
                self.screen.blit(self.emptymPotTextSurface, (1636, 815))

