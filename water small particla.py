import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
water_color = (30, 144, 255)  # Dodger Blue
background_color = (0, 0, 0)  # Black

# Water particle settings
particle_radius = 2
particle_count = 1000
gravity = 0.1
particles = []

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_y = random.uniform(0, 1)

    def update(self):
        self.velocity_y += gravity
        self.y += self.velocity_y
        
        # Bounce off the bottom of the screen
        if self.y >= screen_height - particle_radius:
            self.y = screen_height - particle_radius
            self.velocity_y *= -0.9

    def draw(self):
        pygame.draw.circle(screen, water_color, (int(self.x), int(self.y)), particle_radius)

# Create initial particles
for _ in range(particle_count):
    particles.append(Particle(random.randint(0, screen_width), random.randint(0, screen_height)))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    for particle in particles:
        particle.update()
        particle.draw()

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
sys.exit()
