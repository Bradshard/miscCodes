import numpy as np
import matplotlib.pyplot as pl
from math import *
data = np.linspace(0,360,361)
data1 = np.array(data)
print(data1)

alpha = np.linspace(-1.5,1.5,31)

nu=np.mean(data1)
def like_hood_calculator(n,k):#k stands for the mean of the data1 and n for the data
    l = 1
    for i in range(0,len(n)):
        l*= (1+alpha[i]*cos(data[i]))/(2*(1+(alpha[i]/3)))
    r= np.log(l)
    return(r)
lambda2= np.linspace(0.2,1,100), #lambdas vals
likely_hood=[]
for i in lambda2:
    likely_hood.append(like_hood_calculator(data1,i))#lambda val are found

y=list(zip(lk,lambda2))
q=sorted(y)#find lmax and sort

Lmin= np.log(np.exp((q[-1][0])-0.5))
Lmax= np.log(np.exp((q[-1][0])+0.5))
print("Lmax value and our mean value: ",q[-1])
print("Upper bound of the error interval: " , Lmax)
print("Lower bound of the error interval: ", Lmin)

pl.plot(lambda2,lk,'-r')
pl.xlabel('lambdaa')
pl.ylabel('Log-Likelihood')
pl.title('Log-Likelihood Plot for Accident Data')
pl.grid(True)


pl.gcf().savefig("Likelihood graph.pdf")


#For third question maximum value is one when Cosine is 0 so theta is 90 or 270 degree and alpha is -1.5.