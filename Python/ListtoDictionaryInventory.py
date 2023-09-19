# List to Dictionary Function for Fantasy Game Inventory
# Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
#
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#
# Write a function named addToInventory(inventory, addedItems), where the inventory parameter
# is a dictionary representing the player’s inventory (like in the previous project) and the
# addedItems parameter is a list like dragonLoot. The addToInventory() function should return
# a dictionary that represents the updated inventory. Note that the addedItems list can contain
# multiples of the same item. Your code could look something like this:
#
# def addToInventory(inventory, addedItems):
#     # your code goes here
#
# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)
#
# The previous program (with your displayInventory() function from the previous project) would output the following:
#
# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
#
# Total number of items: 48
import fantasyInventory

def addToInventory(inventory, addedItems):
    loot_conv = {}
    # Create a Dict with addedItems values
    for key_v in addedItems:
        if key_v in loot_conv:
            loot_conv[key_v] += 1
        if key_v not in loot_conv:
            loot_conv[key_v] = 1

    #"merge" both of the lists
    for key_v in loot_conv:
        if key_v in inventory:
            inventory[key_v] += loot_conv[key_v]
        if key_v not in inventory:
            inventory.update({key_v : 1})

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


inv = addToInventory(inv, dragonLoot)
fantasyInventory.displayInventory(inv)



