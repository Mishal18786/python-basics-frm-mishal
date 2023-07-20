class paitent(object):
    '''meddical records'''   
    status = 'paitent'
    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll
        self.condition = []
    
    def paitent_records(self):
        print(f'paitent  records:>> {self.name}, {self.age} years, {self.roll} number \n' \
              f' \n condition information::>>  {self.condition}')
    def add_info(self,information):
        self.condition.append(information)

        
# mis = paitent('mishal', 21, 1)
# pat = paitent('patrick', 20, 2)
# rj = paitent('raghul rj', 20, 3)

##inheritancee

class inherit(paitent):
    def __init__(self, name, age, roll):
        
        self.vaccination = []
        super().__init__(name, age, roll)
    
    def add_vac(self,vaccin):
        self.vaccination.append(vaccin)
        
    def paitent_records(self):
        
        print(f' paitent {self.name}, {self.age} years,{self.roll}, num \n ' \
              f'paitent condition {self.vaccination} vaccines \n '   
               f'current condition {self.condition} \n'
               f'{self.name} ')
    
patrick = inherit('patric',20,2)
    