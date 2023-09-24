def generate_fib(upper):
    fib_list = [0, 1]
    index = 2
    while index<= upper:
        fib_list.append(fib_list[index-1]+fib_list[index-2])
        index+=1
    
    return fib_list

upper = 100000

num=2584

sequence = generate_fib(1000)

#test = num in sequence
#print(test.index(sequence))

#print(generate_fib(num))

f = open('2*odd_fib.txt', 'w')

for i in range (len(sequence)):
    if i%2!= 0:
        f.write(f'{2*sequence[i]}\n')
        
f.close()