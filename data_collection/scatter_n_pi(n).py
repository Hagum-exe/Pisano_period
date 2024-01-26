import matplotlib.pyplot as plt


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

pisanodict = {'hostnum':[], 'period_length': [], 'zero_count': [], 'periods': []}

for i in range(2, 1001):
    pisano_list = accumulate_pisano(i)
    zeros = count_zero(pisano_list)
    pisanodict['hostnum'].append(i)
    pisanodict['period_length'].append(len(pisano_list))
    pisanodict['zero_count'].append(zeros)
    pisanodict['periods'].append(pisano_list)
    
    
plt.scatter(pisanodict['hostnum'], pisanodict['period_length'], color='black', s=4)
plt.title('π(n) against n')
plt.xlabel("n")
plt.ylabel("π(n)")
plt.show()