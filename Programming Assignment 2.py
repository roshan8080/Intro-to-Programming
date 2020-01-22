## Author:Roshan Rijal
## Due Date: September 8
## Class: CSCI 2000 Section: 43078
## Instructor: Ms. Greer
## Program Assignment: 2
## Program Title: ConvertLengths
##
## Program Description: This program asks the user to
## enter a whole number of inches and converts that length
## to feet and inches. See Figure 2.22 on page 49 for a sample run.
##
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.







totalInches = int(input("Enter total inches: "))        #getting input from user and converting it into integer
feet = totalInches // 12                                #calculating feet
inch = totalInches % 12                                 #calculating inch
print(feet,"feet and",inch,"inches")                    #dislaying feet and inches    
