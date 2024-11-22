import turtle
from PIL import Image

def save_as_jpg(canvas, fileName):
    # Assuming you have the necessary PIL functions to save as JPG
    canvas.postscript(file=fileName + ".eps")  # Save as EPS first
    Image.open(fileName + ".eps").convert('RGB').save(fileName + ".jpg")  # Convert to JPG

def drawRectangle(ttl, x, y, width, height):
    """Draws a rectangle with the given dimensions and position."""
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.end_fill()
    ttl.penup()

def drawTriangle(ttl, x1, y1, x2, y2, x3, y3, color):
    """Draws a filled triangle with the given vertices and color."""
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    ttl.goto(x2, y2)
    ttl.goto(x3, y3)
    ttl.goto(x1, y1)
    ttl.end_fill()
    ttl.penup()

# Set up the screen
turtle.setup(600, 400)  # Adjust size as needed

# Define colors
myBlue = "#003882"
myYellow = "#FCD647"
myRed = "#D12421"
myWhite = "#FFFFFF"
myGreen = "#007336"

# Create a Turtle object
turtle.speed(0)  # Set drawing speed to fastest
turtle.hideturtle()  # Hide the turtle cursor

# Draw the flag
drawRectangle(turtle, -300, 100, 600, 200, myBlue)  # Blue rectangle
drawTriangle(turtle, -300, 100, 0, 300, 300, 100, myYellow)  # Yellow triangle
drawTriangle(turtle, 0, 300, 300, 100, 300, 300, myRed)  # Red triangle
drawTriangle(turtle, 0, 300, 300, 300, 150, 300, myWhite)  # White triangle
drawTriangle(turtle, 0, 300, 150, 300, 0, 300, myGreen)  # Green triangle

# Save the image
save_as_jpg(turtle.getscreen(), "seychelles_flag")

turtle.done()