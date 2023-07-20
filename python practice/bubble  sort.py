# Bubble Sort

def Bubble_sort(my_list):
    swap = True
    n = len(my_list)
    
    while n > 0 and swap == True:
        n = n-1
        swap == False
        
        for i in range (n):
            if my_list[i] > my_list[i+1]:
                my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
                swap = True
    return my_list



test = [12,23,56,45,78,89,56,56,26]
print(Bubble_sort(test))