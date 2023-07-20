# def summ(a,b):
#     return a + b

# print(f'The sum of 3 and 4 is {summ(2,3)}')

# def multiply(a,b = 5):
#     return a*b

# print(f'imput of 3 gives {multiply(3)}')
# print(f'imput of 3 and 2 gives {multiply(3,2)}')

# def power(a,b = 2):
#     return a**b

# print(f'imput of 10 gives {power(10)}')
# print(f'impur of 10 and 5 gives {power(10,5)}')


file = open('capitals.txt','w')

file.write("london")
file.write("mexico")
file.write("berlin")
file.write("uk")
file.write("u s")
file.close()

def copy_file(infile,outfile):
    with open (infile) as file_1:
        with open (outfile,'w') as file_2:
            file_2.write(file_1.read())

copy_file('capitals.txt','new_capitals.txt')


