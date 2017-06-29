from turtle import *
import math

# Name your Turtle.

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:


### FUNCTION
def drawShapes(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.right(angle)
        drawnSides+=1

###########################################

# RUNNING PROGRAM

another = True

Dyllen = Turtle()
Dyllen.turtlesize(2,2)
Dyllen.pensize(5)
Dyllen.pendown()

while another == True:
    print("How many sides you you want in your shape?")
    numSides = int(input())
    
    print("What color do you want your shape to be?")
    chosenColor = input()
    
    drawShapes(Dyllen,numSides,chosenColor)
    
    print("Do you want to draw another shape?")
    answer = input()
    if (answer == "no"):
        another = False

# Close window on click.
exitonclick()
