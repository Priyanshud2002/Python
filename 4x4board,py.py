theBoard = {'top left':' ', 'top mid':' ', 'top right':' ', 'top right corner':' ',  #CREATING A DICTIONARY 
            'up left':' ', 'up mid':' ', 'up right':' ', 'up right corner':' ',
            'mid left':' ', 'mid mid':' ', 'mid right':' ', 'mid right corner':' ',
            'low left':' ', 'low mid':' ', 'low right':' ', 'low right corner':' ',
            }

def printboard(theBoard):  #FUNCTION TO PRINT THE BOARD
    print(theBoard['top left'] + '|' + theBoard['top mid'] + '|' + theBoard['top right'] + '|' + theBoard['top right corner'])
    print('+++++++')
    print(theBoard['up left'] + '|' + theBoard['up mid'] + '|' + theBoard['up right'] + '|' + theBoard['up right corner'])
    print('+++++++')
    print(theBoard['mid left'] + '|' + theBoard['mid mid'] + '|' + theBoard['mid right'] + '|' + theBoard['mid right corner'])
    print('+++++++')
    print(theBoard['low left'] + '|' + theBoard['low mid'] + '|' + theBoard['low right'] + '|' + theBoard['low right corner'])

turn = 'x'
for i in range(0,16):
    printboard(theBoard)
    print('turn for ' + turn + ' make your move!')
    move = input()
    theBoard[move] = turn

    if turn == 'x':
        turn = '0'
    else:
        turn = 'x'

    
