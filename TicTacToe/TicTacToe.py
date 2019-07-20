#Tic Tac Toe with AI
# The sauce is from http://inventwithpython.com/chapter10.html
import random 

def drawBoard(board):
    # Prints out what moves are on the board currently
    # All the moves are stored in board
    # Index starts with 1 because its easy to play with the num pad
    # Remember to adjust indexes later
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Deciding what the player wants to be X or O
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want X or O')
        letter = input().upper()

    # Rerutn the letter in an array, with player letter first and cpu letter second
    if letter == 'X':
        return ['X','O']
    else: 
        return ['O', 'X']

# Decides who goes first
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else: 
        return 'player'


# Asking if the user wants to play again
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

# Placing a move on the board
# Added it to board
def makeMove(board, letter, move):
    board[move] = letter

# Check if a player has won or not

def isWinner(bo, le):
    # Given the board(bo) and the letter of the player (le)
    # Find if the player has won
    # Since it is a tic tac toe, only 9 ways to win
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

# Making a copy of the board
def getBoardCopy(board):
    dupeBoard = [i for i in board]
    return dupeBoard

# Checking if there is anymore space on the board 
def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    # Get move from input 
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


# Choosing a move from a list of moves
def chooseRandomMoveFromList(board, movesList):
    # returns valid move, else nothing
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

# Creating the "AI"
# Steps of Algorithm 
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Check if computer can win, if it can return the move
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    # Check if human can win, if human can win, return the winning move to block it
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    # If neither can win, check corner, center, and side spaces
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
        if isSpaceFree(board, 5):
            return 5
    # If nothing then pick whats remaining, or nothing 
    return chooseRandomMoveFromList(board, [2,4,6,8])

# Check if the board is full
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
             return False
    return True
###### Start of the game
print('Welcome to Tic Tac Toe!')
 
while True:
    theBoard = [' '] * 10 # Python syntax for filling up lists easily, because... Python
    # Decide who goes first 
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True # Need this to track in game 
    
    while gameIsPlaying: # In game 
            if turn == 'player':
                # Player’s turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Good job you beat the AI')
                    gameIsPlaying = False # Ending the game 
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game was a tie and you suck XD')
                        break
                    else:
                        turn = 'computer'
            else:
                # Computers turn
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You suck :/')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie! Not good')
                        break
                    else:
                        turn = 'player'
    if not playAgain():
        break