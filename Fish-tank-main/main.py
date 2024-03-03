import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for a larger and higher resolution screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
BORDER_THICKNESS = 2  # Thickness of the border around the fish
EYE_RADIUS = 4        # Radius of the eye, slightly increased due to larger resolution
FISH_SPEED = 3        # Increased speed for larger screen
DIRECTION_CHANGE_PROB = 0.02  # Probability of changing direction
CORAL_COUNT = 15      # Increased number of coral shapes

# Colors
BLUE = (0, 128, 255)
BLACK = (0, 0, 0)
CORAL_COLORS = [(255, 102, 102), (255, 178, 102), (255, 229, 204), (255, 204, 229)]  # Different coral colors

def draw_coral(surface):
    for _ in range(CORAL_COUNT):
        coral_color = random.choice(CORAL_COLORS)
        coral_x = random.randint(0, SCREEN_WIDTH)
        coral_y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - 50)
        coral_width = random.randint(15, 45)  # Increased size for coral
        coral_height = random.randint(30, 150)
        pygame.draw.ellipse(surface, coral_color, (coral_x, coral_y, coral_width, coral_height))

def draw_fish(surface, fish):
    center = fish.position
    radius = fish.radius
    flip = fish.direction

    # Fish body calculations
    if fish.shape == 'circle':
        body_rect = (center[0] - radius, center[1] - radius, 2 * radius, 2 * radius)
    elif fish.shape == 'oval':
        body_rect = (center[0] - radius, center[1] - radius // 2, 2 * radius, radius)

    # Flip the fish if needed
    if flip:
        tail_origin = (center[0] + radius, center[1])
        eye_center = (center[0] - radius + EYE_RADIUS + 2, center[1])
    else:
        tail_origin = (center[0] - radius, center[1])
        eye_center = (center[0] + radius - EYE_RADIUS - 2, center[1])

    # Draw the fish body (a circle or ellipse)
    pygame.draw.ellipse(surface, BLACK, body_rect, BORDER_THICKNESS)
    pygame.draw.ellipse(surface, fish.color, body_rect)

    # Draw patterns like stripes
    if fish.pattern == 'stripes':
        stripe_width = 2  # Thin stripe width
        stripe_count = 5 if fish.shape == 'circle' else 7  # Number of stripes
        for i in range(stripe_count):
            stripe_x = center[0] - radius + i * (2 * radius // stripe_count) if not flip else center[0] + radius - (i + 1) * (2 * radius // stripe_count)
            stripe_rect = (stripe_x, center[1] - radius // 2, stripe_width, radius if fish.shape == 'circle' else radius // 2)
            pygame.draw.rect(surface, BLACK, stripe_rect)

    # Draw the tail of the fish (a triangle with a border)
    tail_points = [tail_origin,
                   (tail_origin[0] - fish.tail_size[0] * (-1 if flip else 1), tail_origin[1] - fish.tail_size[1] // 2),
                   (tail_origin[0] - fish.tail_size[0] * (-1 if flip else 1), tail_origin[1] + fish.tail_size[1] // 2)]
    pygame.draw.polygon(surface, BLACK, tail_points, BORDER_THICKNESS)
    pygame.draw.polygon(surface, fish.color, tail_points)

    # Draw the eye on the correct side
    pygame.draw.circle(surface, BLACK, eye_center, EYE_RADIUS)

class Fish:
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(20, 35)  # Increased radius range for larger fish
        self.tail_size = (self.radius // 2, self.radius)  # Tail size relative to body radius
        self.shape = random.choice(['circle', 'oval'])
        self.pattern = random.choice(['none', 'stripes'])
        self.position = [random.randint(self.radius, SCREEN_WIDTH - self.radius),
                         random.randint(self.radius, SCREEN_HEIGHT - self.radius)]
        self.rect = pygame.Rect(self.position[0] - self.radius, self.position[1] - self.radius,
                                2 * self.radius, 2 * self.radius)
        self.direction = random.choice([True, False])
        self.dragging = False

    def swim(self):
        if not self.dragging:
            self.position[0] += FISH_SPEED if self.direction else -FISH_SPEED
            self.position[1] += random.randint(-2, 2)
            if random.random() < DIRECTION_CHANGE_PROB:
                self.direction = not self.direction
            if self.position[0] < self.radius or self.position[0] > SCREEN_WIDTH - self.radius:
                self.direction = not self.direction
            self.position[0] = max(self.radius, min(self.position[0], SCREEN_WIDTH - self.radius))
            self.position[1] = max(self.radius, min(self.position[1], SCREEN_HEIGHT - self.radius))
            self.rect.x = self.position[0] - self.radius
            self.rect.y = self.position[1] - self.radius

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fish Tank Simulation")

# Create a surface for coral
coral_surface = pygame.Surface(screen.get_size())
coral_surface.set_colorkey((0, 0, 0))
draw_coral(coral_surface)

# Create fish
fishes = [Fish() for _ in range(7)]  # Slightly more fish for a larger tank

# Game loop
running = True
clock = pygame.time.Clock()
selected_fish = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for fish in fishes:
                if fish.rect.collidepoint(event.pos):
                    fish.dragging = True
                    selected_fish = fish
                    mouse_x, mouse_y = event.pos
                    offset_x = fish.position[0] - mouse_x
                    offset_y = fish.position[1] - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_fish:
                selected_fish.dragging = False
            selected_fish = None
        elif event.type == pygame.MOUSEMOTION:
            if selected_fish and selected_fish.dragging:
                mouse_x, mouse_y = event.pos
                selected_fish.position[0] = mouse_x + offset_x
                selected_fish.position[1] = mouse_y + offset_y
                selected_fish.rect.x = selected_fish.position[0] - selected_fish.radius
                selected_fish.rect.y = selected_fish.position[1] - selected_fish.radius

    for fish in fishes:
        fish.swim()

    screen.fill(BLUE)
    screen.blit(coral_surface, (0, 0))

    for fish in fishes:
        draw_fish(screen, fish)

    pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
