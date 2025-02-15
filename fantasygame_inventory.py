inventory = {'rope':1, 'torch':6, 'gold coin':46, 'dagger':1, 'arrow':12} #created an dictionary inventory which stores keys and values of it

def displayInventory(inventory): #created a function to print inventory
    print("inventory")
    total_items = 0 #intial total items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items = total_items +  v
    print("total number of items:" + str(total_items))

displayInventory(inventory)

