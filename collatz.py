def collatz(number):  # Function takes a number as input
    if number % 2 == 0:  # If even
        result = number // 2
    else:  # If odd
        result = 3 * number + 1

    print(result)  # Print the result
    return result  # Return the result


# Ask the user for an integer input
try:
    num = int(input("Enter an integer: "))  # Get user input
    
    while num != 1:  # Loop until the number becomes 1
        num = collatz(num)  # Call collatz() and update num

except ValueError:  # Handle invalid input
    print("Please enter a valid integer.")
