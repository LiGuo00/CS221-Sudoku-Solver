import numpy as np
import sys
import matplotlib.pyplot as plt

class HillClimbing():

	
# To be continued
	def climbHill(self):
		scores = []
		# print("Initial score: " + str(maxScore))
		while True:
			# print("Current score: " + str(maxScore))
			scores.append(maxScore)
			(row, (col1, col2), nextScore) = self.bestNeighbor()
			if(nextScore <= maxScore):
				return scores
			self.swap(self.board[row], col1, col2)
			maxScore = nextScore
