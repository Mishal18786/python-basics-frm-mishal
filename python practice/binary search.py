'''binary search'''

def Binary_search(item,my_list):
    found = False
    first = 0
    last = len(my_list) - 1
    
    while first <= last and found == False:
        midpoint = (first +last)//2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint] < item:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

test = [12,23,56,45,78,89,56,56,26]
test = sorted(test)
print(Binary_search(23,test))
print(Binary_search(24,test))