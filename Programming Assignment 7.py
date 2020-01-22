## Author: Roshan Rijal
## Due Date: October 23
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 7
## Program Title: FunWithNestedLoops
## Program Description:This program use nested for loops to
##                      create four patterns of asterisks.                   
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.




# Getting User input
rows = int(input("Pattern 1 How many rows(3-20)? "))

for i in range(1,rows+1):

    for j in range(1,rows+1):

        print("*",end="")

    print()   # Changing line
    


# Getting User input
rows = int(input("\nPattern 2 How many rows (3-20)? "))

for i in range(1,rows+1):

    for j in range(1,rows):

        print(" ",end="")

    rows -= 1     # Subtracting 1 from 'rows' and assigning that value to 'rows'

    for k in range(1,i+1):

        print("*",end="")

    print()    # Changing line



# Getting User input
rows = int(input("Pattern 3 How many rows(3-20)? "))

for i in range(1,rows+1):

    for j in range(rows,i-1,-1):

        print("*",end="")

    print() # Changing line



# Getting User input
rows=eval(input("\nPattern 4 How many rows (3-20)? "))

for i in range(1,rows+1):
    print("*",end="")

    for j in range(1,i):

        print(" ",end="")
    
    print("*")

