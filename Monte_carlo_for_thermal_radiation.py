# importing the modules
from scipy import random
import numpy as np
import math

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

integral = 0.0 #  to store all values 

# ---- lower and upper boundaries ----
a = 0
b = 3 # gets the value of pi
N = 100000
 
# ----- zero array -----
zero_arr = np.zeros(N)
 
""" 
iterating over each Value of ar and filling
it with a random value between the limits a and b
""" 
for i in range (len(zero_arr)):
    zero_arr[i] = random.uniform(a,b)

 
# --- calculations
for i in zero_arr:
    integral += func(i)
 
ans = (b-a)/float(N)*integral # the real answer
 
# ---- solution printer ----
print("The value calculated by monte carlo integration is {}.".format(ans))