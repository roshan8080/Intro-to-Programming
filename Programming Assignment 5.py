## Author: Roshan Rijal
## Due Date: October 5
## Class: CSCI 2000
## Instructor: Ms. Tyler Greer
## Program Assignment: 5
## Program Title: CalculateArea
## Program Description: This program calculate the area of a rectangle,
## a triangle, or a circle.
##
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code content.





print("Options:")

print("-"*9)

print("1. Area of Rectangle")

print("2. Area of Triangle")

print("3. Area of Circle")

print("4. Quit")

choice = True



while choice:   # Executes only if choice equals to True 


    num = eval(input("\nMake a selection from the options menu: "))     # Obtains input from user    
    


    if num == 1:    # Executes if user inputs 1 
        
        height = eval(input("\nEnter height: "))

        width = eval(input("Enter width: "))

        areaOfRectangle = height * width

        print("Area of Rectangle is {0:.2f}".format(areaOfRectangle))   # Displays area of Rectangle



    elif num == 2:  # Executes if user inputs 2

        base = eval(input("\nEnter base: "))

        height = eval(input("Enter height: "))

        areaOfTriangle = (1/2) * base * height

        print("Area of Triangle is {0:.2f}".format(areaOfTriangle))     # Displays area of Triangle



    elif num == 3:  # Executes if user inputs 3 

        radius = eval(input("\nEnter radius: "))

        areaOfCircle = 3.141592 * radius ** 2

        print("Area of Circle is {0:.2f}".format(areaOfCircle))     # Displays area of Circle



    elif num == 4:  # Executes if user inputs 1 

        choice = False



    else:   # Executes if user inputs number expect 1,2,3 or 4 

        print("\nYou did not enter a proper number.")   # Displays Error message

    
