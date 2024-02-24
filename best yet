import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
color_depths = [(10, 24, 120), (25, 50, 160), (65, 105, 225), (100, 149, 237), (135, 206, 250)]
sky_color = (135, 206, 235)  # Sky blue
sun_color = (255, 255, 0)  # Sun yellow
cloud_color = (255, 255, 255)  # Cloud white
water_base_color = [5, 10, 60]  # Base darker blue for water
mountain_color = (169, 169, 169)  # Dark grey for mountains
landscape_color = (34, 139, 34)  # Forest green for landscape
grass_color = (0, 128, 0)  # Grass green
snow_color = (255, 250, 250)  # Snow white
flower_color = (255, 0, 255)  # Magenta for flowers

# Water particle settings
particle_radius = 2
particle_count = 11250
gravity = 0.1
particles = []

# Timing
clock = pygame.time.Clock()

# Clouds data
clouds = []

# Generate clouds data for bunched up clouds
for _ in range(3):
    cloud_parts = []
    base_x = random.randint(50, screen_width - 150)
    base_y = random.randint(50, 150)
    for _ in range(random.randint(5, 8)):
        offset_x = random.randint(-50, 50)
        offset_y = random.randint(-30, 30)
        part = {'x': base_x + offset_x, 'y': base_y + offset_y, 'radius': random.randint(20, 50)}
        cloud_parts.append(part)
    clouds.append(cloud_parts)


# Function to draw grass
def draw_grass():
    sway_frequency = 0.002  # Adjust the frequency of the sine wave for slower movement
    sway_amplitude = 1  # Adjust the amplitude of the sine wave for smoother movement
    color_change_frequency = 0.1  # Adjust the frequency of color change for slower transition
    for pos in grass_positions:
        x, y = pos
        height = random.randint(5, 15)  # Random height of the grass blade
        sway = math.sin(x * sway_frequency) * sway_amplitude  # Swaying motion based on x-coordinate
        # Adjust color change
        color = (0, 100 + int(100 * math.sin(x * color_change_frequency)), 0)  # Methodical color change
        pygame.draw.line(screen, color, (x, y), (x + sway, y - height), 2)



# Function to draw flowers with fixed colors
def draw_flowers():
    flower_colors = [(255, 0, 255), (255, 69, 0), (255, 165, 0), (255, 255, 0), (127, 255, 0)]  # Color palette for flowers
    for i, pos in enumerate(flower_positions):
        x, y = pos
        color = flower_colors[i % len(flower_colors)]  # Cycle through the color palette for each flower
        pygame.draw.circle(screen, color, (x, y), 3)



# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.depth = 0
        self.velocity_y = random.uniform(0, 0.5)  # Adjusted velocity for slower movement

    def update(self):
        self.velocity_y += gravity
        self.y += self.velocity_y
        if self.y >= screen_height - particle_radius:
            self.y = screen_height - particle_radius
            self.velocity_y *= -0.9
            self.depth = min(self.depth + 1, len(color_depths) - 1)

    def draw(self):
        color = color_depths[self.depth]
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), particle_radius)


# Create initial particles starting from halfway down the screen
for _ in range(particle_count):
    particles.append(Particle(random.randint(0, screen_width), random.randint(screen_height // 2, screen_height)))


# Function to draw sun
def draw_sun():
    pygame.draw.circle(screen, sun_color, (700, 100), 50)


# Function to draw clouds
def draw_clouds():
    for cloud in clouds:
        for part in cloud:
            pygame.draw.circle(screen, cloud_color, (part['x'], part['y']), part['radius'])


# Function to draw mountains, landscape, and snow caps
def draw_mountains_and_landscape():
    # Mountains
    mountains = [(0, 300), (200, 100), (400, 300), (300, 300), (500, 150), (700, 300), (600, 300), (800, 50),
                 (1000, 300)]
    for i in range(0, len(mountains), 3):
        pygame.draw.polygon(screen, mountain_color, mountains[i:i + 3])
    # Snow caps
    pygame.draw.polygon(screen, snow_color, [(180, 120), (200, 100), (220, 120)])
    pygame.draw.polygon(screen, snow_color, [(480, 170), (500, 150), (520, 170)])
    pygame.draw.polygon(screen, snow_color, [(780, 70), (800, 50), (820, 70)])
    # Landscape, extending to the bottom of the screen
    pygame.draw.rect(screen, landscape_color, (0, 300, screen_width, screen_height - 300))
    # Grass
    draw_grass()
    # Flowers
    draw_flowers()


# Fixed positions for grass
grass_positions = [(random.randint(0, screen_width), random.randint(300, screen_height - 1)) for _ in range(1000)]

# Fixed positions for flowers
flower_positions = [(random.randint(0, screen_width), random.randint(300, screen_height - 1)) for _ in range(50)]

# Function to generate a new random position for a flower above the grass
def generate_flower_position():
    return random.randint(0, screen_width), random.randint(300, screen_height - 1)


# Enhanced draw bird function to look more like a bird
def draw_bird(x, y):
    # Body
    pygame.draw.ellipse(screen, (0, 0, 0), (x, y, 20, 15))
    # Wings
    pygame.draw.polygon(screen, (0, 0, 0), [(x + 5, y + 7), (x + 25, y + 15), (x + 5, y + 20)])
    pygame.draw.polygon(screen, (0, 0, 0), [(x + 15, y + 7), (x + 35, y), (x + 15, y + 20)])
    # Tail
    pygame.draw.lines(screen, (0, 0, 0), False, [(x - 5, y + 10), (x - 15, y + 5), (x - 15, y + 15)], 2)
    # Head
    pygame.draw.circle(screen, (0, 0, 0), (x + 20, y + 7), 5)
    # Beak
    pygame.draw.polygon(screen, (255, 215, 0), [(x + 25, y + 7), (x + 35, y + 5), (x + 25, y + 10)])


# Function to check if a point (mouse click) is within a rectangle (bird's position)
def point_inside_rect(x, y, rect):
    x1, y1, width, height = rect
    return x1 <= x <= x1 + width and y1 <= y <= y1 + height


# Initialize bird variables
bird_position_x = -50
bird_flight_height = random.randint(100, 300)  # Random initial flight height

# Function to generate a new random flight height for the bird above the water level
def generate_flight_height():
    return random.randint(max(100, screen_height // 2), 300)  # Ensure bird starts above water


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift_pressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if shift_pressed:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if point_inside_rect(mouse_x, mouse_y, (bird_position_x, bird_flight_height, 50, 20)):
                    # Shoot the bird
                    bird_position_x = -50  # Reset bird position
                    bird_flight_height = generate_flight_height()  # Generate new flight height

    screen.fill(sky_color)  # Fill screen with sky color

    draw_mountains_and_landscape()
    draw_sun()
    draw_clouds()

    highest_particle = min(particles, key=lambda p: p.y).y
    pygame.draw.rect(screen, tuple(water_base_color),
                     pygame.Rect(0, highest_particle, screen_width, screen_height - highest_particle))

    for particle in particles:
        particle.update()
        particle.draw()

    # Draw the bird if it's time
    elapsed_time = pygame.time.get_ticks() // 1000
    if elapsed_time > 15:
        bird_position_x += 5
        if bird_position_x < screen_width + 50:
            draw_bird(bird_position_x, bird_flight_height)
        else:
            bird_position_x = -50  # Reset bird position
            bird_flight_height = random.randint(100, 300)  # New flight height for the bird

    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 FPS

pygame.quit()
sys.exit()
