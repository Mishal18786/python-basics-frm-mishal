'''debugging'''

def add(n):
    size = len(n)
    total = 0  
    iterator = 0
    print('reaached while  loop')
    while iterator < size:
        total = total + n[iterator]
        iterator +=1 #debging
        print(f'iterator{iterator} total {total}')
    return total

n = [1,2,2,5,45,84,41,54,5,45,45,5]
print(add(n))

