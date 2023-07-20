'''Towers of Hanoi'''

A = [3,2,1]
B = []
C = []

count = 0
def Towers_of_Hanoi(A,B,C,n):
    global count
    
    if n == 1:
        disk = A.pop()
        C.append(disk)
        count +=1
    else:
        
        Towers_of_Hanoi(A, C, B, n-1)
        
        Towers_of_Hanoi(A, B, C, 1)
        
        Towers_of_Hanoi(B, A, C, n-1)
        
    return count
        
v = Towers_of_Hanoi(A,B,C, 3)

print(v)