import pygame
from dataclasses import dataclass
from random import uniform
from time import time
import projectiles
from pygame.math import Vector2

# site for learning about random library
# https://docs.python.org/3/library/random.html#random.randrange

DEBUG = 0

# driver struct for weapon actions
@dataclass
class Damage:
    type: str  # damage type (may or may not be used)
    amount: int  # damage amount
    debuff: str  # debuff AKA powerups/decos added to weapons
    deviation: float  # degree of deviation from straight for bullet



# attackSpeed = amount of times per second character can attack
# reloadSpeed = amount of seconds it takes to reload
# ammunition = ammo count before reload
# accuracy = max variation of bullets in degrees
# damageMultiplier = damage multiplier
# projectileSpeeed = speed at which the projectiles travel 

# base class for weapons
class Weapon:
    def __init__(self, game, attackSpeed: float, reloadSpeed: float, ammunition: int, accuracy: float, damageMultiplier: float, projectileSpeed: float):

        self.game = game
        self.attackSpeed = attackSpeed
        self.reloadSpeed = reloadSpeed
        self.maxAmmo = ammunition
        self.acc = accuracy
        self.damageMult = damageMultiplier
        self.reloading = False
        self.lastShotTime = 0
        self.currAmmo = ammunition
        self.damage = None
        self.projSpeed = projectileSpeed

    def use(self, position, player_direction):

        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.currAmmo == 0 and not self.reloading:
            self.reloading = True
            return None

        if self.reloading:
            if ((time() - self.lastShotTime) > self.reloadSpeed):
                self.reloading = False
                self.currAmmo = self.maxAmmo
                self.currAmmo -= 1
                self.damage = Damage("normal", int(100 * self.damageMult), None, round(uniform((self.acc * -1), self.acc), 1))
                self.lastShotTime = time()
                return [projectiles.create_projectile(position, player_direction, self.projSpeed, self.damage.amount)]
            else:
                return None

        if (time() - self.lastShotTime) < (1 / self.attackSpeed):
            return None
        self.lastShotTime = time()
        self.currAmmo -= 1
        self.damage = Damage("normal", int(100 * self.damageMult), None, round(uniform((self.acc * -1), self.acc), 1))
        return [projectiles.create_projectile(position, player_direction, self.projSpeed, self.damage.amount)]
    
    def update(self): 
        #print("HERE", self.reloading)
        if self.currAmmo == 0 and not self.reloading:
            self.reloading = True
            return

        if(self.reloading): 
            if ((time() - self.lastShotTime) > self.reloadSpeed):
                self.reloading = False
                self.currAmmo = self.maxAmmo


    def __eq__(self, compare):
        if(isinstance(compare, Weapon)): 
            if(self.reloadSpeed == compare.reloadSpeed): 
               if(self.attackSpeed == compare.attackSpeed): 
                    if(self.maxAmmo == compare.maxAmmo): 
                        if(self.acc == compare.acc): 
                            if(self.damageMult == compare.damageMult):
                                if(self.projSpeed == compare.projSpeed): 
                                    return(True)
            return(False)
        else: 
            if(self.attackSpeed == compare.weapon.attackSpeed): 
                if(self.reloadSpeed == compare.weapon.reloadSpeed): 
                    if(self.maxAmmo == compare.weapon.maxAmmo): 
                        if(self.acc == compare.weapon.acc): 
                            if(self.damageMult == compare.weapon.damageMult): 
                                if(self.projSpeed == compare.weapon.projSpeed):
                                    return(True)
            return(False)


