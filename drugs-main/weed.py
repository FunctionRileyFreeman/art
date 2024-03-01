import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_weed = np.random.rand(50, 50)

# Apply Weed effect by distorting neural activity
neural_activity_weed = np.random.rand(50, 50) * neural_activity_weed ** 2

# Create a figure and axis for Weed visualization
fig_weed, ax_weed = plt.subplots(figsize=(8, 8))

# Display the neural activity as an image
ax_weed.imshow(neural_activity_weed, cmap='cividis', interpolation='nearest')

# Add title and remove axes
ax_weed.set_title('Neural Activity Under Weed Influence')
ax_weed.axis('off')

# Show the plot for Weed
plt.show()
