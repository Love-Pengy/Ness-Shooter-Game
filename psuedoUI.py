#File David made that allows buttons to be created and checked for pressed attribute
import Button.py

#weapons binds but only if we allow weapon switching like this
weaponBinds = [1, 2]
#consumable binds but only if we allow quick consumes
consumableBinds = ['q','e']
pauseBind = 'esc'
#weapons that user starts game with
defaultWeapons = [' ', ' ']
#bind for inventory
inventoryBind = 'tab'
class UIHandler:
    #build all of respective UI's
    def __init__(self, weapons, items, stats, score=0):
        self.iUI = build(InventoryUI(weapons, items))
        self.stHUD = build(StatHUD(stats))
        self.scHUD = build(ScoreHUD(score))
        return(self)
    """THIS DEPENDS ON WHAT WE DECIDE FOR WEAPON/CONSUMABLES BEHIND INVENTORY OR NOT
    #update weapons HUD with the new order of weapons or weapon 
    def updateWeaponHUD(self):
        pass
    #update count of items based off of the new inventory amount
    def updateItemHUD(self):
        pass
    """
    #update stat UI with new stats based off of Player class values
    def updateStatHUD(self):
        update(self.stHUD)
    #bring up pause menu, execute appropriate action based off of button hit
    def showPauseMenu(self):
        '''unhide pause menu somehow'''
        pass
    #update score HUD
    def updateScoreHUD(self, newScore):
        self.scHUD.udpate(score, newScore)
                         

#destroys will just hide the UI's if that's an option maybe just don't draw?
class InventoryUI:
    def __init__(self): 
        self.weapons = defaultWeapons
        self.items = None
        return(self)

    def build(self): 
        '''
        draws the UI to the screen 
        '''
        pass

    def update(self, weapons=None, items=None): 
        '''
        updates values 
        '''
        pass

class StatHUD: 
    def __init__(self): 
        self.attk = 0
        self.defense = 0
        self.speed = 10
        self.hp = 100
        return(self)
    
    def build(self): 
        pass
    
    def update(self, attk = None, defense = None, speed = None, hp = None): 
        #update values
        pass 

class ScoreHUD: 
    def __init__(self): 
        self.score = 0
        return(self)
    
    def build(self): 
        pass

    def update(self, score = None): 
        #update score
        pass
