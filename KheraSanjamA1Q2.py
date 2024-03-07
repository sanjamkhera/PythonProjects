# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:28:52 2020

@author: sanjam
"""

# User Input
inpX1 = input("What is x1?>")
inpY1 = input("What is y1?>")
inpX2 = input("What is x2?>")
inpY2 = input("What is y2?>")
rise =(int(inpY2)-int(inpY1))
run = (int(inpX2)-int(inpX1))


# Check if run is zero before performing division
if run == 0:
    # If run is zero, print an error message and exit the program
    print("Error: The x-coordinates are the same, so the line is vertical and the slope is undefined.")
    exit()

# Calculate the slope of the line
m = float(rise/run)

# Calculate the y-intercept of the line
b = int(inpY1)-(m*(int(inpX1)))

# Print the equation of the line
print("y = m*x + b\ny = ({:.2f})*x + {:.2f}".format(m,b))

# Ask the user if they want to input an x or y coordinate, or get a set of coordinates
userInp = input("Would you like to enter x or y coordinate?\nType x , y or set>")

if userInp == "x":
    # If the user wants to input an x coordinate, ask for the x value
    inpX = input("Enter x Value?>")
    x = int(inpX)

    # Calculate the corresponding y value using the line equation
    y = (m*x) + b

    # Print the coordinate pair (x, y)
    print("your coordiante set is ({:.2f}),({:.2f})".format(x,y))
    print("Done!")
elif userInp == "y":
    # If the user wants to input a y coordinate, ask for the y value
    inpY = input("Enter y Value?>")
    y = int(inpY)

    # Calculate the corresponding x value by rearranging the line equation
    x = ((y-b)/m)

    # Print the coordinate pair (x, y)
    print("your coordiante set is ({:.2f}),({:.2f})".format(x,y))
    print("Done!")
else:
    # If the user input is not "x" or "y", this part of the code will execute
    # You might want to add some code here to handle this case
    x = -10
    for x in range(-10,11,2):
        y = (m*x) + b
        print(x,y)
print("Done!")