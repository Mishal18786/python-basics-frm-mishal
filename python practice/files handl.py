# files and functions

# m = open('clipping','w')

# # print(type(m))

# m.write('hello this is a new file using \python ')
# m.write('it can crreate \nopen\close\and read \write')
# m.close()

# m = open('clipping','r')

# print(type(m))
# print(m.read())
# m.close()

# print(m.readline())
# print(m.readlines())
# f = m.readlines()
# print(type(f))

# m = open('clipping','a')
# m.write('appending a file \n using python')
# m.close()

# m = open('clipping','r')
# print(m.read())
# m.close()
#######si,ple way

with open('clipping','r') as m:
    for line in m.readlines():
        print(line,end =' ')

