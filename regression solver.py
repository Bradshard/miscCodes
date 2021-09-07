import numpy as np
import matplotlib.pyplot as plt
import csv

phys =  open('data15.csv', 'r')
reader = csv.reader(phys)
print(reader)
items = []
grades_range = []
for row in reader:
    items.append(row)
# Csv into a list then I will make it np array.
o=len(items)
z=len(items[1])
for i in range(1,o):
	grades_range.append(i)
pre_sol=[]
for i in range(1,o):
    pre_sol.append([])
    for i1 in range(0,z):
      pre_sol[i-1].append(int(items[i][i1]))
     #To make a numpy matrix read.
sol=np.array(pre_sol)


def meaner(n):#I calculated mean here.
    ow=len(n)
    sql=0
    for i in range(0,ow):
        sql+=(n[i])/ow
    return sql

def sxx(n,p):#This is for S subxx
    lp=len(n[:,p])
    res=0
    res+=sum((n[:,p])**2) - (((sum(n[:,p]))**2)/lp)
    return(res)
def sxy(n,l,k):#This is for S subxy
    lp=len(n[:,l])
    a1=0
    for i in range(0,lp):
        a1+= n[:,l][i]*n[:,k][i]
    b1=(sum(n[:,l])*sum(n[:,k]))/lp
    res= a1-b1
    return res
beta = sxy(sol,0,1)/sxx(sol,0)
alpha = meaner(sol[:,1])-(beta*meaner(sol[:,0]))

print(alpha)
print(beta)

dfr=1
dfe=98
dft = dfr+dfe
ssr = ((sxy(sol,0,1))**2)/sxx(sol,0)
sst = sxx(sol,1)
sse = sst-ssr
msr = ssr
mse = sse/98
f = msr/mse
r_square = ssr/sst
print(["Source" , "df" , "SS" , "MS" , "F"])
print(["Regression" , 1 , ssr, msr, f])
print(["ERROR" , 100-2 , sse , mse])
print(["Total" , 100-1 , sst])
#I choose first midterm results as x variable.
plt.scatter(sol[:,0],sol[:,1],label='data points mixed')
#couldn't manage to change colors.
plt.plot(sol[:,0],alpha + beta*sol[:,0],'-r',label='linear fitted curve')
plt.grid(True)
plt.legend()
plt.xlabel('first midterm(red)')
plt.ylabel('second midterm')
print("r^2 = ", r_square)
plt.gcf().savefig("regression graph of midterms.pdf")