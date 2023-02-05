import turtle

colors_turtle = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
turtle_instance = turtle.Turtle()
#t = turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    turtle_instance.pencolor(colors_turtle[i % 6])
    turtle_instance.width(i // 100 + 1)
    turtle_instance.forward(i)
    turtle_instance.left(60)

#turtle.done()
turtle.mainloop()