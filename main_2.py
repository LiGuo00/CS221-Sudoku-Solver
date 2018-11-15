import os
import sys
import time
import filereader

if __name__ == '__main__':
    # Check command-line arguments.
    #
    # python main.py ExampleSudokuFiles/PE1.txt output_PE1.txt BT

    if len(sys.argv) < 3:
        print("Program did not received enough correct argument.")
        print("python main.py <input> <output> <method>")
    # input
    sudokudata = filereader.printSudoku(sys.argv[1])
    print(sudokudata)
    method = sys.argv[3:]
    # different method
    if method == 'HC':
        print("HC detected: Hill Climbing (HC)")
        CH.HillClimbing()

    # output
    with open(sys.argv[2], "w") as outfile:
        outfile.write(sudokudata)
