import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
VINE_COLOR = (0, 128, 0)
VINE_RADIUS = 2
MIN_DISTANCE = 2 * VINE_RADIUS
BRANCH_LENGTH = 40
GENERATION_DELAY = 0.1  # Delay between generations (in seconds)
AVOIDANCE_PROBABILITY = 0.2  # Probability of avoiding self-overlap

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Continuous Vine Generator")

# List to store vine segments
vines = []


# Function to generate a vine segment
def generate_vine(x, y, angle):
    end_x = x + BRANCH_LENGTH * math.cos(angle)
    end_y = y - BRANCH_LENGTH * math.sin(angle)  # Positive sin for upward growth
    vine_segment = ((x, y), (end_x, end_y))

    # Check if the vine segment is within bounds
    if 0 <= end_x <= SCREEN_WIDTH and 0 <= end_y <= SCREEN_HEIGHT:
        # Check for self-avoidance with a probability
        if random.random() > AVOIDANCE_PROBABILITY or all(
                math.sqrt((end_x - px) ** 2 + (end_y - py) ** 2) > MIN_DISTANCE for (px, py), _ in vines
        ):
            vines.append(vine_segment)  # Store the vine segment


# Main loop
running = True
previous_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            # Generate a new vine at a random point on the grid
            random_x = random.randint(0, SCREEN_WIDTH)
            random_y = random.randint(0, SCREEN_HEIGHT)
            generate_vine(random_x, random_y, math.pi / 4)  # Positive angle for upward growth

    # Generate and draw a new vine segment periodically
    current_time = time.time()
    if current_time - previous_time >= GENERATION_DELAY:
        previous_time = current_time
        if len(vines) == 0:
            start_x = SCREEN_WIDTH // 2
            start_y = SCREEN_HEIGHT
            generate_vine(start_x, start_y, math.pi / 4)  # Positive angle for upward growth
        else:
            last_vine = vines[-1]
            _, last_y = last_vine[1]
            new_angle = last_vine[1][0] + random.uniform(-math.pi / 3, math.pi / 3)  # More randomness
            generate_vine(last_vine[1][0], last_y, new_angle)  # Twisting and turning

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw vines
    for vine_segment in vines:
        pygame.draw.line(screen, VINE_COLOR, vine_segment[0], vine_segment[1], VINE_RADIUS * 2)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
