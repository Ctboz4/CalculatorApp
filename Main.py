from tkinter import *



#I need to make a calculator class that holds all of the methods needed for a calculator
class Calculator:
    #This is the addition function
    def Addition(self, a, b):
        c = a + b
        return c
    
    #this is the subtraction function
    def Subtraction(self, a, b):
        c = a - b
        return c
    #this is the multiplcation function
    def Multiplcation(self, a, b):
        c = a * b
        return c
    
    #this is the division function
    def Division(self, a, b):
        #This will check if you try to divide by Zero
        if a == 0 or b == 0:  
            return "You cannot divide by 0!"
        c = a / b
        return c
        



calculator = Calculator()

result = calculator.Multiplcation(6, 10)

print(result)
    