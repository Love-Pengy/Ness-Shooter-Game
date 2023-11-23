# NOTE: EXAMPLES OF ALL OF THIS ARE IN THE TEST FILES
## Weapons
+ all weapons return a Damage dataclass that has the following fields
	+ type: (str)
		+ the type of damage that the weapon holds (this was added as kinda an extra I don't know if its really viable to use this)
		+ This field can have normal, Earth, Fire, and Ice 
	+ amount: (int) 
		+ amount of damage that is dealt. 
	+ debuff: (str)
		+ this is the field that I intended to be checked for our powerups. 
		+ this field can have None, Flaming, Frosty, and Shroom
	+ deviation: (float)
		+ this is the field that specifies how accurate a specific bullet should be 
		+ the number that it outputs is intended to be the amount of degrees off from straight that the bullet will travel
		+ this outputs both negative and positive values
+ For init of a weapon you pass in all of the arguments that will be needed and it will look like this: 
```python
weapon = Weapon(attackSpeed, reloadSpeed, ammunition, accuracy, damageMultiplier)
```

	+ attackSpeed is a float
	+ reloadSpeed is a float
	+ ammunition is an int
	+ accuracy is a float
	+ damageMultiplier is a float
+ To add a deco on top of a weapon you do the same as a normal deco 
	+ the class names are: 
		+ ShroomDeco
		+ FlamingDeco 
		+ FrostyDeco
```python
decoratedWeapon = ShroomDeco(weapon)
```
## Inventory 
+ Notes: 
	+ ammo tracking is abstracted away in the weapon classes so there is no need to keep track of the ammo or reloading functions. they will return none if not eligible to shoot
		+ because of this isCooldown() was put into the various methods and use() will return none if a weapon is on cooldown (AKA is reloading or player has tried to use their weapon too quickly)
	+ I know the inventoryManager is a bit weird, but I honestly ran out of time to properly fix it 
+ Inventory is ran with a manager. None of the specific inventories(weapons, items, and score) should need to be touched directly
+ To init the manager: 
```python
inventory = InventoryManager()
```

+ adding items: 
	+ In order to add items you have to pass in what you want to add. Here are all of the examples: 
	```python
	#To add score you just pass in an int with the value that you want to add
	inventory.addItem(100) # this will add 100 to the score

	#To add a weapon to the inventory you just pass in the weapon 
	inventory.addItem(weapon) #this will append weapon to the list of weapons
	#if you want to add a decorated version of weapon to the inventory you just pass that in and the inventory will replace the same weapon with the decorated version 
	inventory.addItem(decoratedWeapon)

	#if you want to add an item then you pass in a string with the items name
	inventory.addItem("healthPot")
	inventory.addItem("manaPot") # these two strings are the hard coded names for health and mana potions


	#if you add something with another name it will go to the "powerUps" dictionary. These will still be accessable the same way as healthPots and manaPots
	inventory.addItem("meowMeowBlaster3000")
	
```

+ Using Items:
	+ In order to use items you basically do the same thing as adding but with the use method
	+ the use method will return True, False, or None 
		+ methodology for this is when use returns True the operation associated with the call is supposed to be executed 
		+ When False (or None for weapons) the operation is supposed to be ignored

```python
	# to use score
	inventory.use(100) #subtracts 100 from the current score

	#to use potions
	inventory.use("manaPot")
	inventory.use("healthPot") 
	inventory.use("meowMeowBlaster3000") # will subtract 1 from the count of the called potion if a valid number of them is present

	inventory.use(decoratedWeapon) #will return DamageStruct for the associated weapon
```

+ Getting Values:
	+ For UI purposes (and anything else that needs it) there is a getter in the manager as well



