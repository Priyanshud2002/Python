x = 10 #global variable

def change(): #created a function change
    global x # tells python to use the global x
    x = 20 # Changes the value of global variable

change() # calls the function change
print(x)   #prints 20 (global variable changed)
    
