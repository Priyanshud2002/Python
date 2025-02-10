catNames = [] #created an empty list
while True: #condition while loop
    print("enter a cat name(or press enter to stop):")
    name = input()
    if name == "":
        break
    catNames.append(name) #adds catNames to to the list

    print("the cat names are:")
    for name in catNames:
         print(name)
