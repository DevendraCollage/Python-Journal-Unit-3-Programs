# Import the module
from pylab import *

x = linspace(-3, 3, 30)
plot(x, sin(x))
plot(x, cos(x), "r-")
plot(x, -sin(x), "g--")
# Show the graph using show() function
show()
