from turtle import *
import math

# Name your Turtle.

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:

Dyllen = Turtle()
Dyllen.pencolor("purple")
Dyllen.turtlesize(2,2)
Dyllen.pensize(5)
Dyllen.pendown()

print ("How many sides you want?")
sides = input()
sides2=int(sides)


drawnSides = 0

angle = 360/sides2

while drawnSides < sides2:
    Dyllen.forward(50)
    Dyllen.right(angle)
    drawnSides+=1

Dyllen.penup()
Dyllen.forward(90)
Dyllen.pendown()

for side in range(sides2):
    Dyllen.forward(50)
    Dyllen.right(angle)



# Close window on click.
exitonclick()
