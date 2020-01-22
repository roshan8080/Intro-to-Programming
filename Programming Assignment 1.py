## Author: Roshan Rijal.
## Due Date: August 31
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 1
## Program Title: BreakEvenPoint
## Program Description: This program calculates a company’s
## break-even point, the number of units of goods the
## company must manufacture and sell in order to break even.
## It outputs the break-even point.
##
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.

fixedCosts = 5000        # Assign 5000 to fixedCosts

pricePerUnit = 8         # Assign 8 to pricePerUnit
               
costPerUnit = 6          # Assign 6 to costPerUnit

breakEvenPoint = fixedCosts / ( pricePerUnit - costPerUnit )       # Calculate breakEvenPoint

print(breakEvenPoint, "is the number of units the company must manufacture and sell in  order to break even.")         # Display breakEvenPoint
