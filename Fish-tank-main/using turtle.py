import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Aquarium")

# Function to draw a fish
def draw_fish(x, y, color):
    fish = turtle.Turtle()
    fish.penup()
    fish.goto(x, y)
    fish.pendown()
    fish.color(color)
    fish.begin_fill()
    fish.circle(30, 180)  # Draw a half-circle for the fish body
    fish.circle(30//2, 180)  # Draw the tail
    fish.left(180)
    fish.circle(30//2, 180)
    fish.end_fill()
    fish.hideturtle()

# Function to draw seaweed
def draw_seaweed(x, y, height, color):
    seaweed = turtle.Turtle()
    seaweed.penup()
    seaweed.goto(x, y)
    seaweed.pendown()
    seaweed.color(color)
    seaweed.begin_fill()
    for i in range(height):
        seaweed.left(45)
        seaweed.forward(20)
        seaweed.right(90)
        seaweed.forward(20)
        seaweed.left(45)
    seaweed.right(90)
    seaweed.forward(height * 40)  # the height of the seaweed
    seaweed.left(90)
    seaweed.end_fill()
    seaweed.hideturtle()

# Draw aquarium decorations
draw_seaweed(-100, -150, 5, 'darkgreen')
draw_seaweed(-50, -150, 4, 'green')
draw_seaweed(0, -150, 6, 'darkgreen')
draw_seaweed(50, -150, 3, 'green')
draw_seaweed(100, -150, 5, 'darkgreen')

# Draw fish
draw_fish(-60, 0, 'orange')
draw_fish(60, 50, 'yellow')
draw_fish(0, -50, 'purple')
draw_fish(-30, 100, 'red')
draw_fish(90, -100, 'blue')

# Hide turtle and display the result
turtle.hideturtle()
turtle.done()
