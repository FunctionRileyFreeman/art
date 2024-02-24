import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors for depth
color_depths = [
    (10, 24, 120),   # Dark Blue
    (25, 50, 160),   # Medium Dark Blue
    (65, 105, 225),  # Royal Blue
    (100, 149, 237), # Cornflower Blue
    (135, 206, 250), # Light Sky Blue
]

# Water particle settings
particle_radius = 2
particle_count = 5000  # Increased particle count
gravity = 0.1
particles = []

# Particle class with depth
class Particle:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth  # Depth attribute
        self.velocity_y = random.uniform(0, 1)

    def update(self):
        self.velocity_y += gravity
        self.y += self.velocity_y
        
        # Bounce off the bottom of the screen
        if self.y >= screen_height - particle_radius:
            self.y = screen_height - particle_radius
            self.velocity_y *= -0.9

    def draw(self):
        # Change color based on depth
        color = color_depths[self.depth]
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), particle_radius)

# Create initial particles with varying depths
for _ in range(particle_count):
    depth = random.randint(0, len(color_depths) - 1)
    particles.append(Particle(random.randint(0, screen_width), random.randint(0, screen_height), depth))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill screen with black background

    for particle in particles:
        particle.update()
        particle.draw()

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
sys.exit()
