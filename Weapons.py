import pygame
from dataclasses import dataclass
from random import randint
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
    deviation: int  # degree of deviation from straight for bullet


# attackSpeed = amount of times per second character can attack
# reloadSpeed = amount of seconds it takes to reload
# ammunition = ammo count before reload
# accuracy = max variation of bullets in degrees
# damageMultiplier = damage multiplier
# base class for weapons
class Weapon:
    def __init__(self, attackSpeed: float, reloadSpeed: float, ammunition: int, accuracy: int, damageMultiplier: float):
        self.attackSpeed = attackSpeed
        self.reloadSpeed = reloadSpeed
        self.maxAmmo = ammunition
        self.acc = accuracy
        self.damageMult = damageMultiplier
        self.reloading = False
        self.lastShotTime = 0
        self.currAmmo = ammunition
        self.damage = Damage("normal", int(100 * self.damageMult), None, 0)  # Initialize the damage attribute

    def use(self) -> Damage:
        if DEBUG:
            print(f"{self.attackSpeed=}, {self.reloadSpeed=}, {self.maxAmmo=}, {self.acc=}, {self.damageMult=}, {self.reloading=}, {self.lastShotTime=}, {self.currAmmo=}")
        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.currAmmo == 0 and not self.reloading:
            self.reloading = True
            return None

        if self.reloading:
            if time() - self.lastShotTime > self.reloadSpeed:
                self.reloading = False
                self.currAmmo = self.maxAmmo
                self.currAmmo -= 1
                return Damage("normal", int(100 * self.damageMult), None, randint(self.acc * -1, self.acc))
            else:
                return None

        if time() - self.lastShotTime < 1 / self.attackSpeed:
            if DEBUG:
                print("time since shot: ", time() - self.lastShotTime)
            return None
        self.lastShotTime = time()
        self.currAmmo -= 1
        return Damage("normal", int(100 * self.damageMult), None, randint(self.acc * -1, self.acc))

    def fire(self, position, direction):
        speed = 5.0  # Placeholder value
        proj = projectiles.create_projectile(position, direction, speed, self.damage.amount)
        game.projectiles.append(proj)


# class for Flaming Deco
class FlamingDeco:
    def __init__(self, weapon):
        self.weapon = weapon

    def use(self) -> Damage:
        if DEBUG:
            print(f"{self.weapon.attackSpeed=}, {self.weapon.reloadSpeed=}, {self.weapon.maxAmmo=}, {self.weapon.acc=}, {self.weapon.damageMult=}, {self.weapon.reloading=}, {self.weapon.lastShotTime=}, {self.weapon.currAmmo=}")
        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.weapon.currAmmo == 0 and not self.weapon.reloading:
            self.weapon.reloading = True
            return None

        if self.weapon.reloading:
            if time() - self.weapon.lastShotTime > self.weapon.reloadSpeed:
                self.weapon.reloading = False
                self.weapon.currAmmo = self.weapon.maxAmmo
                self.weapon.currAmmo -= 1
                return Damage("Fire", int(100 * self.weapon.damageMult), "Flaming", randint(self.weapon.acc * -1, self.weapon.acc))
            else:
                return None

        if time() - self.weapon.lastShotTime < 1 / self.weapon.attackSpeed:
            if DEBUG:
                print("time since shot: ", time() - self.weapon.lastShotTime)
            return None
        self.weapon.lastShotTime = time()
        self.weapon.currAmmo -= 1
        return Damage("Fire", int(100 * self.weapon.damageMult), "Flaming", randint(self.weapon.acc * -1, self.weapon.acc))

    def fire(self, position, direction):
        speed = 5.0  # Placeholder value
        proj = projectiles.create_projectile(position, direction, speed, self.weapon.damage.amount)
        game.projectiles.append(proj)


# class for Frosty Deco
class FrostyDeco:
    def __init__(self, weapon):
        self.weapon = weapon

    def use(self) -> Damage:

        if DEBUG:
            print(f"{self.weapon.attackSpeed=}, {self.weapon.reloadSpeed=}, {self.weapon.maxAmmo=}, {self.weapon.acc=}, {self.weapon.damageMult=}, {self.weapon.reloading=}, {self.weapon.lastShotTime=}, {self.weapon.currAmmo=}")
        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.weapon.currAmmo == 0 and not self.weapon.reloading:
            self.weapon.reloading = True
            return None

        if self.weapon.reloading:
            if time() - self.weapon.lastShotTime > self.weapon.reloadSpeed:
                self.weapon.reloading = False
                self.weapon.currAmmo = self.weapon.maxAmmo
                self.weapon.currAmmo -= 1
                return Damage("Ice", int(100 * self.weapon.damageMult), "Frosty", randint(self.weapon.acc * -1, self.weapon.acc))
            else:
                return None

        if time() - self.weapon.lastShotTime < 1 / self.weapon.attackSpeed:
            if DEBUG:
                print("time since shot: ", time() - self.weapon.lastShotTime)
            return None
        self.weapon.lastShotTime = time()
        self.weapon.currAmmo -= 1
        return Damage("Ice", int(100 * self.weapon.damageMult), "Frosty", randint(self.weapon.acc * -1, self.weapon.acc))

    def fire(self, position, direction):
        speed = 5.0  # Placeholder value
        proj = projectiles.create_projectile(position, direction, speed, self.weapon.damage.amount)
        game.projectiles.append(proj)


# class for Shroom Deco
class ShroomDeco:
    def __init__(self, weapon):
        self.weapon = weapon

    # earth could potentially also be called poison but I don't think it really matters
    def use(self) -> Damage:

        if DEBUG:
            print(f"{self.weapon.attackSpeed=}, {self.weapon.reloadSpeed=}, {self.weapon.maxAmmo=}, {self.weapon.acc=}, {self.weapon.damageMult=}, {self.weapon.reloading=}, {self.weapon.lastShotTime=}, {self.weapon.currAmmo=}")
        # updates will go in here so that a dedicated update() function doesn't need to be called
        if self.weapon.currAmmo == 0 and not self.weapon.reloading:
            self.weapon.reloading = True
            return None

        if self.weapon.reloading:
            if time() - self.weapon.lastShotTime > self.weapon.reloadSpeed:
                self.weapon.reloading = False
                self.weapon.currAmmo = self.weapon.maxAmmo
                self.weapon.currAmmo -= 1
                return Damage("Earth", int(100 * self.weapon.damageMult), "Shroom", randint(self.weapon.acc * -1, self.weapon.acc))
            else:
                return None

        if time() - self.weapon.lastShotTime < 1 / self.weapon.attackSpeed:
            if DEBUG:
                print("time since shot: ", time() - self.weapon.lastShotTime)
            return None
        self.weapon.lastShotTime = time()
        self.weapon.currAmmo -= 1
        return Damage("Earth", int(100 * self.weapon.damageMult), "Shroom", randint(self.weapon.acc * -1, self.weapon.acc))

    def fire(self, position, direction):
        speed = 5.0  # Placeholder value
        proj = projectiles.create_projectile(position, direction, speed, self.weapon.damage.amount)
        game.projectiles.append(proj)
