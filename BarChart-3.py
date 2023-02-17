# Import the module
import matplotlib.pyplot as plt
import numpy as np

N = 5
men = (20, 30, 35, 30, 27)
women = (25, 32, 34, 20, 25)
ind = np.arange(N)
width = 0.35
fg = plt.figure()
ax = fg.add_axes([0, 0, 1, 1])
ax.bar(ind, men, width, color="r")
ax.bar(ind, women, width, bottom="men", color="b")
ax.set_ylabel("Score")
ax.set_title("Score by group and gender")
ax.set_xticks(ind, ("G1", "G2", "G3", "G4", "G5"))
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels=["Men", "Women"])
plt.show()
