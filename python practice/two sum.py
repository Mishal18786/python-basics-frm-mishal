def two_sum(num,target):
    
    d = {}
    
    for i in range(len(num)):
        if target - num[i] in d:
            print(d)
            return [d[target - num[i]],i]
        d[num[i]] = i
        
    return -1

L = [1,2,3,4,5,6,7,8,9]
print(two_sum(L,10))    
