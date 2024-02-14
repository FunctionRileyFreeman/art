import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np
import random

def draw_person(ax, x, y, size):
    # Head
    head_color = np.random.rand(3,)  # Random color for the head
    ax.plot([x], [y], 'o', color=head_color, markersize=size*0.1)

    # Body
    body_color = np.random.rand(3,)  # Random color for the body
    ax.plot([x, x], [y-size*0.3, y-size*0.7], '-', color=body_color, linewidth=size*0.05)

    # Arms
    arm_color = np.random.rand(3,)  # Random color for the arms
    ax.plot([x, x-size*0.2], [y-size*0.5, y-size*0.5], '-', color=arm_color, linewidth=size*0.02*size)
    ax.plot([x, x+size*0.2], [y-size*0.5, y-size*0.5], '-', color=arm_color, linewidth=size*0.02*size)

    # Legs
    leg_color = np.random.rand(3,)  # Random color for the legs
    ax.plot([x, x-size*0.1], [y-size*0.7, y-size*1.1], '-', color=leg_color, linewidth=size*0.03*size)
    ax.plot([x, x+size*0.1], [y-size*0.7, y-size*1.1], '-', color=leg_color, linewidth=size*0.03*size)

def draw_dog(ax, x, y, size):
    # Head
    head_color = np.random.rand(3,)  # Random color for the head
    ax.plot([x], [y], 'o', color=head_color, markersize=size*0.1)

    # Body
    body_color = np.random.rand(3,)  # Random color for the body
    ax.plot([x, x], [y-size*0.3, y-size*0.7], '-', color=body_color, linewidth=size*0.05)

    # Legs
    leg_color = np.random.rand(3,)  # Random color for the legs
    ax.plot([x, x-size*0.1], [y-size*0.5, y-size*0.9], '-', color=leg_color, linewidth=size*0.04*size)
    ax.plot([x, x+size*0.1], [y-size*0.5, y-size*0.9], '-', color=leg_color, linewidth=size*0.04*size)

def draw_cat(ax, x, y, size):
    # Head
    head_color = np.random.rand(3,)  # Random color for the head
    ax.plot([x], [y], 'o', color=head_color, markersize=size*0.1)

    # Body
    body_color = np.random.rand(3,)  # Random color for the body
    ax.plot([x, x], [y-size*0.3, y-size*0.7], '-', color=body_color, linewidth=size*0.05)

    # Legs
    leg_color = np.random.rand(3,)  # Random color for the legs
    ax.plot([x, x-size*0.1], [y-size*0.5, y-size*0.9], '-', color=leg_color, linewidth=size*0.02*size)
    ax.plot([x, x+size*0.1], [y-size*0.5, y-size*0.9], '-', color=leg_color, linewidth=size*0.02*size)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Generate random people, dogs, and cats
num_people = 100
num_dogs = 50
num_cats = 50
for _ in range(num_people):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    size = random.uniform(1, 5)
    draw_person(ax, x, y, size)

for _ in range(num_dogs):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    size = random.uniform(1, 5)
    draw_dog(ax, x, y, size)

for _ in range(num_cats):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    size = random.uniform(1, 5)
    draw_cat(ax, x, y, size)

# Adjust the aspect ratio and axis limits
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Remove axis ticks
ax.set_xticks([])
ax.set_yticks([])

# Remove axis spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Show the plot
plt.show()
