import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math



def plot_circle(radius):
    

    theta = np.linspace(0, 2 * np.pi, 100)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(-x, -y)

    #circle1 = plt.Circle((0, 0), radius, color='k')

    # Set the aspect ratio to be equal to ensure a perfect circle
    ax.set_aspect('equal', adjustable='box')

    # Show the negative values as well by extending the axis limits
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)

    # Label the axes and add a legend
    #ax.set_xlabel('X-axis')
    #ax.set_ylabel('Y-axis')
    #ax.legend()
    
    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])
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

########################################################################   
def plot_lines(x, y, sorted_elements, period):
    line_dict = {'point_one':[], 'point_two':[], 'point_one_coords':[], 'point_two_coords':[], 'line_m':[], 'line_c':[]} #create dictionary to hold information regarding each line connecting two points according to order specified by the period
    
    for i in range(len(period)-1):
        x_coords = []
        y_coords = []
          #points are given in numerical value found as elements in 'sorted_elements'
        if period[i]!=period[i+1]:  #exclude repeating points
            for k in range(2):  #operation has to be repeated twice to acquire coordinates for plotting lines            
                if k==0:
                    index = sorted_elements.index(period[i])    #acquire number of point
                    line_dict['point_one'].append(period[i])
                    line_dict['point_one_coords'].append([x[index], y[index]])  #pair with corresponding coordinates
                    
                    
                elif i<len(period)-1:
                    index = sorted_elements.index(period[i+1])  #acquire number of the next point
                    line_dict['point_two'].append(period[i+1])
                    line_dict['point_two_coords'].append([x[index], y[index]])  #pair with corresponding coordinates
                    
                #print(index)
                x_coords.append(x[index])   #append coordinates to prepare for plotting line
                y_coords.append(y[index])
                
            if (x_coords[1]-x_coords[0])==0:    #exclude division by 0 by assigning discrete values
                m = 100
            else:
                m = (y_coords[1]-y_coords[0]) / (x_coords[1]-x_coords[0])   #calculate gradient of line
            
                c = ((-y_coords[1]+y_coords[0]) / (x_coords[1]-x_coords[0]))*x_coords[1]+y_coords[1]    #calculate y-intercept of line
            
            line_dict['line_m'].append(m)   #write corresponding values to dictionary
            line_dict['line_c'].append(c)
                
            #print(x_coords, y_coords)
           
            plt.plot(x_coords, y_coords, 'bo', linestyle='solid')   #plot lines connected by two points
    i = 0
    while i<len(line_dict['point_one']):
        point_one_i = line_dict['point_one'][i]
        point_two_i = line_dict['point_two'][i]
        k = 0
        while k<len(line_dict['point_one']):
            point_one_k = line_dict['point_one'][k]
            point_two_k = line_dict['point_two'][k]
            
            #if (point_one_i==point_one_k and point_two_i==point_two_k) or (point_one_i==point_two_k and point_two_i==point_one_k):
            if point_one_i==point_two_k and point_two_i==point_one_k:   #compare origins of lines and discard repeats 
                del line_dict['point_one'][k]
                del line_dict['point_two'][k]
                del line_dict['point_one_coords'][k]
                del line_dict['point_two_coords'][k]
                del line_dict['line_m'][k]
                del line_dict['line_c'][k]
            k+=1                
        i+=1    
    line_df = pd.DataFrame(line_dict)   #convert and output as DataFrame for debugging
    print(line_df)
    return line_dict    #return dictionary

################################################################
def compute_intersect(x, y, radius, line_dict, tolerance):
    plot_coords = []
    for i in range(len(x)):
        plot_coords.append([round(x[i], 3), round(y[i], 3)]) #re-format coordinates of each plotted points
    
    intersect_list = []
    #print(len(line_dict['point_one']))
    for i in range ((len(line_dict['point_one']))):
        m_i = line_dict['line_m'][i]    #acquire gradient and y-intercept of each line
        c_i = line_dict['line_c'][i]
        
        for k in range(len(line_dict['point_one'])):
            if k!=i:
                m_k = line_dict['line_m'][k]    #acquire and compare gradient and y-intercept of lines
                c_k = line_dict['line_c'][k]
                
                if m_i!= m_k:
                    inter_x = (c_k-c_i)/(m_i-m_k)   #calculate coordinates of intersection points
                    inter_x = round(inter_x, 3)
                    inter_y = m_i*((c_k-c_i)/(m_i-m_k))+c_i
                    inter_y = round(inter_y, 3)
                    
                    if (inter_x<=radius and inter_x>=-radius)and (inter_y<=radius and inter_y>=-radius):    #ensure coordinates are within domain of interest (i.e. exist within radius)
                        coords = [inter_x,inter_y]
                        #if (coords not in intersect_list) and (coords not in plot_coords):  #ensure coordinates are not repeated
                        repeat = False
                        for intersect in intersect_list:
                            lowerx = intersect[0]-tolerance
                            upperx = intersect[0]+tolerance
                            
                            lowery = intersect[1]-tolerance
                            uppery = intersect[1]+tolerance
                            if (coords[0]>lowerx and coords[0]<upperx) and (coords[1]>lowery and coords[1]<uppery):
                                repeat = True  

                        if repeat==False:
                            for plot in plot_coords:
                                lowerx = plot[0]-tolerance
                                upperx = plot[0]+tolerance
                                
                                lowery = plot[1]-tolerance
                                uppery = plot[1]+tolerance
                                if (coords[0]>lowerx and coords[0]<upperx) and (coords[1]>lowery and coords[1]<uppery):
                                    repeat = True  
                        
                        if repeat==False:
                            intersect_list.append([inter_x,inter_y])
    #print(intersect_list)
    return intersect_list, len(intersect_list)  #return coordinates of all intersects and the number of points of intersections                 

