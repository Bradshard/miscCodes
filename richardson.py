from math import *
import numpy as np

def func(a):
	return a**cos(a)

def phi(x = 0.6, h = 0.1):
	phi_h = (func(x + h) - func(x - h))/(2*h) #our function
	return phi_h

def richardson(x,n,h):
	a =  np.array( [[0] * (n+1)] * (n+1) ) # to create an array to fit all iterations of D(n,m)

	for i in range(n+1): # + 1 to use all iterations.
		a[i,0] = phi(x, h)

		h_4 = 1 # richardson is computed in O(h^4) error.
		for i1 in range(1,i+1):
			h_4 = 4*h_4
			a[i,i1] = a[i,i1-1] + (1/(h_4-1))*(a[i,i1-1] - a[i-1,i1-1])
		h = h/2
	return a

print(richardson(0.6,5,0.1))
print("{} is the final result. ".format(richardson(0.6,5,0.1)[5,5]))