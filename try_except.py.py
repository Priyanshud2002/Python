def divide(number): #creates a function divide
    try:
        result = 42/number #42 will be divided by the enter no and stored in result
        return result  
    except ZeroDivisionError: # catches the error
        return "erroe:You cannot divide by zero"

print(divide(2))
print(divide(12))
print(divide(0))
print(divide(1) + 2)

