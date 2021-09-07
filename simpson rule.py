from math import pi, sin, cos, sqrt, exp
import numpy as np

def a(x):
	return (1/((2.8)*sqrt(2*pi)))*exp((-(x-69)**2)/5.6) #69 inches is the average height of male in Turkey.

def simpson (f,a,b,n): # a lower bound, b upper bound, f function
	h = ((b-a)/n) # distance in between parts
	cout = 0
	s = 0
	al_val = []
	for i1 in range(n+1):
		al_val.append(a+cout)
		cout += h
	for i in range(n+1):
		if ((i%2 == 0) and (i != 0 or i != n)):
			s += (2*f(al_val[i]))
		elif (i == 0 or i == n):
			s += f(al_val[i])
		elif ((i%2 == 1) and (i != 0 or i != n)):
			s += (4*f(al_val[i]))
	return s*(h/3)

print(simpson(a, 59.0551,71.6535,100000)) 
