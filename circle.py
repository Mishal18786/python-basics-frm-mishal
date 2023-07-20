import matplotlib.pyplot as plt

class circle(object):
    
    def __init__(self,radious = 5,color = 'blue'):
        self.radious = radious
        self.color = color
        
    def add_radious(self,r):
        self.radious = self.radious+r
        return (self.radious)
   
    def drawcircle(self):
        plt.gca().add_patch()





# class circle(object):
#     # Constructor
#   def __init__(self, radius=3, color='blue'):
#       self.radius = radius
#       self.color = color 
  
#   # Method
#   def add_radius(self, r):
#       self.radius = self.radius + r
#       return(self.radius)
  
#   # Method
#   def drawCircle(self):
#       plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
#       plt.axis('scaled')
#       plt.show()  