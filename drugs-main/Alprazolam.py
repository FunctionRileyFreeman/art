import matplotlib
matplotlib.use('TkAgg')  # Specify the backend
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for Xanax visualization
fig_xanax, ax_xanax = plt.subplots(figsize=(8, 8))

# Create a random matrix representing neural activity
np.random.seed(42)
neural_activity_xanax = np.random.rand(50, 50)

# Apply Xanax effect by smoothing neural activity
neural_activity_xanax = np.convolve(neural_activity_xanax.flatten(), np.ones(5)/5, mode='same').reshape(50, 50)

# Display the neural activity as an image
ax_xanax.imshow(neural_activity_xanax, cmap='cividis', interpolation='nearest')

# Add title and remove axes
ax_xanax.set_title('Neural Activity Under Xanax Influence')
ax_xanax.axis('off')

# Show the plot for Xanax
plt.show()
