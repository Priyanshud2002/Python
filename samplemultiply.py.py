import random

def multiply(number):
    result = 10 * number
    return result

r = random.randint(1, 10)
output = (multiply(r))

print("Random Number : " + str(r))
print("output : " + str(output))


