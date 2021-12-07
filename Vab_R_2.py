import numpy as np
import matplotlib.pyplot as plt
import math

def volt_non_linear(x,y,z,t):
	y = (z/4)*(t/(x+(t/2)))
	return y

def volt(x,y,z,t):
	y = (z/4)*(t/(x+(t/(2*x))))
	return y

def change_in_resistance(x,y):
	return x + y

R_2_i = 10000 # 10k Ohm
V_ab_i = 0 # initially since balanced
V_i = 5 # 5V as standard
V_ab_in = [] # array of V_ab/V_in changes
V_ab_non_linear = [] # array of V_ab/V non linear
R_2 = [] # array of R_2 changes

delta_R = np.arange(-10000,10100,100) # R_2 changes

for i in delta_R:
	V_ab_in.append(volt(R_2_i,V_ab_i,V_i,i)/V_i)
	V_ab_non_linear.append(volt_non_linear(R_2_i,V_ab_i,V_i,i)/V_i)
	R_2.append(change_in_resistance(R_2_i,i))

plt.plot(delta_R,V_ab_in, label= "change in resistance vs V_ab_in", color = "orange")
plt.plot(delta_R,V_ab_non_linear, label= "change in resistance vs V_ab_non_linear", color = "yellow", linestyle= "dotted")
plt.plot(R_2,V_ab_in, label = "single varying resistance vs V_ab_in", color = "green")
plt.plot(R_2,V_ab_non_linear, label = "single varying resistance vs V_ab_non_linear", color = "brown", linestyle= "dotted")
plt.xlabel("$R_{2}$")
plt.ylabel("$V_{ab} / V_{in} $")
plt.title("$R_{2}$ vs $V_{ab} / V_{in} $")
plt.grid(True)
plt.legend(loc ="lower right")
plt.show()