import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()

# prompt the user for a size
size = input("How big would you like your square to be?")
size = int(size)

# draw a square with sides of the given size
alex.forward(size)
alex.left(90)
alex.forward(size)
alex.left(90)
alex.forward(size)
alex.left(90)
alex.forward(size)
alex.left(90)
