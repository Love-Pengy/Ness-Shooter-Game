from Weapons import Weapon
from Weapons import FlamingDeco
from time import sleep
from Weapons import FrostyDeco
from Weapons import ShroomDeco 

handgun = Weapon(5.5, 3.1, 30, 5.34, .3)
shotgun = Weapon(.25, 10, 4, 15, .7)
machineGun = Weapon(15, 5, 45, 7, .25) 

for i in range(0, 1500):
    output = handgun.use()
    if(output): 
        print(f"handgun: {output=}, {handgun.currAmmo=}")
    sleep(.01)
    
for i in range(0, 1500): 
    output = shotgun.use()
    if(output): 
        print(f"shotgun: {output=}, {shotgun.currAmmo=}")
    sleep(.01)

for i in range(0, 1500): 
    output = machineGun.use()
    if(output): 
        print(f"machineGun: {output=}, {machineGun.currAmmo=}")
    sleep(.01)


FlamingShotgun = FlamingDeco(shotgun)
FlamingMachineGun = FlamingDeco(machineGun)
FlamingHandgun = FlamingDeco(handgun)

for i in range(0, 1500):
    output = FlamingHandgun.use()
    if(output): 
        print(f"FlamingHandgun: {output=}, {FlamingHandgun.weapon.currAmmo=}")
    sleep(.01)

for i in range(0, 1500): 
    output = FlamingShotgun.use()
    if(output): 
        print(f"FlamingShotgun: {output=}, {FlamingShotgun.weapon.currAmmo=}")
    sleep(.01)

for i in range(0, 1500): 
    output = FlamingMachineGun.use()
    if(output): 
        print(f"FlamingMachineGun: {output=}, {FlamingMachineGun.weapon.currAmmo=}")
    sleep(.01)


FrostyHandgun = FrostyDeco(handgun)
FrostyMachineGun = FrostyDeco(machineGun)
FrostyShotgun = FrostyDeco(shotgun)

for i in range(0, 1500): 
    output = FrostyHandgun.use()
    if(output): 
        print(f"FrostyHandgun: {output=}, {FrostyHandgun.weapon.currAmmo=}")
    sleep(.01)

for i in range(0, 1500): 
    output = FrostyShotgun.use()
    if(output): 
        print(f"FrostyShotgun: {output=}, {FrostyShotgun.weapon.currAmmo=}")
    sleep(.01)

for i in range(0,1500): 
    output = FrostyMachineGun.use()
    if(output): 
        print(f"FrostyMachineGun: {output=}, {FrostyMachineGun.weapon.currAmmo=}")
    sleep(.01)



ShroomHandgun = ShroomDeco(handgun) 
ShroomShotgun = ShroomDeco(shotgun)
ShroomMachineGun = ShroomDeco(machineGun)
for i in range(0, 1500): 
    output = ShroomHandgun.use() 
    if(output): 
        print(f"ShroomHandgun: {output=}, {ShroomHandgun.weapon.currAmmo=}")
    sleep(.01)

for i in range(0, 1500): 
    output = ShroomShotgun.use()
    if(output): 
        print(f"ShroomShotgun: {output=}, {ShroomShotgun.weapon.currAmmo=}")
    sleep(.01)

for i in range(0, 1500): 
    output = ShroomMachineGun.use()
    if(output):
        print(f"ShroomMachineGun: {output=}, {ShroomMachineGun.weapon.currAmmo=}")
    sleep(.01)



