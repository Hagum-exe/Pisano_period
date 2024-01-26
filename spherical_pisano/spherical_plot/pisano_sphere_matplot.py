import matplotlib.pyplot as plt
import numpy as np
import math
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.style.use('ggplot')


###graphical simulation
def plot_points(period, marker_sizem, font_size):
    sorted_elements = sorted(np.unique(period))
    samples = len(sorted_elements)
    x_coords = []
    y_coords = []
    z_coords = []
    phi = math.pi * (math.sqrt(5.) - 1.)  # golden angle in radians math.pi * ((math.sqrt(5) - 1)/2)

    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        z = math.sin(theta) * radius

        x_coords.append(x)
        y_coords.append(y)
        z_coords.append(z)
        
        ax.scatter(x, y, z, color='blue', s=marker_size)
        ax.text(x, y, z, str(sorted_elements[i]), fontsize = font_size)
    return sorted_elements, x_coords, y_coords, z_coords

def plot_lines(period, sorted_elements, x, y, z, line_width):
    for i in range(len(period)):
        x_coords = []
        y_coords = []
        z_coords = []
        
        for k in range(2):
            if k==0:
                index = sorted_elements.index(period[i])
                #print(index)
            elif i<len(period)-1:
                index = sorted_elements.index(period[i+1])
            #print(index)
            x_coords.append(x[index])
            y_coords.append(y[index])
            z_coords.append(z[index])
    
        ax.plot(x_coords, y_coords, z_coords, 'bo', linestyle='solid', linewidth=line_width, color='magenta')

################################################################
###period generator
def accumulate_pisano(host_num):
    pisano_list = [0, 1, 1]
    
    i = 1
    while not (pisano_list[i] == 0 and pisano_list[i-1] ==1):
        next_term = pisano_list[i]+pisano_list[i+1] 
        
        if next_term>=host_num:
            next_term = next_term-host_num
           
        pisano_list.append(next_term) 
        i+=1
    return pisano_list[:-2]


def count_zero(repetition_list):
    zero_count=0
    for repetition in repetition_list:
        if repetition == 0:
            zero_count += 1
    return zero_count     


###main
###plt config


##user config
marker_size = 5
line_width = 1
font_size = 12
host_num = 5  
################


period = accumulate_pisano(host_num)
sorted_elements, x, y, z = plot_points(period, marker_size, font_size)
plot_lines(period, sorted_elements, x, y, z, line_width)


plt.show()
