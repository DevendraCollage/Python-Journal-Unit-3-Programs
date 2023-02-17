# Import the module
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
myexmaple = ["Apple", "Banana", "Cherries", "Dtaes"]
mycolors = ["black", "hotpink", "blue", "red"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels=myexmaple, explode=myexplode, shadow=True, colors=mycolors)
plt.show()
