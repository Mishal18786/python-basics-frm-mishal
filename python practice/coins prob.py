

'''coins problem
turn over every sec coin 
turn every first coin
4 
 5
 6
 '''
import math
 
 # declareing the variables of coins and add
n = 1001
coins =[0]*n

for i in range(1,n):
    for j in range(0,n,i):
        coins[j] = 1 - coins[j]
        
    # add to dict
d = {}
for i,v in enumerate(coins):
    if v != 0:
        d[i]=v
    # !print the int!
l = []
for k,v in d.items():
    l.append(k)
    
l2 = [math.sqrt(num) for num in l]

