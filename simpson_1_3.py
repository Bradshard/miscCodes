import numpy as np
import math
import matplotlib.pyplot as plt

# ----- function define ----

def func(x,y):
	return y * ((x**3)/((np.exp(x)-1)))

def simpson (f,a,b,n,z): # a lower bound, b upper bound, f function
	h = ((b-a)/n) # distance in between parts
	cout = 0.5
	s = 0
	al_val = []
	for i1 in range(n):
		al_val.append(a+cout)
		cout += h
	for i in range(n):
		if ((i%2 == 0) and (i != n-1)):
			s += (2*f(al_val[i],z))
		elif (i == n-1):
			s += f(al_val[i],z)
		elif ((i%2 == 1) and (i != n-1)):
			s += (4*f(al_val[i],z))
	return s*(h/3)


# ----- constants -----
T = 273 # temperature but random in kelvin. I pick 0 celcius degree.

K_b = 1.380649 * 10**(-23) # Boltzmann constant, joule/kelvin.

c = 2.99792458*((10)**(8)) # in m/s

planck_c = 6.62607004 * 10**(-34) # in m^2* kg / s

h_bar = planck_c/(2*math.pi)

h = 0.5 # will be used in the formulation as interval jumps



# ----- Real values -----

real_val_of_integral = 6.49393940226684
constant_part = (((K_b**4)*(T**4))/(4*((math.pi)**2)*(c**2)*(h_bar**3)))
real_W_val = constant_part*real_val_of_integral

print(simpson(func,0,3,6,constant_part)) 