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


upper = 30
host_num = 2
fib_list = generate_fib(upper)
pisano_list = generate_pisano(host_num, fib_list)
period, repetitions = check_period(pisano_list)

print(f'pisano of n={host_num}: {pisano_list}\n')
print(f'period: {period}\n')
print(f'repetitions:{repetitions}')
