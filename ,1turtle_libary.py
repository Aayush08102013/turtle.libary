'''import turtle # importing turle.
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() # defined varaible
num_sides = 6 #varable
side_length = 70
angle = 360.0 / num_sides
# itirate loop for total number of side:
for i in range (num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done() '''

# Creating A STAR

'''import turtle #importing turle.
turtle.Screen().bgcolor("Red")
turtle.Screen().setup(300,400)
star = turtle.Turtle() # defined varaible

# first triangle
star.forward(100)
star.left(120)
star.forward(100)
star.left(120)
star.forward(100)
# second triangle
star.penup()
star.right(150)
star.forward(50)


star.pendown()
star.right(90)
star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

turtle.done()'''

# Creating a spiral
import turtle #importing turle.
turtle.Screen().bgcolor("Dark Green")
turtle.Screen().setup(300,400)
spiral = turtle.Turtle() # defined varaible
size = 0
while True: # itirate loop
    for i in range(4):
        spiral.fd(size + 1)
        spiral.left(90)
        size = size - 5
    size = size + 1