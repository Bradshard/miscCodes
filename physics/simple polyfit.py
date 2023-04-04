import numpy as np
from math import *
import matplotlib.pyplot as plt

t = np.array(np.linspace(0,100,101)) # time np.array lineerly spaced

V_0 = 5 # velocity is given in the exercise
g = 10 # gravity is also given in the exercise

Y = [] # empty list to append
for i in range(len(t)):
	Y.append(((V_0*t[i])+(1/2*g*(t[i]**2)))) # appending formula to the list

y = np.array(Y) # list to np.array for distance

plt.title("distance(y) vs time(t)") # labels for the 
plt.ylabel('distance(y)') 
plt.xlabel('time(t)')
plt.plot(t, y,'*r' , label='distance at a specific time' ,linewidth=2.0)

fit = np.polyfit(t,y,2) # polynomial fit of the formula.
plt.plot(t,np.polyval(fit,t), color = "green", label = 'Polynomial-fit')# fitted plot.

plt.legend()
plt.show()