## Author: Roshan Rijal
## Due Date: October 26
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 8
## Program Title: FunWithFunctions
## Program Description:This program uses functions to
##                      create four patterns of asterisks.                   
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.


def main():

    # Print Menu
    print("Options:")
    print("Pattern 1")
    print("Pattern 2")
    print("Pattern 3")
    print("Pattern 4")
    
    getChoice()    # Call getChoice function


def getChoice():

     # Obtains User input
    options = input("\nEnter 1, 2, 3, or 4 to choose a pattern to display. Enter 5 to exit. ")
    
    # Loop continues until user enters 5
    while(options!="5"):
        
        if not options.isdigit():
            print("Input must be a number")   # User did not enter a number

        else:
            options=int(options)
            getRows(options)  # Call getRows function

        options = input("\nEnter 1, 2, 3, or 4 to choose a pattern to display. Enter 5 to exit. ")
        

def getRows(options):
    if options == 1:    # User chooses Pattern 1

        # Getting user input
        rows = int(input("\nPattern 1 How many rows(3-20)? "))

        if rows >= 3 and rows <=20:
            Pattern1(rows)  # Call Pattern1 function 

        else:
            print("Values must be between 3 and 20")

    if options == 2:   # User chooses Pattern 2

        # Getting user input
        rows = int(input("\nPattern 2 How many rows (3-20)? "))

        if rows >= 3 and rows <=20:
            Pattern2(rows)  # Call Pattern2 function 

        else:
            print("Values must be between 3 and 20")
          
    if options == 3:    # User chooses Pattern 3

        # Getting user input
        rows = int(input("\nPattern 3 How many rows(3-20)? "))

        if rows >= 3 and rows <=20:
            Pattern3(rows)   # Call Pattern3 function
        else:
            print("Values must be between 3 and 20")

    if options == 4:    # User chooses Pattern 4

        # Getting user input
        rows=eval(input("\nPattern 4 How many rows (3-20)? "))

        if rows >= 3 and rows <=20:
            Pattern4(rows)    # Call Pattern4 function

        else:
            print("Values must be between 3 and 20")
        

    
        
def Pattern1(rows):   

    for i in range(1,rows+1):

        for j in range(1,rows+1):

            print("*",end="")

        print()   # Changing line
    




def Pattern2(rows):    

    for i in range(1,rows+1):

        for j in range(1,rows):

            print(" ",end="")

        rows -= 1     # Subtracting 1 from 'rows' and assigning that value to 'rows'

        for k in range(1,i+1):

            print("*",end="")

        print()    # Changing line





def Pattern3(rows):    

    for i in range(1,rows+1):

        for j in range(rows,i-1,-1):

            print("*",end="")

        print() # Changing line





def Pattern4(rows):

    for i in range(1,rows+1):
        print("*",end="")

        for j in range(1,i):

            print(" ",end="")
    
        print("*")



#Program starts here.
#Call main function.
main()

