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
    
    sorted_elements = np.unique(sorted(np.unique(period))).tolist()
    
    count_num = []
    for i in range(max(sorted_elements)+1):
        count_num.append(i)
    
    #print(sorted_elements)
    elements_length = len(count_num)
    rad = 2*math.pi/elements_length
    init = 0
    
    x = []
    y = []
    for num in count_num:
        
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
    plt.scatter(x,y, color='k', marker='o', s=30)
    #print(x, y, count_num)
    return x, y, sorted_elements
    
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
            
        

#main
radius = 10
limit = 1000
#plot_circle(radius)

#primes_df = pd.read_csv(f"pisano_prime_to_{limit}_df.csv")


df = pd.read_pickle(f"pisano_df.pkl")
periods = df['periods']
host_num = df['host_num']





for i in range(len(periods)):
    plot_circle(radius)
    #period = []
    #for num in periods[i]:
    #    try: period.append(int(num))
    #    except ValueError: pass
    #print(period)
    period = periods[i]
    host = host_num[i]
    x, y, sorted_elements = plot_points(radius, period)
    plot_lines(x, y, sorted_elements, period)
    plt.savefig(f'{host}.png')
    plt.clf()



'''
period = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 77, 10, 87, 97, 184, 281, 165, 146, 11, 157, 168, 25, 193, 218, 111, 29, 140, 169, 9, 178, 187, 65, 252, 17, 269, 286, 255, 241, 196, 137, 33, 170, 203, 73, 276, 49, 25, 74, 99, 173, 272, 145, 117, 262, 79, 41, 120, 161, 281, 142, 123, 265, 88, 53, 141, 194, 35, 229, 264, 193, 157, 50, 207, 257, 164, 121, 285, 106, 91, 197, 288, 185, 173, 58, 231, 289, 220, 209, 129, 38, 167, 205, 72, 277, 49, 26, 75, 101, 176, 277, 153, 130, 283, 113, 96, 209, 5, 214, 219, 133, 52, 185, 237, 122, 59, 181, 240, 121, 61, 182, 243, 125, 68, 193, 261, 154, 115, 269, 84, 53, 137, 190, 27, 217, 244, 161, 105, 266, 71, 37, 108, 145, 253, 98, 51, 149, 200, 49, 249, 298, 247, 245, 192, 137, 29, 166, 195, 61, 256, 17, 273, 290, 263, 253, 216, 169, 85, 254, 39, 293, 32, 25, 57, 82, 139, 221, 60, 281, 41, 22, 63, 85, 148, 233, 81, 14, 95, 109, 204, 13, 217, 230, 147, 77, 224, 1, 225, 226, 151, 77, 228, 5, 233, 238, 171, 109, 280, 89, 69, 158, 227, 85, 12, 97, 109, 206, 15, 221, 236, 157, 93, 250, 43, 293, 36, 29, 65, 94, 159, 253, 112, 65, 177, 242, 119, 61, 180, 241, 121, 62, 183, 245, 128, 73, 201, 274, 175, 149, 24, 173, 197, 70, 267, 37, 4, 41, 45, 86, 131, 217, 48, 265, 13, 278, 291, 269, 260, 229, 189, 118, 7, 125, 132, 257, 89, 46, 135, 181, 16, 197, 213, 110, 23, 133, 156, 289, 145, 134, 279, 113, 92, 205, 297, 202, 199, 101, 0, 101, 101, 202, 3, 205, 208, 113, 21, 134, 155, 289, 144, 133, 277, 110, 87, 197, 284, 181, 165, 46, 211, 257, 168, 125, 293, 118, 111, 229, 40, 269, 9, 278, 287, 265, 252, 217, 169, 86, 255, 41, 296, 37, 33, 70, 103, 173, 276, 149, 125, 274, 99, 73, 172, 245, 117, 62, 179, 241, 120, 61, 181, 242, 123, 65, 188, 253, 141, 94, 235, 29, 264, 293, 257, 250, 207, 157, 64, 221, 285, 206, 191, 97, 288, 85, 73, 158, 231, 89, 20, 109, 129, 238, 67, 5, 72, 77, 149, 226, 75, 1, 76, 77, 153, 230, 83, 13, 96, 109, 205, 14, 219, 233, 152, 85, 237, 22, 259, 281, 240, 221, 161, 82, 243, 25, 268, 293, 261, 254, 215, 169, 84, 253, 37, 290, 27, 17, 44, 61, 105, 166, 271, 137, 108, 245, 53, 298, 51, 49, 100, 149, 249, 98, 47, 145, 192, 37, 229, 266, 195, 161, 56, 217, 273, 190, 163, 53, 216, 269, 185, 154, 39, 193, 232, 125, 57, 182, 239, 121, 60, 181, 241, 122, 63, 185, 248, 133, 81, 214, 295, 209, 204, 113, 17, 130, 147, 277, 124, 101, 225, 26, 251, 277, 228, 205, 133, 38, 171, 209, 80, 289, 69, 58, 127, 185, 12, 197, 209, 106, 15, 121, 136, 257, 93, 50, 143, 193, 36, 229, 265, 194, 159, 53, 212, 265, 177, 142, 19, 161, 180, 41, 221, 262, 183, 145, 28, 173, 201, 74, 275, 49, 24, 73, 97, 170, 267, 137, 104, 241, 45, 286, 31, 17, 48, 65, 113, 178, 291, 169, 160, 29, 189, 218, 107, 25, 132, 157, 289, 146, 135, 281, 116, 97, 213, 10, 223, 233, 156, 89, 245, 34, 279, 13, 292, 5, 297, 2, 299, 1]

plot_circle(radius)
x, y, sorted_elements = plot_points(radius, period)
plot_lines(x, y, sorted_elements, period)
plt.show()
'''
