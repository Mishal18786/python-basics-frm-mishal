'''searching and sorting
linear search'''

def linear_search(item,my_list):
    i = 0
    found = False
    
    while i < len(my_list) and found == False:
        if my_list[i] == item:
            found = True
        else:
            i = i+1
    return found        

lists = [1,2,3,2,5,1,61,4,5,1]
print(linear_search(2,lists))
print(linear_search(10,lists))