from dataclasses import dataclass


@dataclass
class Damage: 
    type: str 
    amount: int 
    debuff: str


#base class for weapons
class Weapons: 
    def __init__(self, attackSpeed, reloadSpeed, ammunition, accuracy, damageMultiplier): 
        self.attackSpeed = attackSpeed
        self.reloadSpeed = reloadSpeed
        self.ammo = ammunition
        self.acc = accuracy 
        self.damageMult = damageMultiplier
        self.cooldown = None
    
    def isCooldown(self) -> bool: 
        return(self.cooldown)

    def use(self) -> Damage: 
        #updates will go in here so that a dedicated update() function doesnt need to be called    
        return(Damage("normal", (100 * self.damageMult), None))

#class for Flaming Deco
class FlamingDeco: 
    def __init__(self, weapon): 
        self.weapon = weapon

    def isCoolDown(self) -> bool: 
        return(self.weapon.isCooldown())

    def use(self) -> Damage: 
        return(Damage("fire", (100 * self.weapon.damageMult), "Flaming"))

#class for Frosty Deco 
class FrostyDeco: 
    def __init__(self, weapon): 
        self.weapon = weapon

    def isCoolDown(self) -> bool: 
        return(self.weapon.isCooldown())

    def use(self) -> Damage: 
        return(Damage("ice", (100 * self.weapon.damageMult), "Frosty"))
    
#class for Shroom Deco
class ShroomDeco: 
    def __init__(self, weapon): 
        self.weapon = weapon

    def isCooldown(self) -> bool: 
        return(self.weapon.isCoolDown())

    #earth could potentially also be called poison but I dont think it really matters
    def use(self) -> Damage: 
        return(Damage("earth", (100 * self.weapon.damageMult), "Shroom"))
    




