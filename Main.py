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
    
    def ClearButton(self, display):
        display.config(state="normal")  # This makes the display editable, without this you cannot change the display at all
        display.delete(0, 'end')       
        display.config(state="readonly")  #This puts the display back to read only.... Make sure you always change the state back


    # We need to make the actual buttons for each number 
    def one_Button(self, number):
        number.config(state="normal")
        number.insert('end', "1")
        number.config(state="readonly")
    def two_Button(self, number):
        number.config(state="normal")
        number.insert('end', "2")
        number.config(state="readonly")
    

#Call the class
calculator = Calculator() 
    
    
        



root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=0, column=0, columnspan=4)
display.config(state="readonly")

#Here I will put all of the Buttons, Make sure that you pass the "display" argument so that it knows where to put the number
#We are going to use the grid system instead of the pack() method
clear_button = Button(root, text="C", command=lambda: calculator.ClearButton(display))
clear_button.grid(row=1, column=0)

button_one = Button(root, text="1", command=lambda: calculator.one_Button(display))
button_one.grid(row=1, column=1)

button_two = Button(root, text="2", command=lambda: calculator.two_Button(display))
button_two.grid(row=1,column=2)







#Pack everything here



root.mainloop()