#importing libraries
from turtle import *
import math

#setting up screen size
setup(500,500)


#FUNCTIONS
#def whileDrawShape(turtle,sides,color):
    #turtle.pencolor(color)
    #drawnSides = 0
    #angle = 360/sides

    #while drawnSides < sides:
        #turtle.forward(50)
        #turtle.right(angle)
        #drawnSides += 1

def forDrawHouse (turtle,color):
    turtle.pencolor(color)

    for s in range(3):
        turtle.left(120)
        turtle.forward(50)
        

    for s in range(4):
        turtle.right(90)
        turtle.forward(50)

        
        

#RUNNING CODE
house = Turtle() #create turtle
house.turtlesize(2,2) #makes turtle larger
house.pensize(5) #makes pen larger
house.pendown()

another = True

print("Hi I'm a real estate agent. Want to buy a house?")
answer = input()

while another == True:
    
    if (answer == "no"):
        another = False
        print ("Ok bye.")
    elif (answer == "yes"):
        print("What color is your house?")
        chosenColor = input()

    forDrawHouse(house,chosenColor)

    print("Do you want to buy another house?")
    answer = input()

    if (answer == "no"):
        another = False
        print("Ok bye.")
    elif (answer == "yes"):
        house.penup()
        house.forward(90)
        house.pendown()
        another = True

    
#whileDrawShape(chicken,4,"green")
#chicken.penup()
#chicken.forward(100)
#chicken.pendown()
#forDrawShape(chicken,5,"pink")
#whileDrawShape(duck,5,red)

#closes the turtle window on click
exitonclick()
