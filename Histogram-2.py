# import the module
import matplotlib.pyplot as plt

# Frequencies
age = [2, 5, 70, 20, 45, 96, 5, 78, 85, 25, 36, 52, 31, 51, 42, 63, 54]
# Setting the ranges and no of intervals
range = (0, 100)
bins = 10

# Plotting a histogram
plt.hist(age, range, bins, color="green", histtype="bar", rwidth=0.8)
# x-axis label
plt.xlabel("age")
# y-axis label
plt.ylabel("No. of pepole")
# plot title
plt.title("My Histogram")
# Show the graph using the show() function
plt.show()
