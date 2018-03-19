import numpy as np

def sigmoid(x, deriv = False):
	if deriv:
		return x*(1-x) #deriv of sigmoid function
	return 1/(1+np.exp(-x))

X = np.array( [[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
Y = np.array([0,1,1,0]).T

weights = 2*np.random.random((3,1)) - 1.  #initialized randomly with mean = 0
mean_error = 100
while mean_error > 0.001:
	res = sigmoid(np.dot(X, weights))
	error = Y - res
	mean_error = np.mean(error)
	# multiply how much we missed by the slope of the sigmoid at the values in l1
	delta = error * sigmoid(np.dot(X, weights), True)
	#update weights 
	weights = np.dot( X.T, delta)
	
print("error:", mean_error)

