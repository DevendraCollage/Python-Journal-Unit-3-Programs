# Import the module
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
n_bins = 10
x = np.random.randn(1000, 3)

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)
colors = ["red", "tan", "lime"]
ax0.hist(x, n_bins, density=True, histtype="bar", color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('Bars With Legend')

ax1.hist(x, n_bins, density=True, histtype="bar", color=colors, label=colors)
ax1.set_title('Stacked Bar')

ax2.hist(x, n_bins, density=True, histtype="bar", color=colors, label=colors)
ax2.set_title('Stack Step (unfilled)')

# Make a multiple_histogram of data-sets with different length
x_multi = [np.random.randn() for n in [10000, 5000, 2000]]
ax3.hist(x_multi, n_bins, histtype="bar")
ax3.set_title("Different Sample Sizes")

fig.tight_layout()
# Show the graph using the show() function
plt.show()
