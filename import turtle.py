import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')

# Create a turtle to draw the heart
heart = turtle.Turtle()
heart.color('pink', 'red')
heart.speed(0)
heart.penup()
heart.goto(0, 0)
heart.pendown()

# Define the heart shape
def curve():
    for i in range(200):
        heart.right(1)
        heart.forward(1)

heart.begin_fill()
heart.left(140)
heart.forward(111.65)
curve()
heart.left(120)
curve()
heart.forward(111.65)
heart.end_fill()

# Create the animation
for i in range(150):
    heart.penup()
    heart.goto(0, 0)
    heart.pendown()
    heart.right(i)
    heart.forward(5)

turtle.done()