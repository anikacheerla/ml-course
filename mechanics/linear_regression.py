# linear regression: y = mx
# Find optimal m

import numpy as np

def calc_error(X, Y, m):
	res = np.array([])
	for x in X:
		res = np.append(res, x*m)
	return np.mean(Y - res)

X = np.array([.27,.39, .53])
Y = np.array([1.02, 1.49, 2.01])

m = -9 #set m to arbitrary starting point
error = calc_error(X, Y, m)

while error >= 0.0001:
	print "m =", m ,"error=", error
	m = m+error
	error = calc_error(X,Y,m)

