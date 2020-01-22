## Author: Roshan Rijal
## Due Date: October 19
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 6
## Program Title: Removing dashes from telephone number
## Program Description:This program removes the dashes from a telephone number
##                    input by the user
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.




# Opening File
infile = open("PhoneBook.txt","r")


# Stepping thru each line in the file 
for line in infile:
    

    # Removing spaces in each line at the end 
    line = line.rstrip()    


    # Declaring numAfterDashes as variable
    numAfterDashes = ""


    # Going through each number in the given line
    for n in range(line):  


        # Checking for "-"
        if line != "-":       

            numAfterDashes += line    
            

    #Dispalying new number after removing dashes
    print("Number without dashes is " + str(numAfterDashes) + ".")     


# Closing File
infile.close()     
