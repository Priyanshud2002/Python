spam = [
    'apples',
    'oranges',
    'cats'
    ]
print(spam)

print('Hello,' + \
      'world!')

name = "zophie"
newName = 'm' + name[1:]
print(newName)

eggs = [1, 2, 3]
del eggs[2] #del deletes from the list
del eggs[1]
del eggs[0]
eggs.append(4) #append adds to the list
eggs.append(5)
eggs.append(6)
print(eggs)

import copy
letters = ['A', 'B', 'C', 'D']
cheese = copy.copy(letters)
cheese[1] = 42
print(letters)
print(cheese)


def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
