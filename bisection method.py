from math import *

def f(n):
	return (n**2 - 3)
# Our function

def upper_root(x,y):
	while f(x)*f(y) > 0:
		d = (x + y)/2
		y = d
	while abs((x) - (y)) > 10**(-6) :
		m = (x + y)/2
		if ((f(m) > 0 and f(y) < 0) or (f(m) < 0 and f(y) > 0)):
			x = float(m)
		else:
			y = float(m)
	print('for to only find upper root if f(x)*f(y) > 0.')
	print('here is the upper root.', y)
	print('%', ((round(y,6)/float(exact_soln[0]))*100)) # to get percentage error, here is the ratio between real value and upper root.
	return round(f(y),6)

def lower_root(x,y):
	while f(x)*f(y) > 0:
		d = (x + y)/2
		x = d
	while abs((x) - (y)) > 10**(-6) :
		m = (x + y)/2
		if ((f(m) > 0 and f(y) < 0) or (f(m) < 0 and f(y) > 0)):
			x = float(m)
		else:
			y = float(m)
	print('for to only find lower root if f(x)*f(y) > 0.')
	print('here is the lower root.', x)
	print('%', ((round(x,6)/float(exact_soln[1]))*100))  # to get percentage error, here is the ratio between real value and lower root.	
	return round(f(x),6)

# lower and upper root functions.

exact_soln = [round(sqrt(3),6),(-1)*round(sqrt(3),6)] # exact solution to 6 figures of x**2 - 3
lower_bound = float(input('Please give me an lower_bound for your function: ')) 
upper_bound = float(input('Please give me an upper_bound for your function: '))


# Bounds are determined by you specifically for the functions
if (lower_bound >= upper_bound):
	print('lower_bound must be smaller than upper_bound.')
else:
	if f(upper_bound)*f(lower_bound) > 0:
		print(lower_root(upper_bound,lower_bound))
		print(upper_root(upper_bound,lower_bound))
		# Prints both upper and lower roots for the function.
	else:
		while abs((upper_bound) - (lower_bound)) > 10**(-6) :
			m = (upper_bound + lower_bound)/2
			if ((f(m) > 0 and f(lower_bound) < 0) or (f(m) < 0 and f(lower_bound) > 0)):
				upper_bound = float(m)
			else:
				lower_bound = float(m)
		if round(f(lower_bound),6) == 0:
			print('lower_bound_root.', lower_bound)
			print('%',((lower_bound/float(exact_soln[1]))*100)) # to make ratio positive -1 in front, in percent.
			# ratios between the root we found and exact_soln is pretty close.
		else:
			print('upper_bound is the root.', upper_bound)
			print('%',(upper_bound/float(exact_soln[0]))*100) # in percent.
# ratios between the root we found and exact_soln is pretty close.