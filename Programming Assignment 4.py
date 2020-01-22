## Author: Roshan Rijal
## Due Date: September 30
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 4
## Program Title: Calculate Income Tax
## Program Description: This program asks total income
## and displays income tax. 
##
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.






# Obtain input from user

income = eval(input("Enter your taxable income (-1 to quit): "))

# Asks for income unless user inputs -1

while income != -1:
    
    if income <= 20000:
        
        tax = 0.02 * income     # Executes if condition 1 is true
        
    elif income <= 50000:
        tax = 400 + 0.025 * (income - 20000)    # Executes if condition 1 is false and condition 2 is true
        
    else:
        tax = 1150 + 0.035 * (income - 50000)   # Executes if above conditions are false
        
    print("Your tax is $","{0:,.0f}".format(tax),".","\n",sep="")   # Dispalys tax
    
    income = eval(input("Enter your taxable income (-1 to quit): "))    # Update loop variable    
