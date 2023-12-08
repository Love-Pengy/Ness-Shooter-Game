from Weapons import Weapon
from Weapons import FlamingDeco
from Weapons import FrostyDeco 
from Weapons import ShroomDeco
from Weapons import Damage
DEBUG = 0

#finds the corresponding index to an identical weapon regardless of whether or not its a deco (sorry for the if statements couldnt find a better way)
def getIndexToReplace(weaponOP, weaponList: list): 
    if(DEBUG): 
        print("INDEXTOREPLACE: ", type(weaponOP))
        if(isinstance(weaponOP, Weapon)): 
            print("1")
        if(isinstance(weaponOP, FlamingDeco)): 
            print("2")
    for weaponI in weaponList:
        if(weaponOP == weaponI): 
            return(weaponList.index(weaponI))
    return(None)

#need getter functionality for the inventory
class InventoryManager: 
    def __init__(self): 
        self.weapons = WeaponInventory()
        self.items = ItemsInventory()
        self.score = ScoreInventory()
       
    def addItem(self, item): 
        if(isinstance(item, int)): 
            if(DEBUG): 
                print("ADDED SCORE")
            self.score.add(item)
            return
        if((isinstance(item, Weapon)) or (isinstance(item, FlamingDeco)) or (isinstance(item, FrostyDeco)) or (isinstance(item, ShroomDeco))): 
            if(DEBUG): 
                print("ADDED WEAPON")
            self.weapons.add(item)
            return
        if(DEBUG): 
            print("ADDED ITEM")
        self.items.add(item)

    #returns true if item should have the associated action ran through or dict/none if weapon 
    def useItem(self, item, position=None, direction=None): 
        if(isinstance(item, int)): 
            return(self.score.use(item))
        if(isinstance(item, str)): 
            return(self.items.use(item))
        else: 
            return(self.weapons.use(item, position, direction))
    #itemType can be passed Weapon, str (where you specify what it is. Ex. healtPots), or int (score)
    #returns None if nonvalid itemType
    def getItem(self, itemType): 
        if(itemType is Weapon): 
            return(self.weapons.get())
        if(itemType is int): 
            return(self.score.get())
        if(isinstance(itemType, str)): 
            return(self.items.get(itemType))
        return(None)

#possible instances: 
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
            if(DEBUG): 
                print("FLAMING DECO")
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
            if(DEBUG): 
                print(index)
            if(index is not None): 
                return(self.weapons[getIndexToReplace(item, self.weapons)].use(position, direction))
            else: 
                return(None)
    def get(self): 
        print(self.weapons)

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
