# import the module
import matplotlib.pyplot as plt
import numpy as np

data = ([30, 25, 50, 20], [40, 24, 71, 96], [45, 12, 20, 46])
x = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(x + 0.00, data[0], color='b', width=0.25)
ax.bar(x + 0.25, data[1], color='g', width=0.25)
ax.bar(x + 0.50, data[2], color='r', width=0.25)
# Show the graph using show() function
plt.show()
