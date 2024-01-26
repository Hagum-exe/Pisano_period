def fib(upper):
    fib_list = [0, 1]
    index = 2
    while index<= upper:
        fib_list.append(fib_list[index-1]+fib_list[index-2])
        index+=1
    
    return fib_list

fib_list = fib(10000)

two_times_even_fib = []

f = open('two_times_even_fib.txt', 'w')
for i in range(0, len(fib_list)):
    num = fib_list[i]
    if i%2==0:
        num=2*num
        two_times_even_fib.append(num)
        f.write(f'{num}\n')
#print(two_times_even_fib)
f.close()

