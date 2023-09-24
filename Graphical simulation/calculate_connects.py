def vertical_symmetry(intersect_list, line_dict, sorted_elements):
    connects = 0
    symmetries = 0
    point_ones = line_dict['point_one'] #extract list of points from existing lines
    point_twos = line_dict['point_two']
    
    for i in range(len(point_ones)):
        point_one = point_ones[i]   #acquire points for each line
        point_two = point_twos[i]
        
        try: adj_greater = sorted_elements[sorted_elements.index(point_one)+1]  
        
        except IndexError: adj_greater = sorted_elements[0]
        
        try: adj_smaller = sorted_elements[sorted_elements.index(point_one)-1]
        
        except IndexError: adj_smaller = sorted_elements[-1]
        
        if point_two==adj_greater or point_two==adj_smaller:    #compare 'point_one' with 'point_two', if 'point_two' is adjacent to either side of 'point_one' in 'sorted_elements', the lines are connected 
            connects+=1
    #print(connects)  
    
    if connects==len(sorted_elements):  #ensure a cyclical structure is formed at the outer rim of the diagram
        symmetries = 0
        
        for intersect in intersect_list:
            if intersect[0]==0.0:
                intersect_list.remove(intersect) #exclude intersections which lie on the y-axis 
        if intersect_list==[]:
            return True
        
        #print(intersect_list)
        for i in range (len(intersect_list)):   #iterate through the list of intersections
            x_coord = intersect_list[i][0]
            
            for k in range(len(intersect_list)):
                if x_coord==(-intersect_list[k][0]):    #compare x_coordinate of each intersections and ensure a reflected coordinate is present in 'intersect_list'
                    symmetries+=1   #increment symmetrical points by 1
                    break
        
        #print(symmetries)            
        if symmetries==len(intersect_list):     #if number of symmetrical points and number of intersections are identical, the diagram must be symmetrical on the y-axis
            return True
        else:
            return False