from math import *

def f(n):
	return (n**2 - 3)
# Our function
def false_pos(x1,x2):
	while (f(x1)*f(x2) < 0):
		if (f(x1) < 10**(-6) and f(x2) > 10**(-6)):
			x_r = float(((x1*f(x2))-(x2*f(x1)))/(f(x2)-f(x1)))
			if (f(x_r) < 0):
				x1 = x_r
			elif (f(x_r) > 0):
				x2 = x_r
				print('this is the positive root.', x2)
				print('%', (x2/exact_soln[0])*100)
				return x2
		elif (f(x1) > 10**(-6) and f(x2) < 10**(-6)):
			x_r = float(((x1*f(x2))-(x2*f(x1)))/(f(x2)-f(x1)))
			if (f(x_r) < 0):
				x2 = x_r
			elif (f(x_r) > 0):
				x1 = x_r
				print('this is the negative root.', x1)
				print('%', (x1/exact_soln[1])*100)
				return x1
	return x_r

# false position method function. 
exact_soln = [round(sqrt(3),6),-1*round(sqrt(3),6)] # exact solution to 6 figures of x**2 - 3
bound_one = float(input('Please give me a boundary: '))
bound_two = float(input('Please give me an another boundary: '))
if (bound_one >= bound_two):
	print('bound_one must be smaller than bound_two.')
else:
	if (f(bound_one)*f(bound_two) > 0):
		print('no root that tis program can find. Please give other values.')
	elif (f(bound_one)*f(bound_two) == 0):
		print('bound_one or bound_two is a root.')
	else:
		print(false_pos(bound_one,bound_two))