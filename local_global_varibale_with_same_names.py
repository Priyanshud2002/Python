x = 'global' #creatwed a global variable

def my_func(): # created a function as myfunc
    x = 'local' #created a local varibale x and set its value as 'local 'inside function(my_func)
    print(x) #prints the value of local varibale x inside function

my_func()  # called the function my_func()
print(x)   # prints the value of global variable x because it is outisde the function
