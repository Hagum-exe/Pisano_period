import matplotlib.pyplot as plt
import numpy as np
import math
import random

###plt config
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.style.use('ggplot')

def fibonacci_sphere(samples):

    x_coords = []
    y_coords = []
    z_coords = []
    phi = math.pi * (math.sqrt(5.) + 1.)
  # golden angle in radians math.pi * ((math.sqrt(5) - 1)/2), phi = math.pi * (math.sqrt(5.) - 1.)

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
        

    return x_coords, y_coords, z_coords

samples = 5000
x, y, z = fibonacci_sphere(samples)

ax.scatter(x, y, z, s=3)
plt.show()
