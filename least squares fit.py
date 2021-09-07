import numpy as np
import matplotlib.pyplot as pl
time = np.array([0.1, 0.3, 0.5, 0.7])
data = np.array([[0.05 , 0.44 , 1.23 , 2.4],[10 , 9.78, 9.84, 9.8 ],[0.1, 0.1, 0.1, 0.1]])

	

x1=sum(data[0])
y1=sum(data[1])
tot_x1y1=sum(data[0]*data[1])

alpha = ((y1*sum(data[0]**2))-(tot_x1y1*x1))/((len(data[0])*sum(data[0]**2))-((sum(data[0]))**2))

beta  = ((len(data[0])*tot_x1y1)-(x1*y1))/(((len(data[0]))*(sum(data[0]**2)))-((sum(data[0]))**2)) 

D = ((sum((data[0]**2)/(data[2]**2)))*((sum(1/data[2]**2))))-((sum(data[0]/(data[2]**2)))**2)

sigma_beta = np.sqrt((sum(1/data[2]**2))*(1/D))

sigma_alpha = np.sqrt(sum((data[0]**2)/(data[2]**2))*(1/D))

chi_square = sum(((data[1]-((beta*data[0])+alpha))**2)/(data[2]**2))
print("chi_square = " , chi_square , "sigma_alpha = " , sigma_alpha , "sigma_beta = ", sigma_beta)
print("chi_square", chi_square , " with 2 d.o.f is 66%.")
print("Since our chi_square bigger than 0.65 we can approximate as 0.65 and its probability is 72% and it is a good fit.")

pl.scatter(data[0],data[1],c = "green")
pl.plot(data[0],((data[0]*beta)+alpha),"-r",label = " fit ")
pl.errorbar(data[0],data[1],yerr=data[2],ecolor="blue",label= " data ")
pl.grid(True)
pl.xlabel("Height values")
pl.ylabel("Gravity values")
pl.title("least square fit and data graph")
pl.legend()
pl.gcf().savefig("Least Squares Method Fit Graph.pdf")
print("alpha as constant value = ", alpha, "beta as the slope value =", beta)