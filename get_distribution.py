import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

ref_craters_array = np.array(1, dtype=float)
det_craters_array = np.array(1, dtype=float)

with open("Craters.AW82", 'r') as ref, open("detected_diameters", 'r') as detected, open("ref_craters", 'a') as ref_craters, open("det_craters", 'a') as det_craters:
	linesr = ref.readlines()
	linesd = detected.readlines()
	
	for line in linesr:
		ref_craters.write(line[33:36] + "\n")
		if float(line[33:36]) <= 100:
			ref_craters_array = np.append(ref_craters_array, float(line[33:36])) # already in km
	for line in linesd:
		temp = line.replace("tensor(", '')
		temp = temp.replace("., device='cuda:0')", '')
		det_craters.write(temp)
		det_craters_array = np.append(det_craters_array, round(float(temp) * 0.001, 0)) # in km

plt.hist(ref_craters_array, bins=30, alpha=0.5, density=True)
plt.hist(det_craters_array, bins=30, alpha=0.5, density=True)
density1 = gaussian_kde(ref_craters_array)
x_vals1 = np.linspace(ref_craters_array.min(), ref_craters_array.max(), 400)
density2 = gaussian_kde(det_craters_array)
x_vals2 = np.linspace(det_craters_array.min(), det_craters_array.max(), 400)
plt.plot(x_vals1, density1(x_vals1), linewidth=2)
plt.plot(x_vals2, density2(x_vals2), linewidth=2)
plt.xlabel("Diameter")
plt.ylabel("Density")
plt.title("Histogram of Reference (Green) and Detected (Red) Craters")
plt.show()