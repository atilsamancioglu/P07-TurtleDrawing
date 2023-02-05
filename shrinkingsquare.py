import turtle  # Outside_In

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")
turtle_instance = turtle.Turtle()
turtle_instance.color("blue")


def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

shrinkingSquare(146)
shrinkingSquare(126)
shrinkingSquare(106)
shrinkingSquare(86)
shrinkingSquare(66)
shrinkingSquare(46)
shrinkingSquare(26)

turtle.done()