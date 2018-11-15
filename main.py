import submission

print "hello world"
csp = submission.create_suduko(4)
alg = submission.BacktrackingSearch()
alg.solve(csp, True, True, True)
print csp.variables
print 'One of the optimal assignments:',  alg.optimalAssignment

