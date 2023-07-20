user_input = input('enter a number :>>>')
numbers = []
while (user_input.lower()) != 'exit':
    while not user_input.isdigit():
        print ('enter only  number ',user_input)
        user_input = ('enter correctly:>')
    numbers.append(int(user_input))
    user_input = input('enter next number')

total = 0 
for number in numbers:
    total += number
    
print(f'Mean is {total/len(numbers)}')
print (sum(numbers)/len(numbers))