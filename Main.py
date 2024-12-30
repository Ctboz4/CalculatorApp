from tkinter import *



#I need to make a calculator class that holds all of the methods needed for a calculator
class Calculator:
    #We want to be able to store whatever numbers and operators are being used
    def __init__(self):
        self.first_number_used = None
        self.second_number_used = None
        self.Operator = None



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

    #These buttons will be the ones for the functionality
    def addition_button(self, number):
        #This should get the value of what in the display
        current_value = display.get()

        self.first_number_used = int(current_value)
        self.Operator = "+"
        

        display.config(state="normal")
        display.delete(0, 'end')
        display.config(state="readonly")

    def equals_Button(self, display):

        secondNumber = int(display.get()) #This gets the number that is in the display
        self.second_number_used = secondNumber #This stores the number in the display to the self.second_number_used variable used in the Class
        
        #now we need an if statement to know what operator is being used and to use it correctly
        if self.Operator == "+":
            answer = self.Addition(self.first_number_used, self.second_number_used)
        elif self.Operator == "-":
            answer = self.Subtraction(self.first_number_used, self.second_number_used)
        elif self.Operator == "*":
            answer = self.Multiplcation(self.first_number_used, self.second_number_used)
        elif self.Operator == "/":
            answer = self.Division(self.first_number_used, self.second_number_used)
        else:
            answer = "Error"

        #This should put the answer into the display
        display.config(state="normal")
        display.delete(0, 'end')  # Clear the current display
        display.insert('end', str(answer))  # Display the result
        display.config(state="readonly")

        
        self.first_operand = None
        self.second_operand = None
        self.current_operator = None
        
    
    


#Call the class
calculator = Calculator() 
    
    
        



root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=0, column=0, columnspan=4)
display.config(state="readonly")

#Here I will put all of the number Buttons, Make sure that you pass the "display" argument so that it knows where to put the number
#We are going to use the grid system instead of the pack() method


button_one = Button(root, text="1", command=lambda: calculator.one_Button(display))
button_one.grid(row=1, column=1)

button_two = Button(root, text="2", command=lambda: calculator.two_Button(display))
button_two.grid(row=1,column=2)

#Here is all the function buttons
clear_button = Button(root, text="C", command=lambda: calculator.ClearButton(display))
clear_button.grid(row=1, column=0)

equals_button = Button(root, text="=", command=lambda: calculator.equals_Button(display))
equals_button.grid(row=2, column=3)

addition_button = Button(root, text="+",command=lambda: calculator.addition_button(display))
addition_button.grid(row=1, column=3)









root.mainloop()