import matplotlib.pyplot as plt
import numpy as np

# ODE

def func(t,v):
	return 1 - 2*v**2 - t
"""
# exact solution
def y(t):
	return 
"""
# lower and upper limits

t_0 = 0.0
t_1 = 1.0

# steps

N = 100

# step-size

h = (t_1 - t_0)/N

#Initial Value as tuple since it won't change

y_0 = (0.0,1.0)
y_1 = (1.0,0.472725)
# arrays

t = np.arange(t_0, t_1 + h , h)
z = np.zeros((N+1, ))

# initial value set from y_0

t[0], z[0] = y_0

# Euler Method
for i in range(1, N+1):
	z[i] = z[i-1] + h* func(t[i-1], z[i-1])


# real value is approximately y(1) = 0.472725
# normally 0.472725 - 1.66533 x 10**-16 i  second part is too small, so ignore.

print("Euler Method solution for function at y(1) given as {}.".format(z[N]))
print("Error between exact value and Euler is %{}.".format(100*(1-(z[N]/y_1[1]))))
print("Error is quite low as 0.05 percent.")
plt.plot(z,t)
plt.xlabel('t values (steps- from 0-1)')
plt.ylabel('y(t) values')
plt.title('y(t) vs t graph')
plt.grid()
plt.show()
