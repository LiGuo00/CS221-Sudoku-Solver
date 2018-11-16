import BacktrackCSP
import os
import sys
import time
import filereader
import BacktrackCSP

if __name__ == '__main__':
    # Check command-line arguments.
    #
    # python main.py ExampleSudokuFiles/PE1.txt output_PE1.txt BT

    if len(sys.argv) < 3:
        print("Program did not received enough correct argument.")
        print("python main.py <input> <output> <method>")
    # input
    sudokudata = filereader.printSudoku(sys.argv[1])
    print sudokudata.board
    method = sys.argv[3:]
    # different method
    if method == 'HC':
        print("HC detected: Hill Climbing (HC)")
        CH.HillClimbing()
    else:
        csp = BacktrackCSP.create_suduko(sudokudata.N, sudokudata.board)
        alg = BacktrackCSP.BacktrackingSearch()
        alg.solve(csp, True, True, False, False) #lookahead, mcv, ac3, find only one solution
        print 'One of the optimal assignments:', alg.optimalAssignment
        # output
  #  with open(sys.argv[2], "w") as outfile:
  #      outfile.write(sudokudata)
