import os
import sys
import time
import filereader
import BacktrackCSP

if __name__ == '__main__':
    # Check command-line arguments.
    # python main.py ExampleSudokuFiles/PE1.txt output_PE1.txt BT

    if len(sys.argv) < 3:
        print("Program did not received enough correct argument.")
        print("python main.py <input> <output> <method>")
        print("method includes: backtrack hillclimbing")
    # input
    sudokudata = filereader.ReadFile(sys.argv[1])
    csp = BacktrackCSP.CreateCSP(sudokudata)
    print(sudokudata)
    method = sys.argv[3]
    print(method)
    # different method
    if method == 'backtrack':
        print("backtrack detected!")
        alg = BacktrackCSP.BacktrackingSearch()
        alg.solve(csp, True, True, True) #lookahead, mcv, ac3
        print csp.variables
        print 'One of the optimal assignments:',  alg.optimalAssignment

    elif method == "hillclimbing":
        pass

    # output
    with open(sys.argv[2], "w") as outfile:
        outfile.write(sudokudata)
