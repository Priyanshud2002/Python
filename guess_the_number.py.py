import random  # imported module random

secretNumber = random.randint(1,20) #created a secretnumber input
print("I am thinking of a number between 1 and 20.") #prints this exact line

for guessesTaken in range(1, 7): #loop runs 6 times
    print("take a guess?")
    guess = int(input())  #gets players guess(converts it into a integer)

    if guess < secretNumber: #condition
        print("your guess is too low")

    elif guess > secretNumber: #condition
        print("Your guess is too high")

    else:
        break #if the guess is correct it breaks the loop

if guess == secretNumber:
    print("You gussed the correct number which i was thinking:" + guessesTaken)
else:
    print("nope the number i was thinking of was:" + secretNumber)
    

    
              
