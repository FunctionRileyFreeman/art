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
VINE_RADIUS = 2
MIN_DISTANCE = 2 * VINE_RADIUS
MAX_GENERATION_DEPTH = 8
BRANCH_LENGTH = 40  # Increase the branch length for stretching

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stretchy Procedural Vine Generator")

# List to store vine segments
vines = []

# Function to generate a vine segment
def generate_vine(x, y, angle, generation_depth):
    if generation_depth <= 0:
        return

    end_x = x + BRANCH_LENGTH * math.cos(angle)
    end_y = y + BRANCH_LENGTH * math.sin(angle)
    vine_segment = ((x, y), (end_x, end_y))
    vines.append(vine_segment)

    # Generate new branches with slight deviations
    new_angle1 = angle + random.uniform(-math.pi / 8, math.pi / 8)
    new_angle2 = angle + random.uniform(-math.pi / 8, math.pi / 8)

    generate_vine(end_x, end_y, new_angle1, generation_depth - 1)
    generate_vine(end_x, end_y, new_angle2, generation_depth - 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Generate the vine
    vines = []
    start_x = SCREEN_WIDTH // 2
    start_y = SCREEN_HEIGHT
    generate_vine(start_x, start_y, -math.pi / 2, MAX_GENERATION_DEPTH)

    # Draw vines
    for vine in vines:
        pygame.draw.line(screen, VINE_COLOR, vine[0], vine[1], VINE_RADIUS * 2)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
