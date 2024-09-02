import turtle

# Set up the turtl
t = turtle.Turtle()
t.speed(5)  # Set the drawing speed

# Draw a heart
t.fillcolor('red')  # Set fill color to red
t.begin_fill()

t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)

t.end_fill()
# Move to the center and write 'lucky'
t.penup()
t.goto(5, 60)
t.pendown()

t.color('white')  # Set text color to white
t.write('MOM', align='center', font=('Arial', 15, 'bold'))

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.mainloop()


