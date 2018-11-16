#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:12:31 2018

@author: liguo
"""

import numpy as np
import time
import sys



class HillClimbing():
    
    def __init__(self, initBoard):
        self.fixedValue = self.boardToList(initBoard)
        self.board = (np.indices((9, 9)) + 1)[1] #1,2,3,4...,9 for each row
        self.setup()
    
    
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
        for i in range(3):
            for j in range(3):
                sub = board[i*3 : i*3+3, j*3 : j*3+3]
                score += len(np.unique(sub))
        # this is to be maximized
        return score
    
    
    
    # check whether value in given position is fixed O(n)
    def isFixed(self, row, col):
        for item in self.fixedValue:
            if item[1] == row and item[2] == col:
                return True
        return False
        
    
    #def firstSucc(self):
        
        
    
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
		# print("Initial score: " + str(maxScore))
        while True:
			# print("Current score: " + str(maxScore))
            scores.append(maxScore)
            (row, (col1, col2), nextScore) = self.bestSucc()
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
                    
                        

startTime = time.time()
                
board = np.zeros((9, 9), dtype=np.int)
climb =  HillClimbing(board)
print climb.fixedValue
climb.printBoard()
print climb.climbHill()
climb.printBoard()

endTime = time.time()
print "Time spent: ", endTime - startTime
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

