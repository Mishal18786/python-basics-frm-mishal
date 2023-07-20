def fib(n):
    '''calculate the nth tern '''
    a = 0
    b = 1    
    for i in range(n):
        a,b = b,a+b
    return a


def mean_calc(first,*remainder):
    '''calculates the mean of given numbers'''
    mean = (first + sum(remainder)) / (1 + len(remainder))
    
    return mean

def fib_2(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fib_2(n-1) + fib_2(n-2)

def hi():
    print('hello how r u')
    

def hii(name = 'mishal'):
    print(f'hello mr {name}')
   
    




