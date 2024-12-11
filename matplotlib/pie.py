import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["cyan", "hotpink", "r", "#4CAF50"]

plt.pie(y, labels=mylabels , explode=myexplode, shadow = False , colors=mycolors)
plt.legend(title = "Four Fruits:")
plt.show() 