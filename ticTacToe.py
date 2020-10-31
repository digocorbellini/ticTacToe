import random
isGameOver = False
#Method to print out the board
def printBoard(board):
    index1 = 0
    for arr in board:
        index = 0
        for element in arr:
            if element == 0:
                print(" ", end = "")
            elif element == 1:
                print("X", end = "")
            elif element == 2:
                print("O", end = "")
            if index < 2:
                print("|", end = "")
            index += 1
        print()
        if index1 < 2:
            print("-----")
        index1 += 1

#Matrix element holds position of an element in the board
class MatrixElement:
    row = 0
    col = 0

    #constructor
    def __init__(self, row, col):
        self.row = row
        self.col = col

#get move as number
def moveAsIndex(playerMove):
    rowString = playerMove[0]
    colString = playerMove[1]
    cellIndex = MatrixElement(0,0)
    #find desired row
    if rowString == "T":
        cellIndex.row = 0
    elif rowString == "M":
        cellIndex.row = 1
    elif rowString == "B":
        cellIndex.row = 2
    else:
        return None
    #find desired col
    if colString == "L":
        cellIndex.col = 0
    elif colString == "M":
        cellIndex.col = 1
    elif colString == "R":
        cellIndex.col = 2
    else:
        return None
    return cellIndex

#returns true if move can be made
def canMakeMove(cell):
    if(cell == None):
        return False
    
    row = cell.row
    col = cell.col
    currentCell = board[row][col]
    return currentCell == 0

#Do the move of the bot
def botMove():
    if(isBoardFilled()):
        return
    randomRow = random.randrange(0,3)
    randomCol = random.randrange(0,3)
    while not canMakeMove(MatrixElement(randomRow, randomCol)):
        randomRow = random.randrange(0,3)
        randomCol = random.randrange(0,3)
    board[randomRow][randomCol] = 2


#Make Player move
def makeMove(playerMove):
    cell = moveAsIndex(playerMove)
    if(not canMakeMove(cell)):
        print("Illegal Move")
        return
    
    board[cell.row][cell.col] = 1
    botMove()
 
#Check to see if board is filled
def isBoardFilled():
    for r in range(0,3):
        for c in range(0,3):
            if board[r][c] == 0:
                return False
    return True

#Checks to see if anyone has won
def checkBoard():
    global isGameOver
    if isBoardFilled():
        print("board filled")
        isGameOver = True
        return

    diagonal = ""
    for r in range(0,3):
        arrStr = str(board[r])
        if arrStr == "[2, 2, 2]" or arrStr == "[1, 1, 1]":
            isGameOver = True
            return
        
        diagonal += str(board[r][r])

        column = ""
        for c in range(0,3):
            column += str(board[r][c])
        if column == "111" or column == "222":
            isGameOver = True
            return
    if diagonal == "111" or diagonal == "222":
        isGameOver = True
        return
                
def startRound():
    global isGameOver
    global board
    isGameOver = False
    board = ([[0,0,0],
            [0,0,0],
            [0,0,0]])

    printBoard(board)
    while(not isGameOver):
        move = input("Make a move")
        makeMove(move)
        checkBoard()
        print()
        printBoard(board)

    print("GAME IS OVER")

board = ([[0,0,0],
         [0,0,0],
         [0,0,0]])

playerResponse = ""
while(playerResponse != "exit"):
    startRound()
    playerResponse = input("type 'exit' to quit or anything else to retry")




string = ""
""" for i in range(0,3):
    string += str(board[i][i])
if(string == "111" or string == "222"):
    isGameOver = True """




