import numpy as np
import matplotlib.pyplot as plt
import math

# ----- Functions ------

def analytical_func(x):
    return math.log(((x**3)/(3*math.e))+math.e)

def dydx(x, y):
    return (x**2) * (np.exp(-(y+1)))
 

# ---- values ----

h = 0.3 # Step size
steps = np.arange(0,3 + h, h) # Numerical grid
y = 1 # Initial Condition

# ---- explicit euler method
u = np.zeros(len(steps))
u[0] = y

for i in range(0, len(steps) - 1):
    u[i + 1] = u[i] + h*dydx(steps[i], u[i])


# ----- analytic solution -----
analytic_solns = []
for i in steps:
    analytic_solns.append(analytical_func(i))

real_end_y = analytic_solns[-1]

# ---- last value numeric ----

last_numeric_val = u[-1]


# ---- measurements ----

print('The analytical value of y at x = 3 is: {}'.format(real_end_y))
print('The numerical method value of y at x = 3 is: {}'.format(last_numeric_val))
print('The explicit euler error of y at x = 3 is: %{}'.format(100*(abs(last_numeric_val-real_end_y)/real_end_y)))



# ----- plotting -----

#plt.figure(figsize = (8, 4))
plt.plot(steps, u, 'bo--', label='Explicit Euler')
plt.plot(steps, analytic_solns , 'go--', label='Exact')
plt.title('Exact vs Euler Method')
plt.xlabel('x values - step size 0.3')
plt.ylabel('u(x) values at x')
plt.grid()
plt.legend(loc='upper left')
plt.show()