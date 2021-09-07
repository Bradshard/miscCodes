import math
N = int(input('Number of Elements: '))
v1 = []
v2 = []
result=0

if N <= 0:
	print('N has to be positive you should be careful next time')
elif N>20:
	print('N is bigger than 20')
else:
	for i1 in range(0,N,1):
		v1.append(float(math.cos(math.pi*(i1+1)/16)))
	for i2 in range(0,N,1):
		v2.append(float(math.sin(math.pi*(i2+1)/21)))

for i in range(0,N,1):
	mult=v1[i]*v2[i]
	result+=mult

print("Result:",result)
