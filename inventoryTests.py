from inventory import *
import Weapons
from time import sleep
inventory = InventoryManager()

handgun = Weapon(5, 3, 30, 5, .3)
shotgun = Weapon(.25, 10, 4, 15, .7)
machineGun = Weapon(15, 5, 45, 7, .25) 

inventory.addItem(handgun)
inventory.addItem(shotgun)
inventory.addItem(machineGun)


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

    

print("YIPPEEE")
