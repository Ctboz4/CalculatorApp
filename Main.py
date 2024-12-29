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

    #We need functions to display the signs
    def AdditionSignDisplay(self):
        return "+"
    def SubtractionSignDisplay(self):
        return "-"
    def MultiplcationSignDisplay(self):
        return "*"
    def DivisionSignDisplay(self):
        return "/"
    
    
    
        



root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=0, column=0, columnspan=4)
display.config(state="readonly")

display.pack()

root.mainloop()