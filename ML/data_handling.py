import numpy as np
import pandas as pd


'''
df = pd.read_pickle("pisano_df.pkl")
#print(df.columns)

period_lengths = df['period_length']
host_num = df['host_num']

unique_period_lengths = list(set(period_lengths))
print(unique_period_lengths)

repeat_list = []
repeat_dict = {}

for i in range(len(unique_period_lengths)):
    
    if unique_period_lengths[i] not in repeat_list:
        host_num_list = []
        for period_length in period_lengths:
            if period_length==unique_period_lengths[i]:
                host_num_list.append(host_num[i])
        
        repeat_dict[f'{unique_period_lengths[i]}'] = list(set(host_num_list))
        repeat_list.append(unique_period_lengths[i])
        
#repeat_df = pd.Series(repeat_dict)

#print(repeat_dict)

'''

array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 6, 40, 46, 37, 34, 22, 7, 29, 36, 16, 3, 19, 22, 41, 14, 6, 20, 26, 46, 23, 20, 43, 14, 8, 22, 30, 3, 33, 36, 20, 7, 27, 34, 12, 46, 9, 6, 15, 21, 36, 8, 44, 3, 47, 1, 48, 0, 48, 48, 47, 46, 44, 41, 36, 28, 15, 43, 9, 3, 12, 15, 27, 42, 20, 13, 33, 46, 30, 27, 8, 35, 43, 29, 23, 3, 26, 29, 6, 35, 41, 27, 19, 46, 16, 13, 29, 42, 22, 15, 37, 3, 40, 43, 34, 28, 13, 41, 5, 46, 2, 48, 1]

print(len(array))