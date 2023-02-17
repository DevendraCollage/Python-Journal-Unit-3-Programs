# Import the module
import matplotlib.pyplot as plt

fig = plt.figure()
fig = fig.add_axes([0, 0, 1, 1])
lang = ["ASP.Net", "Java", "Python", "Php", "GoLang"]
student = [20, 47, 65, 85, 34]
fig.bar(lang, student)
# Shoe the graph using show() function
plt.show()
