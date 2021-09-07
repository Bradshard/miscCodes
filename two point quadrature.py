from math import e, cos , sin, sqrt
import numpy as np
from scipy.integrate import quad

# Used scipy quad to show error because it gives real close values.
# real solution for e^x*cos(x) integration from 0.5 to 1.5 is 1.27508 
# Which is real close to what quad function finds.

def func(x):
	return (e**x)*cos(x)

def two_point_quadrature(a,b,f, c_1 = 1, c_2 = 1):  
	x_1 = ((b-a)/2)*(-1/sqrt(3))+((b+a)/2)
	x_2 = ((b-a)/2)*(1/sqrt(3))+((b+a)/2)
	# normally c_1 & c_2 equals to (b-a)/2 but not for two point.
	I_1 = ((b-a)/2)*(c_1*f(x_1)+c_2*f(x_2))
	return I_1

upper_bound = 1.5
lower_bound = 0.5


print("two point quadrature result for function is {} value. "
	.format(round(two_point_quadrature(lower_bound,upper_bound,func),6))) 
# two - point quadrature gives exact answer up to 3rd order.

# call quad to integrate f from 1.5 to 0.5
res, err = quad(func, 0.5, 1.5) # result and error values 

print("The numerical result is {:f} (+-{:g})"
    .format(res, err))

print("The error between real result and our quadrature is %{} value. "
	.format((res/two_point_quadrature(lower_bound,upper_bound,func))*100))