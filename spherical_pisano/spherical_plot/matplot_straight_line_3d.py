import numpy as np
from matplotlib import pyplot as plt

x = [1,10]
y = [2, 12]
z = [3, 13]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, 'bo', linestyle='solid', linewidth=1, color='magenta')
plt.show()