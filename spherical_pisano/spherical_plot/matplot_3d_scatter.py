import matplotlib.pyplot as plt
import numpy as np
import math
import random

fig = plt.figure()
ax = fig.add_subplot(projection='3d')



x = []
y = []
z = []
for i in range(0, 50):
    x.append(random.randint(0, 100))
    y.append(random.randint(0, 100))
    z.append(random.randint(0, 100))
    
    
ax.scatter(x, y, z)
plt.show()

