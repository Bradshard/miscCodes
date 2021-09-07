import numpy as np
import matplotlib.pyplot as plt
import math

def phi_func(x): # the function given
	return math.e**((-a)*((x-L/2)**2))

def fill_phi(u,o,m,x,t):
	for j in range(len(x)):
		m.append(phi_func(x[j]))

	return solver(u,m,o,x,t)

def solver(u,g,o,x,t): # all are the formulas that are excerpted from the pdf

	for j in range(len(x)): # t = 0, j is given as x vals in the exercise
		u[0,j] = g[j]

	for j in range(1,len(x)-1): #t = 1
		u[1,j] = (0.5)*s*(g[j+1]+g[j-1]) + (1-s)*g[j] + k*o # formula of n = 1

	for n in range(1, len(t)-1): # t > 1
		for j in range(1,len(x)-1):
			u[n+1,j] = s*(u[n,j+1] + u[n,j-1]) + 2*(1-s)*u[n,j] - u[n-1,j] # formula for bigger n

	return u

def exact_sol(x,t):
	exact = []
	for i in range(len(x)//2):
		exact.append(0.5*(phi_func(x[i]+t[i])+phi_func(x[i]-t[i])))
	for i in range(len(x)//2,len(x)):
		exact.append(0.5*(phi_func(x[-i]+t[-i])+phi_func(x[-i]-t[-i])))
	return exact

phi_vals = []

psi_val = 0 # in the example psi is given as 0. this function is 0


L = 20
h = 0.1
s = 0.9
N = 200
a = 15
k = h*math.sqrt(s)

x_val = np.linspace(0,L,N)
t_val = np.linspace(0,k*N,N) #n vals


u = np.zeros([len(t_val),len(x_val)]) # the function


q = fill_phi(u,psi_val,phi_vals,x_val,t_val)
exact_soln = exact_sol(x_val,t_val)

#e = reverse(exact_soln)


#print(len(e))
#print(len(exact_soln))

numeric = q[51] # it was the closest when I tried several values from q[0] to q[200] with step = 10
"""
for i in range(len(x_val)):
	if all(np.around(q[i],3)) == [round(num,3) for num in exact_soln]: # Couldn't make it work, will try.
		numeric = q[i]
"""
plt.plot(x_val,phi_vals,color='black', label='initial condition')
plt.plot(x_val,numeric,color='blue',label='Numerical Method')
plt.plot(x_val,exact_soln,color ='red', label='Exact Solution')
plt.legend()
plt.grid(True)
plt.title('Wave Function with initial condition')
plt.ylabel('result of the function')
plt.xlabel('x values')
plt.gcf().savefig("Wave Function Solution with NM, IC, ES, 2355170.pdf")


