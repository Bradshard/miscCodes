import math
N = int(input('please insert number here: '))
A = []
x0 = 2
x1 = 3
DltX = (x1-x0)/N
B = [(DltX)*math.log(x0/2),(DltX)*math.log(DltX*x1/2)]
for i in range(1,N):
	A.append((DltX)*(math.log(DltX*i+x0)))
print(sum(A)+sum(B))