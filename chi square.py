import csv
import math
import matplotlib.pyplot as plt
from numpy import *
from scipy import optimize

phys =  open('phys.csv', 'r')
reader = csv.reader(phys)

chi_square_val = 0
e = 2.71828 # Euler number
items = []
pre_intervals = []
counts = []

for row in reader:
	items.append(row)

for i in range(1,len(items)):
	counts.append(items[i][0])

for i1 in range(1,len(items)):
	pre_intervals.append(items[i1][1])

pre_two_intervals = "".join(pre_intervals)
intervals = pre_two_intervals.split()


def summation(d):
	summation = 0
	q = 0
	for i in d:
		summation += int(counts[q])*int(i)
		q = q + 1
	return summation


def mean(d):
	total_count = 0
	for i in range(len(counts)):
		total_count += int(d[i])
	mu  = summation(d) / total_count 
	return mu



ndf = len(counts) - 2 # Header eliminated also found mean from data.

def A_the_constant(d): # Number of intervals in 15 secs
	A = 0
	for i in range(len(d)):
		A += int(d[i])
	return A

A = A_the_constant(intervals)

def Poisson(f):
	P = []
	for i in range(len(f)):
		P.append((A*e**-(mean(intervals))*(mean(intervals)**i)/(math.factorial(i))))
	return P

Poisson_dist = Poisson(counts)

def chi_square(x,y):
	chi_square = []
	i = 0
	for c in range(len(x)):
		chi_square.append(((float(intervals[i])-float(y[i])))**2/(float(y[i])))
		i += 1
	return chi_square

for i in chi_square(counts,Poisson_dist):
	chi_square_val += i

print(chi_square(counts,Poisson_dist), "Here is the result",chi_square_val,"." )

With_degrees_of_freedom_applied = chi_square_val/ndf

print(With_degrees_of_freedom_applied," is the result after n.d.f applied, and it can be seen that the probability is not high so it is not Poisson.")

plt.plot(counts, Poisson(counts), 'bo')
plt.xlabel('Number of Counts in 15 seconds intervals')
plt.ylabel('Predicated Number of intervals with above counts')
plt.show()