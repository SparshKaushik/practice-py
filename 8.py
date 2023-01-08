import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(0, 1, 1000)
mean = np.mean(data)
median = np.median(data)
std = np.std(data)
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation: {std:.2f}")
plt.hist(data)
plt.show()
