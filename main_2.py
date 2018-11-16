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
    print(sudokudata)
    method = sys.argv[3]
    # different method
    if method == 'hillclimbing':
        print("hillclimbing detected")
        pass
    elif method == "backtrack":
        print("Backtrack detected")
        csp = BacktrackCSP.create_suduko(sudokudata.N, sudokudata.board)
        alg = BacktrackCSP.BacktrackingSearch()
        alg.solve(csp, True, True, True)
        print 'One of the optimal assignments:', alg.optimalAssignment
        
        # output
  #  with open(sys.argv[2], "w") as outfile:
  #      outfile.write(sudokudata)
