# Import the module
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
a = np.array([22, 87, 54, 82, 10, 74, 37, 46, 83, 27, 5, 57, 62, 96])
ax.hist = (a)
ax.set_title("Histogram of result")
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_xlabel("Marks")
ax.set_ylabel("No. fo students")
plt.show()
