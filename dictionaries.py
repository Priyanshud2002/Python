myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
print(myCat.get('size'))
print(myCat.get('voice', 'Not Found'))

for key in myCat.keys():
    print(key)
for value in myCat.values():
    print(value)
for key, value in myCat.items():
    print(key + " : " + value)

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input("Enter a name: (blank to quit) ")
    if name == '':
        break
    if name in birthdays:
        print(name + "'s birthday is " + birthdays[name])
    else:
        print("I don't have birthday information for " + name)
        addbirthday = input("What is their birthday? ")
        birthdays[name] = addbirthday  # Adds new data
        print("Birthday database updated!")

spam = {'name':'messi', 'age':'5'}
spam.setdefault('color', 'white')
print(spam)

import pprint
data = {'name': 'Alice', 'age': 30, 'hobbies': 'reading,writing'}
pprint.pprint(data)

