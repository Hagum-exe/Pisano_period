def generate_lucas(upper):
    lucas_list = [1, 2]
    index = 2
    while index<= upper:
        lucas_list.append(lucas_list[index-1]+lucas_list[index-2])
        index+=1
    
    return lucas_list

upper = 50
lucas_list = generate_lucas(upper)
print(lucas_list)

