lists = [1,2,1,4,5,6,8,7,9,6,3,2,5,5,44,256,8,8,425,6,6,5,4,1,2,6,5,4,4,2,5]
l = sorted(lists)

def Binary_search(item,lists):
    found = False
    first = 0
    last = len(lists) -1
    
    while first <= last and found == False:
        midpoint = (first + last)//2
        if lists[midpoint] == item:
            found = True
        else:
            if lists[midpoint] < item:
                first = midpoint +1
            else:
                last = midpoint -1
    return found
    
print(Binary_search(4, l)) 
print(Binary_search(65, l))   