import pandas as pd



def accumulate_pisano(host_num):
    pisano_list = [0, 1, 1]
    
    i = 1
    while not (pisano_list[i] == 0 and pisano_list[i-1] ==1):
        next_term = pisano_list[i]+pisano_list[i+1] 
        
        if next_term>=host_num:
            next_term = next_term-host_num
           
        pisano_list.append(next_term) 
        i+=1
    return pisano_list
        
def check_period(pisano_list):
    pisano_list.pop(0)
    pisano_list.pop(1)
    
    for i in range(len(pisano_list)):
        if pisano_list[i]==0 and pisano_list[i+1]==1:
            repetitions = [0,1] + pisano_list[0:i]
            return i+2, repetitions



def count_zero(repetition_list):
    zero_count=0
    for repetition in repetition_list:
        if repetition == 0:
            zero_count += 1
    return zero_count




host_num = 21892

pisano_list = accumulate_pisano(host_num)

#print(fib_list)

#pisano_list = generate_pisano(host_num, fib_list)

length, pisano_list = check_period(pisano_list)



zero_count = count_zero(pisano_list)

print(zero_count,' ', length, '\n')
print(pisano_list, '\n')