#bank acccount ,balance,method od withdraw deposite ,display nbalance

class bank_account(object):
    
    def __init__(self,balance = 0.0):
        self.balance = balance
    
    def display_balance(self):
        print(f'the balance of your account is {self.balance}')
    
    def deposite(self):
        amount = float(input('enter the amount'))
        self.balance += amount
        print(f'the balance is {self.balance}')
    def withdraw(self):
        
        amount = float(input('enter the money'))
        if self.balance < amount:
            print ('insufficient balance')
        else:
            self.balance -= amount
            print(f'successfully with drawn the remaining balance is {self.balance}')
            
            
##take value of radious return area
import math

class circle(object):
    
    def __init__(self,radious):
        self.radious = radious

    def calc_area(self):
        area = math.pi * (self.radious)**2
             
        return area   
    