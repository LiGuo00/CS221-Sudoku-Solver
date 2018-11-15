import submission

print "hello world"
csp = submission.create_suduko(4)
alg = submission.BacktrackingSearch()
alg.solve(csp, True, True, True) #lookahead, mcv, ac3
print csp.variables
print 'One of the optimal assignments:',  alg.optimalAssignment

