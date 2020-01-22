## Author: Roshan Rijal
## Due Date: September 28
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 3
## Program Title: Calculate Total Cost
## Program Description: This program requests the number of bagels
## ordered and displays the total cost. 
##
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.




# Obtain input from user

noOfBagels = eval(input("Enter number of bagels: "))

# Analyze the given condition

if noOfBagels < 6:

    cost = noOfBagels * 0.75    # Executes if above condition is true

else:

    cost = noOfBagels * 0.60    # Executes if above condition is false

# Display cost of total bagels

print("Cost is ${0:.2f}.".format(cost))
      