# class for Flaming Deco
class FlamingDeco:
    def __init__(self, game, weapon):
        self.weapon = weapon

    def use(self, position, player_direction):
        if DEBUG:
            print(f"{self.weapon.attackSpeed=}, {self.weapon.reloadSpeed=}, {self.weapon.maxAmmo=}, {self.weapon.acc=}, {self.weapon.damageMult=}, {self.weapon.reloading=}, {self.weapon.lastShotTime=}, {self.weapon.currAmmo=}")
        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.weapon.currAmmo == 0 and not self.weapon.reloading:
            self.weapon.reloading = True
            return None

        if self.weapon.reloading:
            if ((time() - self.weapon.lastShotTime) > self.weapon.reloadSpeed):
                self.weapon.reloading = False
                self.weapon.currAmmo = self.weapon.maxAmmo
                self.weapon.currAmmo -= 1
                self.weapon.damage = Damage("Fire", int(100 * self.weapon.damageMult), "Flaming", round(uniform((self.weapon.acc * -1), self.weapon.acc), 1))
                return [projectiles.create_projectile(position, player_direction, self.weapon.projSpeed, self.weapon.damage.amount)]
            else:
                return None

        if (time() - self.weapon.lastShotTime) < (1 / self.weapon.attackSpeed):
            if DEBUG:
                print("time since shot: ", time() - self.weapon.lastShotTime)
            return None
        self.weapon.lastShotTime = time()
        self.weapon.currAmmo -= 1
        self.weapon.damage = Damage("Fire", int(100 * self.weapon.damageMult), "Flaming", round(uniform((self.weapon.acc * -1), self.weapon.acc), 1))
        return [projectiles.create_projectile(position, player_direction, self.weapon.projSpeed, self.weapon.damage.amount)]

    def update(self): 
        if(self.reloading): 
            if ((time() - self.lastShotTime) > self.reloadSpeed):
                self.reloading = False
                self.currAmmo = self.maxAmmo

    def __eq__(self, compare): 
        if(isinstance(compare, Weapon)): 
            if(self.weapon.attackSpeed == compare.attackSpeed): 
                if(self.weapon.reloadSpeed == compare.reloadSpeed): 
                    if(self.weapon.maxAmmo == compare.maxAmmo): 
                        if(self.weapon.acc == compare.acc): 
                            if(self.weapon.damageMult == compare.damageMult): 
                                return(True)
            return(False)
        else: 
            if(self.weapon.attackSpeed == compare.weapon.attackSpeed): 
                if(self.weapon.reloadSpeed == compare.weapon.reloadSpeed): 
                    if(self.weapon.maxAmmo == compare.weapon.maxAmmo): 
                        if(self.weapon.acc == compare.weapon.acc): 
                            if(self.weapon.damageMult == compare.weapon.damageMult): 
                                if(self.weapon.projSpeed == compare.weapon.projSpeed): 
                                    return(True)
            return(False)


            
# class for Frosty Deco
class FrostyDeco:
    def __init__(self, game, weapon):
        self.weapon = weapon

    def use(self, position, player_direction):
        if DEBUG:
            print(f"{self.weapon.attackSpeed=}, {self.weapon.reloadSpeed=}, {self.weapon.maxAmmo=}, {self.weapon.acc=}, {self.weapon.damageMult=}, {self.weapon.reloading=}, {self.weapon.lastShotTime=}, {self.weapon.currAmmo=}")
        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.weapon.currAmmo == 0 and not self.weapon.reloading:
            self.weapon.reloading = True
            return None

        if self.weapon.reloading:
            if ((time() - self.weapon.lastShotTime) > self.weapon.reloadSpeed):
                self.weapon.reloading = False
                self.weapon.currAmmo = self.weapon.maxAmmo
                self.weapon.currAmmo -= 1
                self.weapon.damage = Damage("Ice", int(100 * self.weapon.damageMult), "Frosty", round(uniform((self.weapon.acc * -1), self.weapon.acc), 1))
                return [projectiles.create_projectile(position, player_direction, self.weapon.projSpeed, self.weapon.damage.amount)]
            else:
                return None

        if (time() - self.weapon.lastShotTime) < (1 / self.weapon.attackSpeed):
            if DEBUG:
                print("time since shot: ", time() - self.weapon.lastShotTime)
            return None
        self.weapon.lastShotTime = time()
        self.weapon.currAmmo -= 1
        self.weapon.damage = Damage("Ice", int(100 * self.weapon.damageMult), "Frosty", round(uniform((self.weapon.acc * -1), self.weapon.acc), 1))
        return [projectiles.create_projectile(position, player_direction, self.weapon.projSpeed, self.weapon.damage.amount)]

    def update(self): 
        if(self.reloading): 
            if ((time() - self.lastShotTime) > self.reloadSpeed):
                self.reloading = False
                self.currAmmo = self.maxAmmo
    
    def __eq__(self, compare): 
        if(isinstance(compare, Weapon)): 
            if(self.weapon.attackSpeed == compare.attackSpeed): 
                if(self.weapon.reloadSpeed == compare.reloadSpeed): 
                    if(self.weapon.maxAmmo == compare.maxAmmo): 
                        if(self.weapon.acc == compare.acc): 
                            if(self.weapon.damageMult == compare.damageMult): 
                                return(True)
            return(False)
        else: 
            if(self.weapon.attackSpeed == compare.weapon.attackSpeed): 
                if(self.weapon.reloadSpeed == compare.weapon.reloadSpeed): 
                    if(self.weapon.maxAmmo == compare.weapon.maxAmmo): 
                        if(self.weapon.acc == compare.weapon.acc): 
                            if(self.weapon.damageMult == compare.weapon.damageMult): 
                                if(self.weapon.projSpeed == compare.weapon.projSpeed): 
                                    return(True)
            return(False)


