import numpy as np
import matplotlib.pyplot as plt
import math

def temp_resistance_change_above_0(R_0,t,R_i):
	global R_2_res_change
	A = 3.9083 * (10**(-3))
	B = -5.775*(10**(-7))
	C = 0
	R_pt = R_0 * (1 + (A*t) + ((B*(t**2))) + (C * (t-100) * (t**(3)))) # C is 0 above 0 celcius degree. increase rate approximately 0.384 for 1 degree celcius
	R_t = R_pt + R_i
	R_2_res_change.append(R_pt)
	return R_t

def temp_resistance_change_below_0(R_0,t,R_i):
	global R_2_res_change
	A = 3.9083 * (10**(-3))
	B = -5.775 * (10**(-7))
	C = -4.183 * (10**(-12))
	R_pt = R_0 * (1 + A*t + (B*(t**2)) + (C * (t-100) * (t**(3)))) # C has a value below 0 celcius degree.
	R_t = R_pt + R_i
	R_2_res_change.append(R_pt)
	return R_t

def volt_non_linear(x,y,z,t):
	y = (z/4)*(t/(x+(t/2)))
	return y

def volt(x,y,z,t):
	y = (z/4)*(t/(x+(t/(2*x))))
	return y

temp = np.arange(10,1010,10) # temperatures from 0 to 850 the Pt100 only works in -200 ~ 850 celcius degrees.
# so from 850 to 1000 we make theoretical linear resistance increase approximation. 
# One must need to know that 850 to 1000 celcius degree Pt100 won't work.

# I will assume Pt100 Resistance to Temperature Difference (RTD) as linear. Since I know
# the final and initial value, and the step size. Increase rate can be found.
R_2_pt_100 = 100 # 100 ohm at 0 celcius degree
R_2_pt_100_2 = 400 # 400 ohm at 850 celcius degree

R_2_prime = 9900 # 10k Ohm at total at 0 celcius degree
V_ab_i = 0 # initially since balanced
V_i = 5 # 5V standard.
V_ab_in = [] # array of V_ab/V_in changes
V_ab_non_linear = [] # array of V_ab/V non linear
R_2 = [] # array of R_2 changes
R_2_res_change = [] # resistance change

real_temp_array = np.arange(0,1010,10)

R_2.append(R_2_pt_100)
R_2_res_change.append(0)

for i in temp:
	R_2.append(temp_resistance_change_above_0(R_2_pt_100,i,R_2_prime))


for i in range(0,len(R_2),1):
	V_ab_in.append(volt(R_2[i],V_ab_i,V_i,R_2_res_change[i])/V_i)
	V_ab_non_linear.append(volt_non_linear(R_2[i],V_ab_i,V_i,R_2_res_change[i])/V_i)

plt.plot(real_temp_array,V_ab_in, label= "Temperature vs V_ab_in", color = "orange")
plt.plot(real_temp_array,V_ab_non_linear, label= "Temperature vs V_ab_non_linear", color = "yellow", linestyle= "dotted")
plt.xlabel("$Temperature_{C}$")
plt.ylabel("$V_{ab} / V_{in} $")
plt.title("$Temperature_{C}$ vs $V_{ab} / V_{in} $")
plt.grid(True)
plt.legend(loc ="lower right")
plt.show()