import matplotlib.pyplot as plt

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
            return i+2

def list_of_periods(upper,list_length):
    period_list = []
    for host_num in range(2, list_length):
        fib_list = generate_fib(upper)
        pisano_list = generate_pisano(host_num, fib_list)
        period = check_period(pisano_list)
        period_list.append(period)
    return period_list

def list_of_num(upper):
    num_list = []
    for i in range(2,upper):
        num_list.append(i)
    return num_list

upper = 1000
list_length=500
#period_list = list_of_periods(upper, list_length)
num_list = list_of_num(list_length)
print(num_list)
#print(period_list)
#print(len(period_list))
#print(len(num_list))

x=num_list
y=period_list

plt.scatter(x,y, label='scatter', color='c', marker='x', s=10)

plt.xlabel('host_number')
plt.ylabel('period_length')
plt.title('period_relationship')
plt.show()
