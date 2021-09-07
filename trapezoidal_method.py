import numpy as np
import math
import matplotlib.pyplot as plt

# ----- function define ----

def func(x):
	global h
	global planck_c
	global c
	global K_b
	global T
	global h_bar
	return (((K_b**4)*(T**4))/(4*((math.pi)**2)*(c**2)*(h_bar**3))) * ((x**3)/((math.e**x) -1))

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

# ----- calculation -----
vals = np.arange(0.5,709,h) #  RuntimeWarning: overflow encountered in double_scalars above 710
pre_W = []
summation_of_mid_vals = 0


for i in vals:
	pre_W.append(func(i))

for i in pre_W:
	summation_of_mid_vals += i

T = h*(summation_of_mid_vals + (0.5)*(0+func(709.5)))

print("W value found by trapezoid method is {}.".format(T))
print("W value found by analytical calculation is {}.".format(real_W_val))
print("Error between W values are %{}.".format((100*(abs(T-real_W_val)/real_W_val))))
