import turtle
import math

class Equation:




    def __init__(self, PositiveGrapher,NegativeGrapher,MaxX):
        self.Pturtle = PositiveGrapher
        self.Nturtle = NegativeGrapher
        self.maxx = MaxX

        # Giving  The Turtles some properties not much to change here
        self.Pturtle.speed(10)
        self.Pturtle.pencolor("red")
        self.Pturtle.pensize(0.5)

        self.Nturtle.speed(10)
        self.Nturtle.pensize(0.5)
        self.Nturtle.pencolor("red")


        self.Pturtle.hideturtle()
        self.Nturtle.hideturtle()

    def drawgraph(self,MaxX, MaxY, spacing, speed=100):
        grapher = turtle.Turtle()
        grapher.hideturtle()
        grapher.speed(speed)
        grapher.penup()
        grapher.goto(0, 0)

        YGrapher = turtle.Turtle()
        YGrapher.hideturtle()
        YGrapher.speed(speed)
        YGrapher.penup()
        YGrapher.goto(0, 0)

        grapher.goto(-MaxX, 0)
        grapher.pendown()

        YGrapher.goto(0, -MaxY)
        YGrapher.pendown()

        xPos = -MaxX
        yPos = -MaxY
        for i in range(MaxX * 2 // spacing):
            grapher.pensize(1)
            grapher.goto(xPos, MaxY)
            grapher.goto(xPos, -MaxY)
            grapher.goto(xPos, 0)
            grapher.pensize(3)
            grapher.forward(spacing)
            xPos += spacing

            YGrapher.pensize(1)
            YGrapher.goto(MaxX, yPos)
            YGrapher.goto(-MaxX, yPos)
            YGrapher.goto(0, yPos)
            YGrapher.pensize(3)
            YGrapher.goto(0, YGrapher.ycor() + spacing)
            yPos += spacing

        grapher.pensize(1)

        YGrapher.pensize(1)

        grapher.penup()
        grapher.goto(MaxX, MaxY)
        grapher.pendown()
        grapher.goto(MaxX, -MaxY)

        YGrapher.penup()
        YGrapher.goto(MaxX, MaxY)
        YGrapher.pendown()
        YGrapher.goto(-MaxX, MaxY)

    def clearLines(self):
        self.Pturtle.clear()
        self.Nturtle.clear()

    def drawLinear(self,spacing,rise,run,yIntercept):
        rise *= spacing
        run *= spacing
        yIntercept *= spacing
        self.Pturtle.penup()
        self.Nturtle.penup()

        self.Pturtle.goto(0,yIntercept)
        self.Nturtle.goto(0, yIntercept)

        self.Pturtle.pendown()
        self.Nturtle.pendown()

        Input = 0
        for i in range(self.maxx):
            self.Pturtle.goto(Input,rise/run*Input+yIntercept)
            self.Nturtle.goto(-Input, rise / run * -Input + yIntercept)
            Input+=spacing

    def QuadraticSolve(self,a, b, c):
        denominator = 2 * a
        if (a != 0):
            if (b ** 2 - 4 * a * c > -1):
                sqrt = math.sqrt(b ** 2 - 4 * a * c)
                print((-b + sqrt) / denominator)
                print((-b - sqrt) / denominator)

            # Conditional if complex solutions arise
            if (b ** 2 - 4 * a * c < 0):
                # making the solution not complex so we do not get into trouble
                newSqrt = b ** 2 - 4 * a * c
                newSqrt *= -1
                newSqrt = math.sqrt(newSqrt)
                newSqrt = str(newSqrt)

                TheList = []
                TheList.append(str(newSqrt))

                TheList.append("i")

                x = float(TheList[0])

                top = -b / (2 * a)
                x = x / (2 * a)
                TheList[0] = str(x)

                print(str(top) + " + " + TheList[0] + TheList[1])
                print(str(top) + " - " + TheList[0] + TheList[1])
        if(a == 0):
            print("This Is Not A Valid Quadratic Equation")
