import turtle
import random
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# List to store turtles and their starting points
turtles = []
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


# Function to draw a vine segment with smoother S-shaped turns
def draw_vine(turtle_obj, branch_length, color, thickness):
    if branch_length > 5:
        # Set color with gradient
        turtle_obj.pensize(thickness)
        turtle_obj.color(color)

        # Introduce randomness to the movement
        angle_variation = random.uniform(-10, 10)
        turtle_obj.right(90 + angle_variation)

        # Simulate wind effect by adding fluctuations to forward movement
        for _ in range(int(branch_length / 2)):
            turtle_obj.forward(2 + random.uniform(-1, 1))
            turtle_obj.right(angle_variation)

        # Introduce more randomness to the movement
        angle_variation = random.uniform(-10, 10)
        turtle_obj.left(90 + angle_variation)

        # Continue drawing the vine
        for _ in range(int(branch_length / 2)):
            turtle_obj.forward(2 + random.uniform(-1, 1))
            turtle_obj.right(angle_variation)

        # Return to the original position
        turtle_obj.left(90 - angle_variation)
        turtle_obj.backward(branch_length)

        # Add leaves randomly with spacing
        if random.random() < 0.05:
            draw_leaf(turtle_obj)

        # Add vines growing from random starting points
        if random.random() < 0.1:
            draw_new_vine(turtle_obj)


# Function to draw a leaf with soft red patterns
def draw_leaf(turtle_obj):
    position = turtle_obj.pos()
    turtle_obj.penup()
    turtle_obj.goto(position)
    turtle_obj.pendown()

    # Vary leaf size
    leaf_size = random.randint(15, 25)

    # Draw the leaf in green
    turtle_obj.color("green")
    turtle_obj.begin_fill()
    turtle_obj.left(150)
    turtle_obj.forward(leaf_size)
    turtle_obj.circle(leaf_size / 2, 120)
    turtle_obj.forward(leaf_size)
    turtle_obj.circle(leaf_size / 2, 120)
    turtle_obj.end_fill()
    turtle_obj.setheading(0)

    # Add soft red patterns to the leaf
    position = (position[0] - 5, position[1] + 15)
    turtle_obj.penup()
    turtle_obj.goto(position)
    turtle_obj.pendown()
    turtle_obj.color("red")
    turtle_obj.begin_fill()
    turtle_obj.circle(leaf_size / 4)
    turtle_obj.end_fill()


# Function to draw a new vine segment
def draw_new_vine(turtle_obj):
    position = turtle_obj.pos()
    turtle_obj.penup()
    turtle_obj.goto(position)
    turtle_obj.pendown()
    turtle_obj.color("green")
    turtle_obj.pensize(3)  # Set a default thickness

    # Generate a gradient of green colors
    for _ in range(5):
        color = (0, random.uniform(0.4, 0.8), 0)  # Vary the green component
        thickness = random.uniform(2, 5)  # Vary thickness
        draw_vine(turtle_obj, random.randint(20, 80), color, thickness)  # Vary the branch length


# Create multiple turtle objects
num_turtles = 5  # You can adjust the number of turtles
generate_starting_points(num_turtles, 100)

for i in range(num_turtles):
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    new_turtle.penup()
    starting_point = starting_points.pop()  # Get and remove a starting point
    new_turtle.goto(starting_point)
    new_turtle.pendown()
    turtles.append(new_turtle)

# Set the initial position and draw vines for each turtle
for turtle_obj in turtles:
    draw_new_vine(turtle_obj)

# Close the turtle graphics window on click
screen.exitonclick()
