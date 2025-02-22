def addToInventory(inventory, dragonLoot):  # Function to add items to inventory
    for item in dragonLoot:
        inventory[item] = inventory.get(item, 0) + 1  # Adds item or increments count
    return inventory  # Return updated inventory

def displayInventory(inventory):  # Function to display inventory
    print("Inventory:")
    total_items = 0  # Item count starts from 0
    for k, v in inventory.items():  # Loop through key-value pairs in inventory
        print("{} {}".format(v, k))  # Using .format() instead of f-strings
        total_items += v  # Add item count to total
    print("Total number of items: {}".format(total_items))  # Print total count

# Define Inventory & Loot
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Update Inventory with Loot
inventory = addToInventory(inventory, dragonLoot)

# Display Updated Inventory
displayInventory(inventory)
