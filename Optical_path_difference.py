import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

h = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5])
R = 10
OPD = np.array([])

for i in range(len(h)):
    OPD = np.append(OPD, R*2/(2 np.sqrt(R*2-02)) + np.sqrt(R2-02) + R2/(2 np.sqrt(R*2-(h[i])2)) + np.sqrt(R2-(h[i])*2))

h_patch = mpatches.Patch(color='blue', label='Data')

plt.title("OPD vs Height Graph")
plt.xlabel("h (cm)")
plt.ylabel("OPD (cm)")

plt.plot(h, OPD)
plt.grid()
plt.legend(handles = [h_patch])

plt.show()
