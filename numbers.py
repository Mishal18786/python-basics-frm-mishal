# num_1 = int(input('enter a number bewteen 1 - 100:>>'))
# num_2 = int(input('enter a second number between 1 - 100:>>'))
# while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
#     print ('there must be different values ,,please try again')
#     num_1 = int(input('enter a number bewteen 1 - 100:>>'))
#     num_2 = int(input('enter a second number between 1 - 100:>>'))
# if num_1 < num_2:
#     for i in range(num_1,num_2+1):
#         print(i,end= ' ')
        
#     else:
#         for i in range(num_2,num_1,+1):
#             print(i,end= ' ')


# string = input('enter any string')
# reverse = '' 

# for char in string:
#     reverse = char + reverse
# print ('your string is reversed:>>',reverse)
# print(string[::-1])

user_input = int(input('enter a number between 1 - 12 :>>'))

while (not user_input.isdigit() or user_input < 0 or user_input >12):
    print ('pleaser enter a valid in put between 1 and 12')
    user_input = input('please make a selection::::>>>')

user_input = int(user_input) 
print ('======================')
print ()
print (f'this is a {user_input} time table')
print()
for i in range(1,13):
    print(f'{i} x {user_input} = {i*user_input}')
    
    
    
    
    
    
    