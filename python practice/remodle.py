import re

pattern = re.compile(r'giles')

print(pattern)

pattern.match('giles')

me = pattern.match('giles')
me.group()

pattern2 = re.compile(r'g\D')

pattern2.match('giles1234')

string = 'image.jpg,image2.jpg,mydoc1.doc,mydoc2.doc,image3.jpg'

pattern3=re.compile(r'\w+\.(jpg|img)')

for m in re.compile(pattern3,string):
    print(m.group())