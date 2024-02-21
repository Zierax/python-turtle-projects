import random
import turtle

# Function to check whether turtle is within the screen boundaries
def isInScreen(win, turt):
    leftBound = -win.window_width() / 2
    rightBound = win.window_width() / 2
    topBound = win.window_height() / 2
    bottomBound = -win.window_height() / 2

    turtleX = turt.xcor()
    turtleY = turt.ycor()

    return leftBound < turtleX < rightBound and bottomBound < turtleY < topBound

# Function to determine the winner of the game
def determineWinner(RedInScreen, BlueInScreen):
    if RedInScreen and not BlueInScreen:
        return "Red"
    elif BlueInScreen and not RedInScreen:
        return "Blue"
    else:
        return "Draw"

# Main game logic
def playTurtleMove():
    wn = turtle.Screen()
    wn.setup(width=800, height=600)
    wn.bgcolor("white")

    Red = turtle.Turtle()
    Red.color("red")
    Red.shape("turtle")
    Red.penup()
    Red.setposition(-200, 0)

    Blue = turtle.Turtle()
    Blue.color("blue")
    Blue.shape("turtle")
    Blue.penup()
    Blue.setposition(-150, 0)

    RedInScreen = True
    BlueInScreen = True

    while RedInScreen and BlueInScreen:
        coinRed = random.randint(0, 1)
        coinBlue = random.randint(0, 1)

        angleRed = random.randint(0, 180)
        angleBlue = random.randint(0, 180)

        if coinRed == 0:
            Red.left(angleRed)
        else:
            Red.right(angleRed)

        if coinBlue == 0:
            Blue.left(angleBlue)
        else:
            Blue.right(angleBlue)

        Red.forward(50)
        Blue.forward(50)

        RedInScreen = isInScreen(wn, Red)
        BlueInScreen = isInScreen(wn, Blue)

    winner = determineWinner(RedInScreen, BlueInScreen)
    displayResult(winner)

    wn.exitonclick()

# Function to display the result
def displayResult(winner):
    resultTurtle = turtle.Turtle()
    resultTurtle.penup()
    resultTurtle.hideturtle()
    resultTurtle.color("black")
    resultTurtle.goto(0, 0)
    resultTurtle.write(f"{winner} Won", align="center", font=("Arial", 20, "bold"))

# Run the game
if __name__ == "__main__":
    playTurtleMove()
