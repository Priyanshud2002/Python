myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
myCat['size'] = 'chubby'
print(myCat['size'])
myCat['home']= 'Udaipur'
print(myCat)
del myCat['home']
print(myCat)

allGuests = {'Alice':{'apples':5, 'bananas':12},
             'bob':{'burger':3, 'apples':2},
             'caroline':{'cups':3, 'apple pies':1}
             }

def totalBrought(guests, item):
    numBrought = 0 #initialize the count to 0

    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)

    return numBrought

print("Number of things being brought:")
print('apples - ' + str(totalBrought(allGuests, 'apples')))
print('cups -         ' + str(totalBrought(allGuests, 'cups')))
print('banana -         ' + str(totalBrought(allGuests, 'bananas')))
print('burger ' + str(totalBrought(allGuests, 'burger')))
print('apple Pies -    ' + str(totalBrought(allGuests, 'apple pies')))
