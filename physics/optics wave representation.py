import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

A = 5
k = 200 #rad/m.
w = 6*(10**10) # rad/s.
v = (w/k) # to make things easier. 
distance = np.arange(0,math.radians(36*math.pi),(math.radians((math.pi)/180))) # distance.
time_0 = np.linspace(0,(221*(10**-9)),1, endpoint = False) # times that we need to find.
time_1 = np.linspace(0,(221*(10**-9)),1, endpoint = True)
distance_1 = np.arange(0,math.radians(6*math.pi),(math.radians((math.pi)/180)))

a_wave_graph = []
b_wave_graph = []

a_wave_graph_1 = []
b_wave_graph_1 = []

for t in time_0:
	for x in distance:
		a = math.cos(k*3*((x)-(v*t))) # 2nd wave which is harmonic.
		a_wave_graph.append(a)
		b = A*(math.cos((k*x)-(w*t)))*(math.exp(-((x-(v*t))**2))) # 3rd wave which is decaying.
		b_wave_graph.append(b)

for t in time_1:
	for x in distance_1:
		a = math.cos(k*3*((x)-(v*t))) # 2nd wave which is harmonic.
		a_wave_graph_1.append(a)
		b = A*(math.cos((k*x)-(w*t)))*(math.exp(-((x-(v*t))**2))) # 3rd wave which is decaying.
		b_wave_graph_1.append(b)


a_patch = mpatches.Patch(color='blue', label='a_wave_graph')
b_patch = mpatches.Patch(color='red', label='b_wave_graph')

plt.title("Value of Wave vs Distance")
plt.xlabel("Distance")
plt.ylabel("Value of Wave")

plot1 = plt.figure(1)
plt.plot(distance, a_wave_graph, "b-*")
plt.plot(distance, b_wave_graph, "r-h", alpha = 0.15)

plot2 = plt.figure(2)
plt.plot(distance_1, a_wave_graph_1, "b-*")
plt.plot(distance_1, b_wave_graph_1, "r-h", alpha = 0.15)

plt.grid()
plt.legend(handles = [a_patch])
plt.legend(handles = [b_patch])

plt.show()