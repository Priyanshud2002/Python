import random  # Imports the random module to generate random numbers

# Function to return a random answer
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Better not tell you now'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

while True:  # Starts an infinite loop
    print('Do you want to play Magic 8 Ball? (yes/no)')
    user_input = input().strip().lower()  # Get user input and convert it to lowercase

    if user_input == 'yes':  # If the user wants to play
        r = random.randint(1, 9)  # Generate a random number from 1 to 9
        fortune = getAnswer(r)  # Get the fortune based on the number
        print(fortune)  # Print the fortune

    elif user_input == 'no':  # If the user doesn't want to play
        print('Okay, Maybe next time!')
        break  # Exit the loop and end the program

    else:  # If the user enters an invalid response
        print('Please enter yes or no.')
