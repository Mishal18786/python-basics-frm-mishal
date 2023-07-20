# alpha = 'abcdefghijklmnopqrstuvwxyz'

# alpha_list = list(alpha)

# for count,items in enumerate(alpha_list):
#     print(count,items)
    
    
# for i,n in enumerate(alpha_list, start=100):
#     print(i,n)


# sets

a = [1,1,2,2,3,3,4,4,5,5]
b = [6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,1,51,5,1,5,1] 

a= set(a)
b= set(b)

print(a,b)

print(a&b)  #intersection
print(a^b)  #symmetric difference
print(a-b)  #union
print(a|b)  #difference

z = None #empty vaeiable can use later