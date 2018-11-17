
from math import floor
import gameboard


def ReadFile(filePath):
    """Read from input file and generate gameboard."""
    with open(filePath, 'r') as f:
        lines = f.readlines()

        if len(lines) == 0:
            raise ValueError("Input file " + filePath + " was empty")
        elif len(lines) < int(lines[0].split()[0]) + 1:
            raise ValueError("Incomplete or Emtpy board for file " + filePath)
        else:
            board = []
            for i in range(len(lines)):
                if i == 0:
                    if len(lines[0].split()) != 3:
                        raise ValueError("Params invalid in file.")
                    N = int(lines[i].split()[0])
                    p = int(lines[i].split()[1])
                    q = int(lines[i].split()[2])
                else:
                    tempLine = []
                    for n in lines[i].split():
                        # print(num)
                        # print(type(num)
                        tempLine.append(int(n))
                    board.append(tempLine)
            return gameboard.GameBoard(N, p, q, board)
   
    
# simple criteria for difficulty
# define the difficulty as percentage of 0 in the board
def getDifficulty(board):
    n = len(board)
    m = len(board[0])
    count = 0
    total = n * m
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    return float(count) / total
                
