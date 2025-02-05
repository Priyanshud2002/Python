import random  #imports the random module to generate random numbers

while True: #Starts a loop to keep playing the game
    
     print('Do you want to play Magic 8 ball?')
      input()
      if input == 'yes':
        def getAnswer(answerNumber): # getAnswer function takes a number and gives us the return according to the number
            if answerNumber == 1:
            return 'It is certain'
            elif answerNumber == 2:
            return 'It is decidedly so'
            elif answerNumber == 3:
            return 'Yes'
            elif answerNumber == 4:
             return 'Reply hazy try again'
            elif answerNumber == 5:
            return 'Ask again later'
            elif answerNumber == 7:
            return ' My reply is no'
            elif answerNumber == 8:
            return 'Outlook not so good'
            elif answerNumber == 9:
            return 'Very doubtful'

         r = random.randint(1, 9) # generates a random number from 1 to 9
         fortune = getAnswer(r) # gets the fortune based on the number
         print(fortune) # prints fortune

            elif input == 'no'
            print('Okay, Maybe next time!')
            break

            else:
                print('Please enter yes or no')
                

         

       
