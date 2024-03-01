import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity = np.random.rand(50, 50)

# Apply MDMA effect by enhancing neural activity
neural_activity = neural_activity ** 3

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax.imshow(neural_activity, cmap='hot', interpolation='nearest')

# Add title and remove axes
ax.set_title('Neural Activity Under MDMA Influence')
ax.axis('off')

# Show the plot
plt.show()
