from Inventory import *
import Weapons
import pygame
from time import sleep
from pygame.math import Vector2

inventory = InventoryManager()
screen = pygame.display.set_mode((45 * 40, 24 * 40))
screen = screen.fill("black")
handgun = Weapon(screen, 5, 3, 30, 5, .3, 1)
shotgun = Weapon(screen, .25, 10, 4, 15, .7, 1)
machineGun = Weapon(screen, 15, 5, 45, 7, .25, 1) 
position = Vector2(0, 0)
direction = 0
inventory.addItem(handgun)
inventory.addItem(shotgun)
inventory.addItem(machineGun)
WTESTS = 1
STESTS = 0
ITESTS = 0
if(WTESTS): 
    for _ in range(0, 1500): 
        val = inventory.useItem(handgun, position, direction)
        if(val): 
            print(val)
        sleep(.01)
    for _ in range(0, 1500): 
        val = inventory.useItem(shotgun, position, direction)
        if(val): 
            print(val)

        sleep(.01)

    for _ in range(0, 1500): 
        val = inventory.useItem(machineGun, position, direction)
        if(val): 
            print(val)
        sleep(.01)

    flamingHandgun = FlamingDeco(screen, handgun)
    inventory.addItem(flamingHandgun)
    sleep(5)

    for _ in range(0, 1500): 
        val = inventory.useItem(flamingHandgun, position, direction)
        if(val): 
            print(val)
        sleep(.01)

    frostyTheSnowmanBlicky = FrostyDeco(screen, handgun)
    inventory.addItem(frostyTheSnowmanBlicky)
    sleep(5)

    for _ in range(0, 1500): 
        val = inventory.useItem(frostyTheSnowmanBlicky, position, direction)
        if(val):
            print(val)
        sleep(.01)

    shroomHandgun = ShroomDeco(screen, handgun)
    inventory.addItem(shroomHandgun)
    sleep(5)

    for _ in range(0, 1500): 
        val = inventory.useItem(shroomHandgun, position, direction)
        if(val): 
            print(val)
        sleep(.01)

#reset test
    inventory.addItem(handgun)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(handgun, position, direction)
        if(val):
            print(val)
        sleep(.01)

#deco override test
    flamingShotty = FlamingDeco(screen, shotgun)
    inventory.addItem(flamingShotty)
    sleep(5)

    for _ in range(0, 1500):
        val = inventory.useItem(flamingShotty, position, direction)
        if(val): 
            print(val)
        sleep(.01)

    frostyShotty = FrostyDeco(screen, shotgun)
    inventory.addItem(frostyShotty)
    sleep(5)

    for _ in range(0, 1500):
        val = inventory.useItem(frostyShotty, position, direction)
        if(val): 
            print(val)
        sleep(.01)

    shroomShotty = ShroomDeco(screen, shotgun)
    inventory.addItem(shroomShotty)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(shroomShotty, position, direction)
        if(val): 
            print(val)
        sleep(.01)

    inventory.addItem(shotgun)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(shotgun, position, direction)
        if(val): 
            print(val)
        sleep(.01)


    flamingUzi = FlamingDeco(screen, machineGun)
    inventory.addItem(flamingUzi)
    sleep(5)
    for _ in range(0, 1500):
        val = inventory.useItem(flamingUzi, position, direction)
        if(val): 
            print(val)
        sleep(.01)

    frostyUzi = FrostyDeco(screen, machineGun)
    inventory.addItem(frostyUzi)
    sleep(5)
    for _ in range(0, 1500):
        val = inventory.useItem(frostyUzi, position, direction)
        if(val): 
            print(val)
        sleep(.01)

    shroomUzi = ShroomDeco(screen, machineGun)
    inventory.addItem(shroomUzi)
    sleep(5)
    for _ in range(0, 1500): 
        val = inventory.useItem(shroomUzi, position, direction)  
        if(val): 
            print(val)
        sleep(.01)

    inventory.addItem(machineGun)
    for _ in range(0, 1500): 
        val = inventory.useItem(machineGun, position, direction)
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



