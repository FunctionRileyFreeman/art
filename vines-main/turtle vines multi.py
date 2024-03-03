import turtle
import random
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
vine = turtle.Turtle()
vine.speed(0)
vine.color("green")

# List to store starting points
starting_points = []


# Function to generate random starting points that avoid each other
def generate_starting_points(num_points, min_distance):
    for _ in range(num_points):
        while True:
            x = random.randint(-400, 400)
            y = random.randint(-300, -50)
            point = (x, y)
            if all(math.sqrt((x - px) ** 2 + (y - py) ** 2) > min_distance for px, py in starting_points):
                starting_points.append(point)
                break


# Function to draw a vine segment
def draw_vine(branch_length):
    if branch_length > 10:
        # Draw the main vine
        vine.forward(branch_length)
        vine.right(20)  # Adjust the angle for a more sprawling vine

        # Create smaller branches
        for _ in range(2):
            vine.forward(branch_length // 2)
            vine.left(45)
            draw_vine(branch_length // 2)
            vine.right(45)
            vine.backward(branch_length // 2)

        # Return to the original position
        vine.left(20)
        vine.backward(branch_length)

        # Add leaves randomly
        if random.random() < 0.1:  # Adjust the probability as needed
            draw_leaf(vine.pos())  # Draw a tear-drop shaped leaf

        # Add vines growing from random starting points
        if random.random() < 0.1:  # Adjust the probability as needed
            draw_new_vine(random.choice(starting_points))


# Function to draw a tear-drop shaped leaf
def draw_leaf(position):
    vine.penup()
    vine.goto(position)
    vine.pendown()
    vine.color("green")
    vine.begin_fill()
    vine.left(150)
    vine.forward(20)
    vine.circle(10, 120)
    vine.forward(20)
    vine.circle(10, 120)
    vine.end_fill()
    vine.setheading(0)


# Function to draw a new vine segment
def draw_new_vine(position):
    vine.penup()
    vine.goto(position)
    vine.pendown()
    vine.color("green")
    vine.setheading(random.randint(60, 120))
    draw_vine(random.randint(30, 80))


# Generate starting points
generate_starting_points(5, 100)

# Set the initial position and draw vines from each starting point
for start_point in starting_points:
    vine.penup()
    vine.goto(start_point)
    vine.pendown()
    draw_vine(200)  # Adjust the initial branch length

# Close the turtle graphics window on click
screen.exitonclick()
