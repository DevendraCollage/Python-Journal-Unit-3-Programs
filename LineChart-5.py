# Import the module
import matplotlib.pyplot as plt

# x-axis values
x = [1, 2, 3, 4, 5, 6]
# y-axis values
y = [2, 4, 1, 5, 2, 6]
# plotting the points
plt.plot(x, y, color="green", linestyle="dashed", linewidth=3, marker="o", markerfacecolor="blue", markersize=10)
# setting x and y-axis range
plt.ylim(1, 8)
plt.xlim(1, 8)
# naming the x-axis
plt.xlabel("x-axis")
# naming the y-axis
plt.ylabel("y-axis")
# title of graph
plt.title("Some cool customizations!")
# show the graph using the show() function
plt.show()
