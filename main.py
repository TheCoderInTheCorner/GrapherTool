import turtle
import math
import Functions

turtle.hideturtle()

# ================================================= Meet Bob And Bobby Ver Nice Friendly Turtles, It Is Very Sad That We Will Now Start Exploiting Their Kindness AndPower So That We Can Draw Cool Lines =================================================#

bob = turtle.Turtle()
bob.hideturtle()

# Best Hide The Exploitable Turtles
bobby = turtle.Turtle()
bobby.hideturtle()

# =======================================================================================================================================================================================================================================================#

# Making an Instance of the Equation Class
Grapher = Functions.Equation(bob,bobby,20)

# Making the 'Game Loop'
asking = True
# drawing The Graph
# Asking For max X and max Y values, Keep In mind The Valiues Below will be multiplied by 2
MaxX = int(input("Enter a Maximum X Length(500 recommended): "))
MaxY = int(input("Enter a Maximum Y Length(500 recommended): "))

# Spacing basically means the width and height of each cell in the graph

Spacing = int(input("Enter a Spacing Length(10 recommended): "))

# Calling The draw graph func to actually draw the graph
Grapher.drawgraph(MaxX, MaxY, Spacing)

# Game Loop
while asking:
    question = input("Linear(L) Quadratic(Q) or Quit(q)")
    if(question == "q"):
        asking = False
    if(question == "L"):
        Grapher.clearLines()

        rise = float(input("Enter The Rise: "))
        run = float(input("Enter The Run: "))
        YIntercept = float(input("Enter The Y-Intercept: "))


        Grapher.drawLinear(Spacing,rise,run,YIntercept)
    if(question == "Q"):
        Values = input("Enter 3 Values Separated By Spaces: ")
        Values = Values.split(" ")

        Grapher.QuadraticSolve(float(Values[0]),float(Values[1]),float(Values[2]))




turtle .done()