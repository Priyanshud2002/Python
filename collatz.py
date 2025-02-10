def collatz(number): #created a funtion collatz with perimeter number
    if number % 2 == 0: #condition
       result = number // 2

    else:
        result = 3 * number + 1

    print(result)
    return result

#ask user for integer input
try:
    print("Enter a number")
    num = int(input())

    while num != 1:
        num = collatz(num)

except ValueError:
    print("Please enter a valid integer")
        
        
