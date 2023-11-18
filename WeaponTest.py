from Weapons import Weapon
from Weapons import FlamingDeco
from time import sleep

handgun = Weapon(5, 3, 31, 5, .3)


for _ in range(0, 1500): 
    print(handgun.use())
    sleep(.01)

handgun = FlamingDeco(handgun)

for _ in range(0, 1500): 
    print(handgun.use())
    sleep(.01)





