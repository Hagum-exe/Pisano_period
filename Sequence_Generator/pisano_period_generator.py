import pandas as pd

def generate_fib(upper):
    fib_list = [0, 1]
    index = 2
    while index<= upper:
        fib_list.append(fib_list[index-1]+fib_list[index-2])
        index+=1
    
    return fib_list

def generate_pisano(host_num, fib_list):
    pisano_list = []
    for num in fib_list:
        pisano_list.append(num%host_num)
    return pisano_list

def check_period(pisano_list):
    pisano_list.pop(0)
    pisano_list.pop(1)
    
    for i in range(len(pisano_list)):
        if pisano_list[i]==0 and pisano_list[i+1]==1:
            repetitions = [0,1] + pisano_list[0:i]
            return i+2, repetitions

def list_of_periods(upper,list_length):
    period_list = []
    repetition_list = []
    for host_num in range(2, list_length):
        fib_list = generate_fib(upper)
        pisano_list = generate_pisano(host_num, fib_list)
        period, repetition = check_period(pisano_list)
        period_list.append(period)
        repetition_list.append(repetition)
    return period_list, repetition_list

def count_zero(repetition_list):
    zero_count=0
    for repetition in repetition_list:
        if repetition == 0:
            zero_count += 1
    return zero_count

def list_of_num(upper):
    num_list = []
    for i in range(2,upper+1):
        num_list.append(i)
    return num_list

upper = 5000
list_length=1000

num_list = list_of_num(list_length)
#print(len(num_list))
period_list, repetition_list = list_of_periods(upper, list_length+1)
zero_count = count_zero(repetition_list)
#print(len(period_list))

pisano_dict = {'host_num':[], 'period_length':[], 'zero_count':[], 'periods':[] }

for i in range(len(num_list)):
    pisano_dict['host_num'].append(num_list[i])
    pisano_dict['period_length'].append(period_list[i])
    
    zero_count = count_zero(repetition_list[i])
    pisano_dict['zero_count'].append(zero_count)
    
    pisano_dict['periods'].append(repetition_list[i])
    

df = pd.DataFrame.from_dict(pisano_dict)
print(df.tail())
df.to_pickle("pisano_df.pkl")
#df.to_csv('pisano_df.csv')
'''
f = open('pisano_period.txt', 'w')
f.write('[host_number, period_length]\n')
for i in range(len(num_list)):
    f.write(f'[{num_list[i]}, {period_list[i]}], {repetition_list[i]}\n')
f.close() 
'''   

'''
fib_list = generate_fib(upper)
pisano_list = generate_pisano(host_num, fib_list)
period = check_period(pisano_list)
'''
#print(pisano_list)
#print(f'period length: {period}')
