import math
import numpy as np
def magnitude_position(b):
	value = np.linalg.norm(b)
	return value
def changing_position(c, a):
	regular_position = np.sum([c, initial_position], axis=0)
	print(regular_position.astype(np.int64))
	for i in range(step):
		while  (magnitude_position(regular_position) < magnitude_position(a)):
			d = np.sum([regular_position, velocity], axis=0)
			regular_position = d
			#print(regular_position)
			e = magnitude_position(d)
			f = int(e)
			finding_r_distance(f)

		#print(regular_position)
	#print(regular_position)
	return f
def finding_r_distance(x):
	r = math.sqrt(x**2)
	magnetic_field(r,60,0)
	return r
def magnetic_field(r,theta,phi):
	global every_mag_field
	global B_theta_data
	global B_r_data
	B_r = -2*K0*math.cos(math.radians(theta))/r**3
	B_theta = -math.sin(math.radians(theta))/r**3
	B_phi = 0
	B_tot = math.sqrt(B_r**2 + B_theta**2 + B_phi**2)
	B_r_data.append(B_r)
	B_theta_data.append(B_theta)
	every_mag_field.append(B_tot)
	return every_mag_field
def data_to_file(a,b,c):
	with open("B_tot_data.txt", "w+") as filehandle:
		for item in a:
			filehandle.write('%s\n' % item)
	with open("B_r_data.txt", "w+") as jordan:
		for measurements in b:
			jordan.write('%s\n' % measurements)
	with open("B_theta_data.txt", "w+") as handle:
		for data in c:
			handle.write('%s\n' % data)
	return a,b,c
#Finding the mag field for departure at 60 degrees.
B_r_data = []
B_theta_data = []
every_mag_field = []
R_earth_departure_mag = 6.400379e+6
R_earth_departure = np.array([3.2e+6,5.543e+6,0], dtype=np.float64)
R_earth_mag = 6.37e+6
# Since earth's radius is 6370km, in meters this is the value of earth's radius.
Dist_mag_btw_moon_earth = 3.8e+8
R_moon = 1.737e+6
Dist_btw_moon_earth = np.array([1.94e+8,3.36e+8,0], dtype=np.float64)
Where_to_land_at_moon = np.array([1.931e+8,3.345e+8,0], dtype=np.float64)
#from 60 to 30 triangle closest is hypotenuse.
initial_position = R_earth_departure
position = [0,0,0]
velocity = np.array([8e+3,1.38581e+4,0],  dtype=np.float64)
velocity_mag = 1.6001e+4
#Using constant velocity to change position.
theta = 60
Mu0 = math.pi*4*(10**-7)
K0 = 8*(10**15)
step = int((Where_to_land_at_moon[0]-R_earth_departure[0])/velocity[0]) # Value is same with other axis.
# m is dipole moment [A*m**2] , k0 is Earth's dipole and Mu0 is vacuum permeability
# K0 == Mu0*m/4*pi
B_at_departure = K0*(math.sqrt(1+(3*math.sin(math.radians(60)**2))))/(R_earth_mag**3)
print("First magnetic field is {} this.".format(B_at_departure))
changing_position(position, Where_to_land_at_moon)
data_to_file(every_mag_field,B_r_data,B_theta_data)
