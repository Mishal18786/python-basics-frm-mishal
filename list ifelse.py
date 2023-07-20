# user_input = input('enter any number between 1 - 12:>>>>')

# while (not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) > 12):
#     print('must be an integer try again::>>>>')
#     user_input = input('make a selection')
# user_input = int(user_input)

# print(f'this is {user_input} times table')

# for i in range(1,13):
#     print (f'{i} x {user_input} = {i*user_input}')

# for i in range(1,13):
#     print ('=======================')
#     print('''''''''''''')
    
#     print(f'this is {i} times table')
    
#     for j in range(1,13):
#         print(f'{j} x {i} = {i*j}')
        
# user_input = input('enter a number :>>>')
# numbers = []
# while (user_input.lower()) != 'exit':
#     while not user_input.isdigit():
#         print ('enter only  number ')
#         user_input = ('enter correctly:>')
#     numbers.append(int(user_input))
#     user_input = input('enter next number')

# total=0 
# for number in numbers:
#     total+=number
    
# print(f'Mean is {total/len(numbers)}')
# print (sum(numbers)/len(numbers))

# n = input('enter a number to find the factorial:>>>')

# while (not n.isdigit()):
#     print ('please enter a number ')
#     n = input('enter correctly:>>>')
# n = int(n)
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
    
# print(fact)

# n = 20

# a = 0
# b = 1

# fibonacci = []
# for i in range(n):
#     fibonacci.append(a)
#     a,b = b,a+b
#     print(f'the first {n} fibonacci numbers are,{fibonacci}')
    

# s = '*'
# for i in range(1,7):
#     for j in range(1,6):
#         if i == 1 and j < 6:
#             print (s,end='')
#         elif i == 2 and j == 1:
#             print()
#             print(s)
#         elif i == 6 and j < 5:
#             print ()
#             print (s,end='')
#         elif i == 4 and j == 3:
#              print ()
#              print (s,end='')    
#         elif i == 3 and j == 2:
#               print ()
#               print (s,end='')
#         elif i == 3 and j == 2:
#                print ()
#                print (s,end='')    

# n = 100

# odd = []
# even = []

# for i in range(n+1):
#     if not i%2:
#         even.append(i)
#     else:
#         odd.append(i)

# print(f'the odd numbers are,{odd}')
# print (f'the even numbers are,{even}')

# modules
# import math

# import random
# print (random.randint(1,100))
# for i in range(100):
#     print (random.randint(1,100),end='  ')

# import webbrowser
# webbrowser.open('www.google.com')

# from random import randint










