spam = ["Cat", "Bat", "Rat", "elephant"] #stored multiple values in spam(list)
print(spam[0]) #index starts from 0 it will print cat
print(spam[2]) #index no 2 it will print 2
print(spam[-1]) #negative indexing -1 will print elephant
print(spam[1:3]) #will print index 1 to 2 not 3
print(spam[:2])  #will print from start to 1 not 2
print(spam[2:]) #will print from index 2 to end
print(spam[:]) # will print whole list
print(len(spam)) #finding length of the list
spam[1] = "shark" #changes span index 1(bat) to new index 1(shark)
print(spam[1]) #print spam index 1
print([spam] + ["1", "2", "3", "4"]) # using + to combine(add) different lists
print([spam]*2) #using * to repeat this list twice
del spam[3] #removes 3 index from spam list
print([spam]) #prints updated spam list
for animal in spam: #using a loop to go through all items in a list
    print(animal)
cats = ["zoe", "Max", "Cipher", "rio"]
print([cats])
