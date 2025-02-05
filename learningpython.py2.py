x = 10  #global variable'


def my_function(): #defined a function as my_function()
    y = 5  #local varibale because declared inside the function
    print(y)  #works because it is inside the function - my_function

my_function()  #calling the function my_function
print(x)  # works as x is global variable
print(y)  # Error y is local varibale only works inside function
