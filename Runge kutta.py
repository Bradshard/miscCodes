import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax


def du_dx(x,u): # function derivative
	return (x**2)*math.e**(-(u+1))

def u(x): # the real function
	return math.log(math.e+(x**3/(3*math.e)))

u_0 = 1 #first value
u_i = u_0 # to iterate
alpha = 1 # alpha value
h = 0.01 # step size

step = np.arange(0,3.01,h) # to get till 3 from 0 since both ends are in the interval
x_val = []
u_val = []
u_val_real_func = []

for i in step:
	k_1 = h*du_dx(i,u_i)
	k_2 = h*du_dx(i+h,u_i+k_1)
	u_i = u_i +((1-(1/(2*alpha)))*k_1)+((1/(2*alpha))*k_2) # values with step taken.
	u_val.append(u_i)
	u_val_real_func.append(u(i))
	x_val.append(i)

print('u value at u(3) is {}'.format(u_val[300]))
print('error from the real u(3) is %{}'.format(100*(1-(u(3)/u_val[300])))) # really low error.
plt.plot(x_val,u_val,'-b' , label= 'Runge-Kutta function')
plt.plot(x_val,u_val_real_func, 'r:', label = 'Realfunction')
plt.xlabel('Interval')
plt.ylabel('Runge-Kutta Values')
plt.title('RK2 in x # [0 - 3]') # plot for 0 <= x <= 3
plt.legend()
plt.grid()
plt.show()

