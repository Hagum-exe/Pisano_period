import turtle
import numpy as np
import math

###constants
radius = 180

t = turtle.Turtle()

turtle.shape('turtle')  #specify pen shape


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


###graphing
def plot_points(radius, period):
    turtle.speed(10)
    sorted_elements = np.unique(sorted(np.unique(period))).tolist() #compute list of sorted unique numbers that appeared in the period
    #print(sorted_elements)
    elements_length = len(sorted_elements)
    rad = 2*math.pi/elements_length #calculate radian interval for each number
    init = 0
    
    x = []
    y = []
    for element in sorted_elements:
        turtle.penup()
        x_val = radius*math.sin(init)   #calculate coordates for each number when evenly spread on the circumference with given radius
        y_val = radius*math.cos(init)+radius
         
        x.append(x_val)
        y.append(y_val)
        
        turtle.setpos(x_val, y_val)
        turtle.write(str(element), font=("Verdana",
                                    15, "normal"))
        init  += rad 
    return x, y, sorted_elements    #return list of point coordinates, sorted unique numbers

def plot_lines(x, y, sorted_elements, period, draw_speed):
    turtle.speed(draw_speed)
    turtle.penup()
    turtle.setpos(x[0], y[0])
    turtle.pendown()
    for i in range(1, len(period)):
        index = sorted_elements.index(period[i])
        x_coord = x[index]
        y_coord = y[index]
        turtle.setpos(x_coord, y_coord)

###main
turtle.pendown()
t.circle(radius) 

host_num = 34
draw_speed = 2
period = accumulate_pisano(host_num)
zero_count = count_zero(period)

print(period, zero_count)

x, y , sorted_elements = plot_points(radius, period)
plot_lines(x, y, sorted_elements, period, draw_speed)

turtle.exitonclick()