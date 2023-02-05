import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()

#turtle_instance.forward(100)

#square
#for i in range(4):
#    turtle_instance.right(90)
#    turtle_instance.forward(50)

#star
#for i in range(5):
#    turtle_instance.right(144)
#    turtle_instance.forward(360)


#polygon
num_sides = 8
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    turtle_instance.forward(side_length)
    turtle_instance.right(angle)

turtle.done()

