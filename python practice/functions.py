# funct

# def hi():
#     print('hello how r u')
    
# hi()    

# def hii(name = 'mishal'):
#     print(f'hello mr {name}')
   
# hii('rocky')    

# for i in range(20):
#     print(hii('rocky'))

# fibonacci
# def fib(n):
#     '''calculate the nth tern '''
#     a = 0
#     b = 1    
#     for i in range(n):
#         a,b = b,a+b
#     return a
    
# # print(fib(20))

# for i in range(20):
#     print(fib(i))

# mean of number
# def mean_calc(first,*remainder):
#     '''calculates the mean of given numbers'''
#     mean = (first + sum(remainder)) / (1 + len(remainder))
    
#     return mean

# print(mean_calc(25,36,25,25,8,8,5,58,5,5,84,8,451,5,145,))

# recursion

# def fib_2(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1 
#     else:
#         return fib_2(n-1) + fib_2(n-2)
        
# x = fib_2(1000)
# print(x)        

# y = fib_2(35)
# print(y)

# import timeit
 

# t1 = timeit.Timer("fib(36)","from greetings import fib")
# print(t1.timeit(5))

# t2 = timeit.Timer("fib_2(36)","from greetings import fib_2")
# print(t2.timeit(5))

# def li(n,my_list=[1,2,3]):
#     my_list.append(n)
#     return my_list

# x = li(4)
# x = li(4)  wrong way

def li(n,my_list = None):
    if my_list == None:
        my_list = [1,2,3]
        my_list.append(n)
        return my_list

x = li(4)
x = li(4)    
        