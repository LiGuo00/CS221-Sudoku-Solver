#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:12:31 2018

@author: liguo
"""

import numpy as np
import time
import sys
import filereader
import math


class HillClimbing():
    
    def __init__(self, initBoard):
        self.initBoard = initBoard
        self.reset()
    
    def reset(self):
        self.fixedValue = self.boardToList(self.initBoard)
        self.board = self.randomBoard()
        
        self.setup()
        
    def randomBoard(self):
        n = len(self.initBoard)
        grid = (np.indices((n, n)) + 1)[1] #1,2,3,4...,n for each row
        for row in grid:
            np.random.shuffle(row)
        return grid
    
    # convert initBoard into an array of fixed value
    def boardToList(self, initBoard):
        valList = []
        for i in range(len(initBoard)):
            for j in range(len(initBoard[i])):
                if initBoard[i][j] == 0:
                    continue
                # (val, i, j)
                valList.append( (initBoard[i][j], i, j) )
        return np.asarray(valList)
            

    # set fixed value in right position in self.board
    def setup(self):
        for (val, row, col) in self.fixedValue:
            valIndex, = np.where( self.board[row] == val )[0]
            #self.board[row][col], self.board[row][valIndex] = \
            #self.board[row][valIndex], self.board[row][col]
            self.swap(self.board[row], valIndex, col)
            
            
    # swap two elements in an array
    def swap(self, array, p1, p2):
        array[p1], array[p2] = array[p2], array[p1]
        
        
        

    # heuristic function to be maximized
    # defined as sum of unique elements in row, column and sub-grid
    def heuristic(self, board=[]):  # board: numpy array
        score = 0;
        if board == []:
            board = self.board
        for row in board:
            score += len(np.unique(row))
        for col in np.transpose(board):
            score += len(np.unique(col))
        n = int(math.sqrt(len(self.initBoard)))
        for i in range(n):
            for j in range(n):
                sub = board[i*n : i*n+n, j*n : j*n+n]
                score += len(np.unique(sub))
        # this is to be maximized
        return score
    
    
    
    # check whether value in given position is fixed O(n)
    def isFixed(self, row, col):
        for item in self.fixedValue:
            if item[1] == row and item[2] == col:
                return True
        return False
        
    
    def firstSucc(self):
        tempBoard = self.board.copy()
		# best = (row, (col1, col2), heuristic value)
        succ = (0, (0,0), -1)
        for i in range(len(tempBoard)):
			for j in range(len(tempBoard[i])):
				for k in range(i, len(tempBoard)):
					if(self.isFixed(i,j) or self.isFixed(i,k)):
						continue
					self.swap(tempBoard[i], j, k)
					succ = (i, (j,k), self.heuristic(tempBoard))
					if succ[2] > 0:
						break
					
					self.swap(tempBoard[i], j, k)
        return succ
        
    
    # find first closer node was chosen
    # best successor given current board state
    def bestSucc(self): # use copy of board
        tempBoard = self.board.copy()
		# best = (row, (col1, col2), heuristic value)
        best = (0, (0,0), -1)
        for i in range(len(tempBoard)):
			for j in range(len(tempBoard[i])):
				for k in range(i, len(tempBoard)):
					if(self.isFixed(i,j) or self.isFixed(i,k)):
						continue
					self.swap(tempBoard[i], j, k)
					contestant = (i, (j,k), self.heuristic(tempBoard))
					if(contestant[2] > best[2]):
						best = contestant
					
					self.swap(tempBoard[i], j, k)
        return best
    
    
    
    # Start doing hill climbing
    def climbHill(self):
        scores = []
        maxScore = self.heuristic()

        while True:

            scores.append(maxScore)
            # best successor
            #(row, (col1, col2), nextScore) = self.bestSucc()
            # first successor
            (row, (col1, col2), nextScore) = self.firstSucc()
            if(nextScore <= maxScore):
                return scores
            self.swap(self.board[row], col1, col2)
            maxScore = nextScore
            
            
            
    def printBoard(self, board=[]):
        if(board == []):
            board = self.board
            
        for i in range(len(board)):
            if(i % 3 == 0 and i != 0):
                print("------+------+------")
            for j in range(len(board[i])):
                if(j % 3 == 0 and j != 0):
                    sys.stdout.write("|")
                sys.stdout.write(str(board[i][j]) + " ")
            print("")
            
    def maxScore(self):
        n = len(self.initBoard)
        return 3 * n * n
    
            
    
    def randomStart(self):
        trials = []
        maxScore = -1
        bestBoard = []
        for i in range(1000):
            self.reset()
            finalScore = self.climbHill()
            maxFinalScore = max(finalScore)
            if(maxScore < maxFinalScore):
                maxScore = maxFinalScore
                bestBoard = self.board.copy()
            print(str(i) + ") " + str(finalScore[-1]) + "/" + str(self.maxScore()))
            if(maxScore == self.maxScore()):
                print("This is the solution!")
                self.printBoard()
                break
            trials.append(finalScore)
        	# print(finalScore)
        print("Max Score: %i" % maxScore)
        self.printBoard(bestBoard)
        return bestBoard
                    
                        

startTime = time.time()

sudokudata = filereader.ReadFile('ExampleSudokuFiles/simple_3.txt') 
board = sudokudata.board   
climb =  HillClimbing(board)
print "Initial given Board!!"
climb.printBoard(climb.initBoard)
print "Initial random Board!!"
climb.printBoard()
print "Final Board!!"
climb.randomStart()
endTime = time.time()
print "Time spent: ", endTime - startTime
    

################# best successor
# 9 * 9
# PE1: 
# PE2: 
# PE3: 
# PE4: 
# PE5: 
# PE6: 
# PE7: 
# PE8: 
# PE9: 
# PE10: 
# simple2_0: 0.0269889831543, 0.0210738182068
# simple2_1: 0.0391039848328, 0.0223798751831, 0.0238790512085, 0.0355310440063
# simple2_2: 0.0745677947998, 0.0770859718323, 0.076290845871, 0.0634069442749
# simple2_3: 12.8873381615, 1.01769685745, 2.82208919525, 4.54819011688, 1.81693601608
# simple2_4: NA

# 4 * 4
# simple_0: 0.0354709625244, 0.0495710372925, 0.0290508270264, 0.0327370166779
# simple_1: 0.128174066544, 0.0327930450439, 0.0387780666351, 0.0587818622589
# simple_2: 0.0467238426208, 0.0872540473938, 0.256032943726, 0.530433893204, 0.0249390602112
# simple_3: 0.025120973587, 0.0302770137787, 0.0391111373901, 0.0273420810699



################# first successor  
# 9 * 9
# PE1: 
# PE2: 
# PE3: 
# PE4: 
# PE5: 
# PE6: 
# PE7: 
# PE8: 
# PE9: 
# PE10: 
# simple2: 

# 4 * 4
# simple2_0: 0.0306029319763, 0.019681930542, 0.0222079753876, 0.0218741893768
# simple2_1: 0.0334420204163, 0.0310080051422, 0.0240390300751, 0.0369670391083
# simple2_2: 0.349719047546, 1.11760401726, 0.954236984253,  0.12286901474, 0.247157096863, 0.664642095566
# simple2_3: NA
# simple2_4: NA

# simple_0: 0.78049993515, 2.97117209435, 0.599956989288, 2.93151807785
# simple_1: 0.337473154068, 4.34701800346, 0.716123104095, 4.00713920593, 0.0895810127258
# simple_2: 2.75815296173, 0.188815832138, 1.67441511154, 0.32562494278
# simple_3: 0.158025026321, 0.292256832123, 0.528688907623, 0.0728278160095

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

