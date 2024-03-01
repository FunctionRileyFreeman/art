import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_cocaine = np.random.rand(50, 50)

# Apply Cocaine effect by enhancing neural activity
neural_activity_cocaine = neural_activity_cocaine ** 2

# Create a figure and axis for Cocaine visualization
fig_cocaine, ax_cocaine = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax_cocaine.imshow(neural_activity_cocaine, cmap='hot', interpolation='nearest')

# Add title and remove axes
ax_cocaine.set_title('Neural Activity Under Cocaine Influence')
ax_cocaine.axis('off')

# Show the plot for Cocaine
plt.show()
