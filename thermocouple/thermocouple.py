import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import csv

def func(T):
	return 38.74*T + (3.319 * (10**(-2))*(T**(2))) + (2.071 * (10**(-4))*(T**(3))) - (2.195 * (10**(-6))*(T**(4)))
	# in microVolts.

temp = np.linspace(0,400, num = 41, endpoint= True).astype(int).reshape(-1,1)
max_dist = 0
E_t_1 = []

model = LinearRegression()

for i in temp:
	E_t_1.append(func(i))

E_t = np.array(E_t_1).reshape((-1,1))

model.fit(E_t, temp)
model = LinearRegression().fit(E_t, temp)

r_sq = model.score(E_t, temp)
print("Coefficient of determination: ", r_sq)
print('intercept: ', model.intercept_)
print("slope: ", model.coef_)
y_pred = model.predict(E_t)
print('predicted response:', y_pred, sep='\n')

for i in range(len(temp)):
	if ((E_t[i] - y_pred[i]) > max_dist):
		max_dist = E_t[i] - y_pred[i]
	else:
		continue

rownames = ["Temperature","E()", "predicted E(t)", "maximum_distance"] 


with open('thermocouple.csv', 'w', encoding='UTF8') as f:
	writer = csv.writer(f)

	writer.writerow(rownames)
	writer.writerow(temp)
	writer.writerow(E_t)
	writer.writerow(y_pred)
	writer.writerow(max_dist)


plt.plot(temp,E_t, color = "g", label = "Thermocouple")
plt.plot(temp, y_pred, color = "blue", label = "linear regression")

plt.xlabel("Temperature")
plt.ylabel("E function wrt temperature")
plt.title("linear regression vs normal function")

plt.legend()

plt.show()


print(max_dist)