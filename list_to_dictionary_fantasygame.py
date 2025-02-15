def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1  # Increase count if item exists
        else:
            inventory[item] = 1  # Add new item with count 1
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v
    print("Total number of items: " + str(total_items))

# Existing inventory
inv = {'gold coin': 42, 'rope': 1}

# New loot
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Update inventory
inv = addToInventory(inv, dragonLoot)

# Display inventory
displayInventory(inv)
