from Weapons import Weapon
from Weapons import FlamingDeco
from Weapons import FrostyDeco 
from Weapons import ShroomDeco
from Weapons import Damage
DEBUG = 0

def getIndexToReplace(weaponOP, weaponList: list): 
    for weaponI in weaponList:
        if(weaponOP == weaponI): 
            return(weaponList.index(weaponI))
    return(None)

class InventoryManager: 
    def __init__(self): 
        self.weapons = WeaponInventory()
        self.items = ItemsInventory()
        self.score = ScoreInventory()
       
    def addItem(self, item): 
        if(isinstance(item, int)): 
            self.score.add(item)
            return
        if((isinstance(item, Weapon)) or (isinstance(item, FlamingDeco)) or (isinstance(item, FrostyDeco)) or (isinstance(item, ShroomDeco))): 
            self.weapons.add(item)
            return
        self.items.add(item)

    def useItem(self, item, position=None, direction=None): 
        if(isinstance(item, int)): 
            return(self.score.use(item))
        if(isinstance(item, str)): 
            return(self.items.use(item))
        else: 
            return(self.weapons.use(item, position, direction))

    def getItem(self, itemType, index=None): 
        if(itemType is Weapon): 
            if(index is not None):
                if(index >= len(self.weapons.get())):
                   return(None)
                return(self.weapons.get(index))
            return(self.weapons.get())
        if(itemType is int): 
            return(self.score.get())
        if(isinstance(itemType, str)): 
            return(self.items.get(itemType))
        return(None)

class WeaponInventory: 
    
    def __init__(self): 
        self.weapons = list()

    def add(self, item): 
        if(isinstance(item, Weapon) and not(len(self.weapons) == 3)):
            self.weapons.append(item)
            return
        if(isinstance(item, Weapon) and (len(self.weapons) == 3)):
            self.weapons[getIndexToReplace(item, self.weapons)] = item
            return
        if(isinstance(item, FlamingDeco)):
            self.weapons[getIndexToReplace(item, self.weapons)] = item
            return
        if(isinstance(item, FrostyDeco)): 
            self.weapons[getIndexToReplace(item, self.weapons)] = item
            return
        if(isinstance(item, ShroomDeco)): 
            self.weapons[getIndexToReplace(item, self.weapons)] = item
            return
        print("ERROR: INVALID ITEM PASSED TO 'addItem' IN 'WeaponInventory'")
        return

    def use(self, item, position, direction) -> Damage:
            index = getIndexToReplace(item, self.weapons)
            if(index is not None): 
                return(self.weapons[getIndexToReplace(item, self.weapons)].use(position, direction))
            else: 
                return(None)

    def update(self): 
        for i in range(0, len(self.weapons)): 
            if(self.weapons[i]): 
                self.weapons[i].update()

    def get(self, index=None): 
        if(index is not None): 
            return(self.weapons[index])
        return(self.weapons)

class ItemsInventory: 
    
    def __init__(self): 
        self.healthPots = 0
        self.manaPots = 0
        self.powerUps = dict() 
    
    def add(self, item: str):
        if(item == "healthPot"): 
            self.healthPots += 1

        if(item == "manaPot"): 
            self.manaPots += 1
            
        else:
            if(item in self.powerUps): 
               self.powerUps[item] += 1
            else: 
                self.powerUps[item] = 1
    
    def use(self, item: str) -> bool: 
        if(item == "healthPot"): 
            if(self.healthPots == 0): 
                return(False)
            self.healthPots -= 1
            return(True)
        elif(item == "manaPot"): 
            if(self.manaPots == 0):
                return(False)
            self.manaPots -= 1
            return(True)
        elif(item in self.powerUps): 
            if(self.powerUps[item] == 0): 
                return(False)
            self.powerUps[item] -= 1
            return(True)
        else: 
            print("INVALID ITME PASSED TO 'use' IN 'ItemInventory'")

    def get(self, item) -> int: 
        if(item == "healthPot"):
            return(self.healthPots)
        if(item == "manaPot"): 
            return(self.manaPots)
        if(item in self.powerUps): 
            return(self.powerUps[item])

class ScoreInventory: 
    def __init__(self): 
        self.score = 0

    def add(self, score: int) -> bool:
        if(isinstance(score, int)): 
            self.score += score
        else: 
            print("INVALID TYPE PASSED TO 'add' IN 'ScoreInventory'")

    def use(self, score) -> bool: 
        if(isinstance(score, int)): 
            self.score -= score
            return(True)
        else: 
           print("INVALID TYPE PASSED TO 'remove' IN 'ScoreInventory'")
           return(False)
    
    def get(self) -> int: 
        return(self.score)
