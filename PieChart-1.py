# Import the module
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis("equal")
lang = ["C-language", "Python", "Java", "PHP", "JavaScript"]
stud = [23, 17, 35, 65, 47]
ax.pie(stud, labels=lang, autopct="%1.d%%")
plt.legend()
# show the graph using the show() function
plt.show()
