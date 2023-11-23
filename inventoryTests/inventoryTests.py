from Inventory import *
import Weapons
from time import sleep
inventory = InventoryManager()

handgun = Weapon(5, 3, 30, 5, .3)
shotgun = Weapon(.25, 10, 4, 15, .7)
machineGun = Weapon(15, 5, 45, 7, .25) 

inventory.addItem(handgun)
inventory.addItem(shotgun)
inventory.addItem(machineGun)
WTESTS = 0
STESTS = 0
ITESTS = 1
if(WTESTS): 
    for _ in range(0, 1500): 
        val = inventory.useItem(handgun)
        if(val): 
            print(val)
        sleep(.01)

    for _ in range(0, 1500): 
        val = inventory.useItem(shotgun)
        if(val): 
            print(val)

        sleep(.01)

    for _ in range(0, 1500): 
        val = inventory.useItem(machineGun)
        if(val): 
            print(val)
        sleep(.01)

    flamingHandgun = FlamingDeco(handgun)
    inventory.addItem(flamingHandgun)
    sleep(5)

    for _ in range(0, 1500): 
        val = inventory.useItem(flamingHandgun)
        if(val): 
            print(val)
        sleep(.01)

    frostyTheSnowmanBlicky = FrostyDeco(handgun)
    inventory.addItem(frostyTheSnowmanBlicky)
    sleep(5)

    for _ in range(0, 1500): 
        val = inventory.useItem(frostyTheSnowmanBlicky)
        if(val):
            print(val)
        sleep(.01)

    shroomHandgun = ShroomDeco(handgun)
    inventory.addItem(shroomHandgun)
    sleep(5)

    for _ in range(0, 1500): 
        val = inventory.useItem(shroomHandgun)
        if(val): 
            print(val)
        sleep(.01)

#reset test
    inventory.addItem(handgun)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(handgun)
        if(val):
            print(val)
        sleep(.01)

#deco override test
    flamingShotty = FlamingDeco(shotgun)
    inventory.addItem(flamingShotty)
    sleep(5)

    for _ in range(0, 1500):
        val = inventory.useItem(flamingShotty)
        if(val): 
            print(val)
        sleep(.01)

    frostyShotty = FrostyDeco(shotgun)
    inventory.addItem(frostyShotty)
    sleep(5)

    for _ in range(0, 1500):
        val = inventory.useItem(frostyShotty)
        if(val): 
            print(val)
        sleep(.01)

    shroomShotty = ShroomDeco(shotgun)
    inventory.addItem(shroomShotty)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(shroomShotty)
        if(val): 
            print(val)
        sleep(.01)

    inventory.addItem(shotgun)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(shotgun)
        if(val): 
            print(val)
        sleep(.01)


    flamingUzi = FlamingDeco(machineGun)
    inventory.addItem(flamingUzi)
    sleep(5)
    for _ in range(0, 1500):
        val = inventory.useItem(flamingUzi)
        if(val): 
            print(val)
        sleep(.01)

    frostyUzi = FrostyDeco(machineGun)
    inventory.addItem(frostyUzi)
    sleep(5)
    for _ in range(0, 1500):
        val = inventory.useItem(frostyUzi)
        if(val): 
            print(val)
        sleep(.01)

    shroomUzi = ShroomDeco(machineGun)
    inventory.addItem(shroomUzi)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(shroomUzi)  
        if(val): 
            print(val)
        sleep(.01)

    inventory.addItem(machineGun)
    for _ in range(0, 1500): 
        val = inventory.useItem(machineGun)
        if(val): 
            print(val)
        sleep(.01)

    
#getter tests: 
    print(inventory.getItem(int))
    print(inventory.getItem(Weapon))
    print(inventory.getItem("healthPots"))
    print(inventory.getItem("manaPots"))
    print(inventory.getItem("somethingRandom"))
    sleep(5)



#score tests 
if(STESTS): 
    CHUNKSIZE = 10
    for _ in range(0, 1500): 
        inventory.addItem(CHUNKSIZE)
        print(inventory.getItem(int))
        sleep(.01)

    for _ in range(0, 1500): 
        inventory.useItem(10)
        print(inventory.getItem(int))
        sleep(.01)

    #invalid input test 
    for _ in range(0, 1500): 
        print(inventory.addItem(CHUNKSIZE/2.5))
        print(inventory.getItem(int))
        sleep(.01)

#inventory tests
if(ITESTS): 
    for _ in range(0, 15): 
        inventory.addItem("healthPot")
        print(inventory.items.powerUps)
        print(inventory.getItem("healthPot"))
        sleep(.01)
    for _ in range(0, 15): 
        print(inventory.useItem("healthPot"))
        print(inventory.getItem("healthPot"))
        sleep(.01)
        
    for _ in range(0, 15): 
        inventory.addItem("manaPot")
        print(inventory.getItem("manaPot"))
        sleep(.01)
    for _ in range(0, 15): 
        print(inventory.useItem("manaPot"))
        print(inventory.getItem("manaPot"))
        sleep(.01)
    print(inventory.useItem("manaPot"))
    print(inventory.useItem("healthPot"))
    print(inventory.items.powerUps)

    inventory.addItem("meowBlaster1")
    inventory.addItem("meowBlaster2")
    inventory.addItem("meowBlaster3")
    inventory.addItem("meowBlaster4")
    inventory.addItem("meowBlaster5")
    print(inventory.useItem("meowBlaster1"))
    print(inventory.getItem("meowBlaster1"))
    print(inventory.items.powerUps)
    print(inventory.useItem("meowBlaster1"))



