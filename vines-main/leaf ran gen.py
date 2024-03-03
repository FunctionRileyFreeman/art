import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
VINE_COLOR = (0, 128, 0)
VINE_RADIUS = 5
MIN_DISTANCE = 2 * VINE_RADIUS

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vine Generator")

# List to store vine segments
vines = []

# Function to generate a random starting point while avoiding other vines
def generate_starting_point():
    while True:
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        point = (x, y)
        if all(math.sqrt((x - px) ** 2 + (y - py) ** 2) > MIN_DISTANCE for px, py in vines):
            return point

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate and draw vines
    if len(vines) < 100:  # Number of vines to generate
        start_point = generate_starting_point()
        vines.append(start_point)

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw vines
    for vine in vines:
        pygame.draw.circle(screen, VINE_COLOR, vine, VINE_RADIUS)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
