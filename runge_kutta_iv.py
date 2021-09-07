import math
import numpy as np
import matplotlib.pyplot as plt

# ----- Functions ------

def analytical_func(x):
    return math.log(((x**3)/(3*math.e))+math.e)

def dydx(x, y):
    return (x**2) * (np.exp(-(y+1)))
 


def rungeKutta(x_i, y0, x, h):

    y_vals = [y0,] # append y values to a list
    x_vals = [x_i,] # append x values to a list
    n = int((x - x_i)/h) # iteration count


    y = y0
    for i in range(1, n + 1):
        """Apply Runge Kutta Formulas to find next value of y"""
        k1 = dydx(x_i, y)
        k2 = dydx(x_i + 0.5 * h, y + 0.5 * k1 * h)
        k3 = dydx(x_i + 0.5 * h, y + 0.5 * k2 * h)
        k4 = dydx(x_i + h, y + k3 * h)
 
        # ---- y value gets to the next step
        y = y + (1.0 / 6.0)*h*(k1 + 2 * k2 + 2 * k3 + k4)
        y_vals.append(y)
 
        # Update next value of x
        x_i = x_i + h
        x_vals.append(x_i)
    return y, y_vals, x_vals
 
# ---- values ----

x_i = 0
y = 1
x = 3
h = 0.3

steps = np.arange(0,3.3,h)
analytic_solns = []
for i in steps:
    analytic_solns.append(analytical_func(i))

real_end_y = analytic_solns[-1]

y, y_vals, x_vals = rungeKutta(x_i, y, x, h)

# ---- measurements ----

print('The analytical value of y at x = 3 is: {}'.format(real_end_y))
print('The numerical method value of y at x = 3 is: {}'.format(y))
print('The RK_4 error of y at x = 3 is: %{}'.format(100*(abs(y-real_end_y)/real_end_y)))

# ---- plotting ----- 


plt.plot(steps,analytic_solns, label = 'analytical_solutions',color = 'purple' ,linestyle = '--', alpha = 0.5)
plt.plot(x_vals, y_vals, label = 'RK_4', color = 'green', marker= '*',linestyle = ':' ,alpha = 0.5)
plt.title('u(x) vs x')
plt.xlabel('x values - step size 0.3')
plt.ylabel('u(x) values at x')
plt.legend()
plt.grid()


plt.show()