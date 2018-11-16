import BacktrackCSP
import os
import sys
import time
import filereader
import BacktrackCSP
import gameboard

if __name__ == '__main__':
    # Check command-line arguments.
    #
    # python main.py ExampleSudokuFiles/PE1.txt output_PE1.txt BT

    if len(sys.argv) < 3:
        print("Program did not received enough correct argument.")
        print("python main.py <input> <output> <method>")
    # input
    sudokudata = filereader.printSudoku(sys.argv[1])
    method = sys.argv[3:]
    # different method
    if method == 'HC':
        print("HC detected: Hill Climbing (HC)")
        CH.HillClimbing()
    else:
        csp = BacktrackCSP.create_suduko(sudokudata.N, sudokudata.board)
        alg = BacktrackCSP.BacktrackingSearch()
        alg.solve(csp, True, True, False, True) #lookahead, mcv, ac3, find only one solution
        print 'One of the optimal assignments:', alg.optimalAssignment

        #print the board and ready to write into a file
        n= sudokudata.N
        def getnum(i, j):
            return (i - 1) / int(n ** 0.5) * int(n ** 0.5) + (j - 1) / int(n ** 0.5) + 1
        board = []
        for i in range(1, sudokudata.N+1):
            table = []
            for j in range(1, sudokudata.N+1):
                table.append(str(alg.optimalAssignment[i, j, getnum(i, j)]))
            board.append(table)
    sudokudataoutput= gameboard.GameBoard(sudokudata.N, sudokudata.p, sudokudata.q, board)
    print sudokudataoutput

    #output doesn't work
    #with open(sys.argv[2], "w") as outfile:
        #outfile.write(sudokudataoutput)
