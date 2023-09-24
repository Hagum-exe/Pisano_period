import numpy as np
import pandas as pd

upper = 20


prime_list = [3]
for num in range(upper):
    if num%2==0:
        continue
    for i in range(2, int(num/2)+1):
        if num%i == 0:
            break
        
        if i == int(num/2):
            prime_list.append(num)
            
print(prime_list)

f = open(f'primes_to_{str(upper)}.txt', 'w')

for prime in prime_list:
    f.write(f'{prime},')

f.close()