########################################################################       
def compute_axis(x, y, intersect_list, plot_lines_dict):                          
    plot_coords = []
    for i in range(len(x)):
        plot_coords.append([round(x[i],2),round(y[i],2)])
    
    #print(plot_coords)
   
    axis_list = [] #[m, c]
    
    for i in range(len(plot_coords)):
        plot_x = plot_coords[i][0]
        plot_y = plot_coords[i][1]
        
        for intersect in intersect_list:
            inter_x = intersect[0]
            inter_y = intersect[1]
            
            if (plot_x-inter_x)==0:
                m = 100
                c=0
                
            else:
                m = round((plot_y-inter_y) / (plot_x-inter_x), 2)
                c = round(((-plot_y+inter_y)/(plot_x-inter_x))*plot_x+plot_y, 2)
            
            for i in range(len(plot_lines_dict['line_m'])):
                if (m!=plot_lines_dict['line_m'][i] and c!=plot_lines_dict['line_c'][i]) and [m,c] not in axis_list:
                    axis_list.append([m,c])
    
    print(axis_list)
    print(len(axis_list))

########################################################################           
def vertical_symmetry(intersect_list, line_dict, sorted_elements):
    rim_symmetry = False
    open_symmetry = False
    connects = 0
    symmetries = 0
    point_ones = line_dict['point_one'] #extract list of points from existing lines
    point_twos = line_dict['point_two']
    
    median = sorted_elements[len(sorted_elements)//2]
    
    for i in range(len(point_ones)):
        point_one = point_ones[i]   #acquire points for each line
        point_two = point_twos[i]
        
        try: adj_greater = sorted_elements[sorted_elements.index(point_one)+1]  
        
        except IndexError: adj_greater = sorted_elements[0]
        
        try: adj_smaller = sorted_elements[sorted_elements.index(point_one)-1]
        
        except IndexError: adj_smaller = sorted_elements[-1]
        
        if point_two==adj_greater or point_two==adj_smaller:    #compare 'point_one' with 'point_two', if 'point_two' is adjacent to either side of 'point_one' in 'sorted_elements', the lines are connected 
            connects+=1
        elif point_one==median and (point_two!=adj_greater and point_two!=adj_smaller): #compare 'point_one' with 'point_two'
            open_symmetry=True
    if connects==len(sorted_elements):  #ensure a cyclical structure is formed at the outer rim of the diagram
        rim_symmetry=True
        
    
    
    if rim_symmetry==True or open_symmetry==True:    
        for intersect in intersect_list:
            if intersect[0]==0.0:
                intersect_list.remove(intersect) #exclude intersections which lie on the y-axis 
        if intersect_list==[]:
            return True
        
        #print(intersect_list)
        
        for i in range (len(intersect_list)):   #iterate through the list of intersections
            x_coord = intersect_list[i][0]
            
            for k in range(len(intersect_list)):
                if x_coord>=(-(intersect_list[k][0]+tolerance)) and x_coord<=(-(intersect_list[k][0]-tolerance)):    #compare x_coordinate of each intersections and ensure a reflected coordinate is present in 'intersect_list'
                    symmetries+=1   #increment symmetrical points by 1
                    break
        
        #print(symmetries)            
        if symmetries==len(intersect_list):     #if number of symmetrical points and number of intersections are identical, the diagram must be symmetrical on the y-axis
            return True
        else:
            return False
    else:
        return False
   
#main
radius = 20
tolerance = 3.05

period = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 6765, 2584, 9349, 11933, 21282, 11323, 10713, 144, 10857, 11001, 21858, 10967, 10933, 8, 10941, 10949, 21890, 10947, 10945, 0, 10945, 10945, 21890, 10943, 10941, 21884, 10933, 10925, 21858, 10891, 10857, 21748, 10713, 10569, 21282, 9959, 9349, 19308, 6765, 4181, 10946, 15127, 4181, 19308, 1597, 20905, 610, 21515, 233, 21748, 89, 21837, 34, 21871, 13, 21884, 5, 21889, 2, 21891, 1] 

plot_circle(radius)
x, y, sorted_elements = plot_points(radius, period)
line_dict = plot_lines(x, y, sorted_elements, period)

intersect_list, intersect_num = compute_intersect(x, y, radius, line_dict, tolerance)

#symmetrical = vertical_symmetry(intersect_list, line_dict, sorted_elements)
#print(f'vertical symmetry:{symmetrical}')
#print(f'number of intersections:{intersect_num}, {intersect_list}')

plt.show()
#plt.savefig('test.png')