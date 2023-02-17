# Import the module
import matplotlib.pyplot as plt

# x-axis values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y-axis values
y = [2, 4, 5, 6, 7, 8, 9, 11, 12, 12]
# plotting points as a scatter plot
plt.scatter(x, y, label="Stars", color="green", marker="*", s=30)
# x-axis label
plt.xlabel("x-axis")
# y-axis label
plt.ylabel("y-axis")
# plot title
plt.title("My Scatter plot")
# Showing Legend
plt.legend()
# show the graph using the show() function
plt.show()
