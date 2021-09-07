import math


# q(z = 0) = -k*rho*C(dT/dz)

def Heatflux(a,b,c,d,e):
	return round((-a*b*c*FD(d,e)),4), round((-a*b*c*MFD(d,e)),4)

def FD(T,z): # Forward derivative
	dt_dz = (T[1] - T[2])/z[1]-z[2] # h is 1.25 since difference between two parts are 1.25
	return dt_dz


def MFD(T,z): # Modified Forward derivative
	dt_dz = (-T[0] + 4* T[1] -3*T[2])/(z[0]-z[2]) # here 2h we have. h is 1.25 since difference between two parts are 1.25
	return dt_dz


rho = 1800 # kg/m**3 soil density
k = 3.5*(10**(-7)) # Coefficient of thermal diffusivity in soil
C = 840 # J/kg . Celcius degree

z = [2.5, 1.25, 0] # cm
T = [10, 12, 13.5] # in Celcius Degrees.

print("First value is for Forward derivative, Second is for Modified Forward Derivative up to 4 decimals. ",Heatflux(k,rho,C,T,z))

