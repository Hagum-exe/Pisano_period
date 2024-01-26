import numpy as np
import math
import pandas as pd
import turtle

###turtle plotter
t = turtle.Turtle()

turtle.shape('turtle')  #specify pen shape
turtle.pendown()
def turtle_plot(step, speed, period):
    turtle.speed(speed)
    #turtle.right(180)
    #turtle.forward(step)
    for num in period:
        if num == 0:
            #turtle.forward(step)
            pass
        elif num%2==0:
            turtle.right(90)
            turtle.forward(step)
        
        else:
            turtle.left(90)
            turtle.forward(step)
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
host_num = 5
draw_speed = 30
step = 30

period = accumulate_pisano(host_num)
zero_count = count_zero(period)
print(zero_count, len(period))
turtle_plot(step, draw_speed, period)


turtle.exitonclick()