# class for Shroom Deco
class ShroomDeco:
    def __init__(self, game, weapon):
        self.weapon = weapon

    # earth could potentially also be called poison but I don't think it really matters
    def use(self, position, player_direction):
        if DEBUG:
            print(f"{self.weapon.attackSpeed=}, {self.weapon.reloadSpeed=}, {self.weapon.maxAmmo=}, {self.weapon.acc=}, {self.weapon.damageMult=}, {self.weapon.reloading=}, {self.weapon.lastShotTime=}, {self.weapon.currAmmo=}")
        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.weapon.currAmmo == 0 and not self.weapon.reloading:
            self.weapon.reloading = True
            return None

        if self.weapon.reloading:
            if ((time() - self.weapon.lastShotTime) > self.weapon.reloadSpeed):
                self.weapon.reloading = False
                self.weapon.currAmmo = self.weapon.maxAmmo
                self.weapon.currAmmo -= 1
                self.weapon.damage = Damage("Earth", int(100 * self.weapon.damageMult), "Frosty", round(uniform((self.weapon.acc * -1), self.weapon.acc), 1))
                return [projectiles.create_projectile(position, player_direction, self.weapon.projSpeed, self.weapon.damage.amount)]
            else:
                return None

        if (time() - self.weapon.lastShotTime) < (1 / self.weapon.attackSpeed):
            if DEBUG:
                print("time since shot: ", time() - self.weapon.lastShotTime)
            return None
        self.weapon.lastShotTime = time()
        self.weapon.currAmmo -= 1
        self.weapon.damage = Damage("Earth", int(100 * self.weapon.damageMult), "Shroom", round(uniform((self.weapon.acc * -1), self.weapon.acc), 1))
        return [projectiles.create_projectile(position, player_direction, self.weapon.projSpeed, self.weapon.damage.amount)]

    def update(self): 
        if(self.reloading): 
            if ((time() - self.lastShotTime) > self.reloadSpeed):
                print("UPDATED")
                self.reloading = False
                self.currAmmo = self.maxAmmo

    def __eq__(self, compare): 
        if(isinstance(compare, Weapon)): 
            if(self.weapon.attackSpeed == compare.attackSpeed): 
                if(self.weapon.reloadSpeed == compare.reloadSpeed): 
                    if(self.weapon.maxAmmo == compare.maxAmmo): 
                        if(self.weapon.acc == compare.acc): 
                            if(self.weapon.damageMult == compare.damageMult): 
                                return(True)
            return(False)
        else: 
            if(self.weapon.attackSpeed == compare.weapon.attackSpeed): 
                if(self.weapon.reloadSpeed == compare.weapon.reloadSpeed): 
                    if(self.weapon.maxAmmo == compare.weapon.maxAmmo): 
                        if(self.weapon.acc == compare.weapon.acc): 
                            if(self.weapon.damageMult == compare.weapon.damageMult): 
                                if(self.weapon.projSpeed == compare.weapon.projSpeed): 
                                    return(True)
            return(False)

