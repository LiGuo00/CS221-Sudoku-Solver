import BacktrackCSP

print "hello world"
csp = BacktrackCSP.create_suduko(4)
alg = BacktrackCSP.BacktrackingSearch()
alg.solve(csp, True, True, True) #lookahead, mcv, ac3
print csp.variables
print 'One of the optimal assignments:',  alg.optimalAssignment

