import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

def plot_circle(radius):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(-x, -y)

    # Set the aspect ratio to be equal to ensure a perfect circle
    ax.set_aspect('equal', adjustable='box')

    # Show the negative values as well by extending the axis limits
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)

    # Label the axes and add a legend
    #ax.set_xlabel('X-axis')
    #ax.set_ylabel('Y-axis')
    #ax.legend()

    plt.axis('off')
    
    # Display the plot
    plt.grid(False)
    #plt.title(f'Circle with Radius {radius} and Negative Values')
    
def plot_points(radius, period):
    
    sorted_elements = np.unique(sorted(np.unique(period))).tolist() #compute list of sorted unique numbers that appeared in the period
    #print(sorted_elements)
    elements_length = len(sorted_elements)
    rad = 2*math.pi/elements_length #calculate radian interval for each number
    init = 0
    
    x = []
    y = []
    for element in sorted_elements:
        
        x_val = radius*math.sin(init)   #calculate coordates for each number when evenly spread on the circumference with given radius
        y_val = radius*math.cos(init)
         
        x.append(x_val)
        y.append(y_val)
        
        plt.text(x_val+0.015, y_val+0.25, str(element)) #lable the points with corresponding numbers
        
       
        init  += rad    #increment radian to compute the next coordinates
    #print(f'{x}\n{y}')
    plt.scatter(x,y, color='k', marker='o', s=30)   #scatter points on graph
    
    return x, y, sorted_elements    #return list of point coordinates, sorted unique numbers
    
def plot_lines(x, y, sorted_elements, period):
    for i in range(len(period)):
        x_coords = []
        y_coords = []
        
        for k in range(2):
            if k==0:
                index = sorted_elements.index(period[i])
                #print(index)
            elif i<len(period)-1:
                index = sorted_elements.index(period[i+1])
            #print(index)
            x_coords.append(x[index])
            y_coords.append(y[index])
        #print(x_coords, y_coords)
        plt.plot(x_coords, y_coords, 'bo', linestyle='solid')
########################################################################

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

#main

host_num= 17711*2

period = accumulate_pisano(host_num)
zeros = count_zero(period)

print(f'Period: {period}\nZero count: {zeros}')

radius = 10
limit = 1000

plot_circle(radius)
    
x, y, sorted_elements = plot_points(radius, period)
plot_lines(x, y, sorted_elements, period)


plt.show()