import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for Crack Cocaine visualization
fig_crack, ax_crack = plt.subplots(figsize=(8, 8))

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_crack = np.random.rand(50, 50)

# Apply Crack Cocaine effect by enhancing neural activity
neural_activity_crack = neural_activity_crack ** 3

# Display the neural activity as an image
ax_crack.imshow(neural_activity_crack, cmap='hot', interpolation='nearest')

# Add title and remove axes
ax_crack.set_title('Neural Activity Under Crack Cocaine Influence')
ax_crack.axis('off')

# Show the plot for Crack Cocaine
plt.show()
