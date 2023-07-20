'''insertion sort 
first is sorted check sec is larger or smaller if sec is smaller we look where do we have to sort sblist to remain sorted
keep repeating'''

def insertion_sort(my_list):
    
    n = len(my_list)
    for i in range(1,n):
        
        value = my_list[i]
        j = 1
        while i > n and my_list[i] > value:
            my_list[j] = my_list[j] - 1
            j = j - 1
            my_list[j] = value
    return my_list

test = [12,23,56,45,78,89,56,56,26]

print(insertion_sort(test))
