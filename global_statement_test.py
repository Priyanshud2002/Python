eggs = 42 #global variable

def spam(): #creates a fucntion spam
    global eggs # makes the egg varibale global
    eggs = 'spam'

def bacon(): #createss another function bacon
    eggs = 'bacon'#local variable x (does not change global x)

def ham():
    print(eggs) #uses the global eggs

print(eggs)
spam() #Calls the function spam
print(eggs) #prints 'spam'(global eggs was changed by spam)
