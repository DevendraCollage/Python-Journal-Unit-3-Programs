# Import the module
import matplotlib.pyplot as plt

# Line 1 points
x1 = [1, 2, 3]
y1 = [2, 4, 1]
# Plotting the line1 points
plt.plot(x1, y1, label="line 1")
# Line 2 points
x2 = [1, 2, 3]
y2 = [4, 1, 3]
# Plotting the line2 points
plt.plot(x2, y2, label="line 2")
# Naming the x-axis
plt.xlabel("x-axis")
# Naming the y-axis
plt.ylabel("y-axis")
# Title of the graph
plt.title("Two lines on a same graph!")
# Show legend on the plot
plt.legend()
# Show the graph using show() function
plt.show()
