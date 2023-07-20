# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:28:16 2022

@author: -
"""

# x = 'go'

# if (x=='go'):
#     print('go')
# else:
#     print('stop')
# print('mike')    

# x=55
# while(x!=2):
#   print(x)
#   x=x-1

class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)
    
    
p1=Points("A","B")
p1.print_point()    





# for i,x in enumerate(['A','B','C']):
#     print(i,2*x)