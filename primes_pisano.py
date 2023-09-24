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


def list_of_num(upper):
    num_list = []
    for i in range(2,upper+1):
        num_list.append(i)
    return num_list

def list_of_periods(fib_list, prime_list):
    period_list = []
    repetition_list = []
    for prime in prime_list:
        #fib_list = generate_fib(upper)
     
        #prime = int(prime[i])
        prime = int(prime)
        pisano_list = generate_pisano(prime, fib_list)
        period, repetition = check_period(pisano_list)
        period_list.append(period)
        repetition_list.append(repetition)

    return period_list, repetition_list

#main########################
upper = 2000
limit = 20
f = open(f'primes_to_{str(limit)}.txt', 'r')
prime_list = f.read().split(',')
prime_list.remove('')
print(prime_list)


#num_list = list_of_num(list_length)
#print(len(num_list))
fib_list = generate_fib(upper)
period_list, repetition_list = list_of_periods(fib_list, prime_list)
#print(len(period_list))

pisano_dict = {'host_num':[], 'period_length':[], 'periods':[]}

for i in range(len(prime_list)):
    pisano_dict['host_num'].append(prime_list[i])
    pisano_dict['period_length'].append(period_list[i])
    pisano_dict['periods'].append(repetition_list[i])

df = pd.DataFrame.from_dict(pisano_dict)
print(df.tail())
df.to_csv(f"pisano_prime_to_{limit}_df.csv")
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
