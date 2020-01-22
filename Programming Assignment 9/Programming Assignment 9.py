## Author: Roshan Rijal
## Due Date: October 30
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 9
## Program Title: FunWithFiles
## Program Description: This program reads the numbers from the file
## and displays the smallest number, the largest number, the sum of the
## numbers, and the average of the numbers.
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.



def main():
    
    # Opening File
    inFile = open("C:\\Users\\rosha\\Desktop\\CS Pdf\\Programming Assignment\\Programming Assignment 9\\numbers.txt","r")

    smallest = 1000

    largest = 1

    # Stepping thru each line in the file 
    for line in inFile:

        line = int(line)  # Coverting each line of String into integer

        if line < smallest:    
            smallest = line

        if line > largest:
            largest = line

    print("Smallest:",smallest)
    print("Largest:",largest)
    print("Sum:",getSum())  # Function call
    print("Average: {0:.1f}".format(getAverage()))   # Function call

    # Closing File
    inFile.close()


def getSum():

    sum = 0

    # Opening File
    inFile = open("C:\\Users\\rosha\\Desktop\\CS Pdf\\Programming Assignment\\Programming Assignment 9\\numbers.txt","r")

    # Stepping thru each line in the file 
    for line in inFile:

        line = int(line)  # Coverting each line of String into integer  
        sum += line

    return sum

    # Closing File
    inFile.close()
    

def getAverage():

    count = 0

    # Opening File
    inFile = open("C:\\Users\\rosha\\Desktop\\CS Pdf\\Programming Assignment\\Programming Assignment 9\\numbers.txt","r")

    # Stepping thru each line in the file 
    for line in inFile:

        count +=1

    average = getSum()/count

    return average

    # Closing File
    inFile.close()


#Program starts here.
#Call main function.
main() 






