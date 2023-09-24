import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from sklearn.cluster import MeanShift

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
    
    sorted_elements = np.unique(sorted(np.unique(period))).tolist()
    #print(sorted_elements)
    elements_length = len(sorted_elements)
    rad = 2*math.pi/elements_length
    init = 0
    
    x = []
    y = []
    for element in sorted_elements:
        
        x_val = radius*math.sin(init)
        y_val = radius*math.cos(init)
         
        x.append(x_val)
        y.append(y_val)
        
        #plt.text(x_val+0.015, y_val+0.25, str(element))
        
        #plt.plot(x, y, 'bo', linestyle="--")
        #plt.text(x[0]-0.015, y[0]+0.25, f"{sequence[i]}")
        #if i<sequence_length-1:
            #plt.text(x[1]-0.015, y[1]+0.25, f"{sequence[i+1]}")
        init  += rad
    #print(f'{x}\n{y}')
    #plt.scatter(x,y, color='k', marker='o', s=30)
    
    return x, y, sorted_elements
    
def plot_lines(x, y, sorted_elements, period):
    line_m = []
    line_c = []
    
    #information regarding each line connecting two points according to order specified by the period
    
    for i in range(len(period)-1):
        x_coords = []
        y_coords = []
          #points are given in numerical value found as elements in 'sorted_elements'
        if period[i]!=period[i+1]:  #exclude repeating points
            for k in range(2):  #operation has to be repeated twice to acquire coordinates for plotting lines            
                if k==0:
                    index = sorted_elements.index(period[i])    #acquire number of point
                      #pair with corresponding coordinates
                    
                    
                elif i<len(period)-1:
                    index = sorted_elements.index(period[i+1])  #acquire number of the next point
                    #pair with corresponding coordinates
                    
                #print(index)
                x_coords.append(x[index])   #append coordinates to prepare for plotting line
                y_coords.append(y[index])
                
            try:
                m = (y_coords[1]-y_coords[0]) / (x_coords[1]-x_coords[0])   #calculate gradient of line
                c = ((-y_coords[1]+y_coords[0]) / (x_coords[1]-x_coords[0]))*x_coords[1]+y_coords[1]    #calculate y-intercept of line
            
            
            except ZeroDivisionError:
                 m = 100
                 c = 0
                 
           
            
            
           
            
            
            if m not in line_m and c not in line_c:
                line_m.append(m)   #write corresponding values to dictionary
                line_c.append(c)
                
            #print(x_coords, y_coords)
           
            #plt.plot(x_coords, y_coords, 'bo', linestyle='solid')   #plot lines connected by two points
   
            k+=1                
        i+=1    
    
    return line_m, line_c   #return dictionary

        

#main
radius = 10
limit = 1000
#plot_circle(radius)

#primes_df = pd.read_csv(f"pisano_prime_to_{limit}_df.csv")


org_df = pd.read_pickle(f"pisano_df.pkl")
periods = org_df['periods']
period_length = org_df['period_length']
host_num = org_df['host_num']
pisano_line_dict = {'host_num':[], 'period_length':[], 'periods':[]}

keys = ['host_num', 'period_length', 'periods']

for i in range(len(periods)):
    period = periods[i]
    #host = host_num[i]
    x, y, sorted_elements = plot_points(radius, period)
    line_m, line_c = plot_lines(x, y, sorted_elements, period)
    #print(len(line_m), len(line_c))
    pisano_line_dict['host_num'].append(host_num[i])
    pisano_line_dict['period_length'].append(period_length[i])
    pisano_line_dict['periods'].append(period)
   
    for k in range(len(line_m)):
        key_m = f'm_{k}'
        key_c = f'c_{k}'
       
        if key_m not in keys and key_c not in keys:
           keys.append(key_m)
           keys.append(key_c)
           
           pisano_line_dict[key_m] = []
           pisano_line_dict[key_c] = []
           
        pisano_line_dict[key_m].append(line_m[k])
        pisano_line_dict[key_c].append(line_c[k])

key_lengths = []
        
for i in range(len(keys)):
    length = len(pisano_line_dict[keys[i]])
    key_lengths.append(length)

max = max(key_lengths)

for i in range(len(keys)):
    length = len(pisano_line_dict[keys[i]])
    if length<max:
        for k in range (1, (max-length)+1):
            pisano_line_dict[keys[i]].append(1000)
            
        
   
    
    #plt.savefig(f'{host}.png')
    #plt.clf()
#print(pisano_line_dict)
line_df = pd.DataFrame.from_dict(pisano_line_dict)
print(line_df.head())
line_df.to_pickle("pisano_line_df.pkl")
line_df.to_csv("pisano_line_df.csv")

